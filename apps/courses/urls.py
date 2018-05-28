from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^main/add_course$', views.add_course),
    url(r'^main/destroy/(?P<id>\d+)$', views.confirm_delete),
    url(r'^main/destroy/(?P<id>\d+)/destroy$', views.destroy),
  ]