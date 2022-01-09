from django.urls import path, re_path
from . import views


urlpatterns = [
    path('list/', views.GeoDataList.as_view(), name='geodata-list'),
    path('add/', views.GeoDataCreate.as_view(), name='geodata-add'),
    path('<pk>/', views.IpDetail.as_view(), name='geodata-ip'),
    re_path('^url/(?P<url>.+)/$', views.UrlDetail.as_view(), name='geodata-url'),
]
