from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from arkeo import views


urlpatterns = [
    path('tests/', views.TestList.as_view()),
    path('tests/<int:pk>/', views.TestDetail.as_view()),
]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = format_suffix_patterns(urlpatterns)
