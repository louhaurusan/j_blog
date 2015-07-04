from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PostsView.as_view(), name="post_list"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="post_detail")
]
