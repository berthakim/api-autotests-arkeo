from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from arkeo import views
from django.conf import settings


urlpatterns = [
    path('stations/', views.MeteoStationList.as_view()),
    path('stations/<int:pk>/', views.MeteoStationDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]

if settings.DEBUG:
    urlpatterns = format_suffix_patterns(urlpatterns)
