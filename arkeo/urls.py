from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('', views.TestList.as_view(), name='arkapi-map')
    path('', views.test_list),
    path('snippets/<int:pk>/', views.test_detail),

]

if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = format_suffix_patterns(urlpatterns)