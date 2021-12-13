from django.db import models
from pygments.formatters.html import HtmlFormatter


station_list = ['Automated observational station', 'Manned synoptic station', 'Virtual station']
STATION_TYPES = [(i, i) for i in station_list]


class MeteoStation(models.Model):
    name = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=50)
    st_type = models.CharField(choices=STATION_TYPES, default="Not defined", max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    obs_beginning = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='stations', default="1", on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name 

    def save(self, *args, **kwargs):
        super(MeteoStation, self).save(*args, **kwargs)
