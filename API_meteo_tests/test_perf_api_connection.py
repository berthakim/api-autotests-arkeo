import pytest
import requests
import queue
import threading
import sys
import time


# offline (if you launch the app in your local machine)
url_local = "http://127.0.0.1:8000/stations"
# online (if you use the heroku web site)
url_heroku = ""
# choose offline or online option from above
url = url_local


def test_check_api_responses():
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Test failed with response status code {response.status_code}")
        return "failed", response.elapsed.total_seconds()
    elif response.headers["Content-Type"] != "application/json":
        print(f'Test failed. The content type is: {response.headers["Content-Type"]}')
        return "failed", response.elapsed.total_seconds()
    else:
        print("Test passed")
        return "passed", response.elapsed.total_seconds()


queue_results = queue.Queue()
start_time = 0
event_time_up = threading.Event()

def loop_test(loop_wait=0, loop_times=sys.maxsize):
    looped_times = 0    
    while (looped_times < loop_times and not event_time_up.is_set()):
        # run an API test
        test_result, elapsed_time = test_check_api_responses()           
        # put results into a queue for statistics
        queue_results.put(['test_check_api_responses', test_result, elapsed_time])
        
        # You can add more API tests in a loop here.        
        looped_times += 1
        time.sleep(loop_wait)


# calculate performance metrics
def stats():
    # request per second
    rps_mean = 0
    total_tested_requests = 0
    total_pass_requests = 0
    # time per request
    tpr_min = 999
    tpr_mean = 0
    tpr_max = 0
    sum_response_time = 0
    # failures
    total_fail_requests = 0
    total_exception_requests = 0

    global start_time
    end_time = time.time()
    # get the approximate queue size
    qsize = queue_results.qsize()
    loop = 0
    for i in range(qsize):
        try:
            result=queue_results.get_nowait()
            loop +=1
        except Empty:
            break
        # calc stats
        if result[1] == 'exception':
            total_exception_requests += 1
        elif result[1] == 'failed':
            total_fail_requests += 1
        elif result[1] == 'passed':
            total_pass_requests += 1
            sum_response_time += result[2]
            # update min and max time per request
            if result[2] < tpr_min:
                tpr_min = result[2]
            if result[2] > tpr_max:
                tpr_max = result[2]
        
    total_tested_requests += loop   
    # time per requests - mean (avg)
    if total_pass_requests != 0:
        tpr_mean = sum_response_time / total_pass_requests
    
    # requests per second - mean
    if start_time == 0:
        # log.error('stats: self.start_time is not set, skipping rps stats.')
        print('stats: start_time is not set, skipping rps stats.')
    else:
        tested_time = end_time - start_time
        rps_mean = total_pass_requests / tested_time
    
    # print stats
    print('\n-----------------Test Statistics---------------')
    print(time.asctime())
    print(f'Total requests: {total_tested_requests},\
        pass: {total_pass_requests},\
        fail: {total_fail_requests},\
        exception: {total_exception_requests}')

    if total_pass_requests > 0:
        print('For pass requests:') 
        print(f'Request per Second - mean: {rps_mean:.0f}')
        print('Time per Request   - mean: %.6f, min: %.6f, max: %.6f' 
            % (tpr_mean, tpr_min, tpr_max))    
                          

def loop_stats():
        """ print stats in an interval(secs) continunously
        
        Run this as a separate thread so it won't block the main thread.
        """
        while (not event_time_up.is_set() and not event_test_done.is_set()):
            sleep(interval)
            stats()


def set_event_time_up():
    if not event_time_up.is_set():
        event_time_up.set()


# run concurrent performance tests
if __name__ == '__main__':
    """ Test Settings 
    Concurrent users
    """
    concurrent_users = 2
    loop_times = 100
    test_time = 5 # time in seconds, e.g. 36000
    
    workers = []
    start_time = time.time()
    print(f'Tests started at {start_time}\n')
    
    # start concurrent user threads
    for i in range(concurrent_users):
        thread = threading.Thread(target=loop_test, kwargs={'loop_times': loop_times}, daemon=True)         
        thread.start()
        workers.append(thread)

    timer = threading.Timer(test_time, set_event_time_up)
    timer.start()

    # Block until all threads finish.
    for w in workers:
        w.join()

    # stop timer if loop_times is reached first.
    if not event_time_up.is_set():
        timer.cancel() 
        
    end_time = time.time()

    # Performance stats
    stats()
    print(f'\nTests ended at {end_time}' )
    print(f'Total test time: {round((end_time - start_time), 3)} seconds')
