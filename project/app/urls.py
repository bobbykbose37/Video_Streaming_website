from django.urls import path
from .import views
from django.conf.urls import url


urlpatterns = [
path('', views.signupp,name="signup"),
    path('loginn/',views.loginn,name="loginn"),
    path('a/',views.home,name="home"),
    path('search',views.search,name="search"),
path('forgot_password',views.forgot_password,name='forgot_password'),
    path('video_page_releases/<int:sid>',views.video_page_releases,name='video_page_releases'),
path('video_page_discover/<int:sid>',views.video_page_discover,name='video_page_discover'),
path('video_page_features/<int:sid>',views.video_page_features,name='video_page_features'),
url(r'^video/(?P<vid>\w+)/$',views.display_video)
]