from django.conf.urls import url
from task import views

urlpatterns = [

    #  task

    url(r'^$',views.home),
    url(r'^create/',views.create,name='create'),
    url(r'^list/',views.list,name='userlist'),
    url(r'^logout/',views.todo_logout,name='logout'),

    url(r'^update/(?P<pk>[0-9]+)/$',views.todo_update,name='update'),
    url(r'^delete/(?P<pk>[0-9]+)/$',views.todo_delete,name='delete'),
]