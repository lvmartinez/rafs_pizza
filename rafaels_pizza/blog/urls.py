from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.blog),
    url(r'^post/(?P<p_id>[\w-]+)/?$',  views.post),
    url(r'^category/(?P<c_id>[\-\w]+)/$', views.category)
]
