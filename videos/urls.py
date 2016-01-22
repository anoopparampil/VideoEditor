from django.conf.urls import url,include
from views import *

urlpatterns = [
    url(r'^$',HomeView.as_view(),name="home"),
    url(r'^crop-video/$',CropView.as_view(),name="crop_video"),
]