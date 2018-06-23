from django.conf.urls import url
from user import views

urlpatterns = [

    # url(r'^',views.home),

    # user

    url(r'^login/',views.user_login,name='userlogin'),
    url(r'^create/',views.create,name='create'),
    url(r'^home/',views.home,name='home'),
    url(r'^logout/',views.user_logout,name='logout'),

    # url(r'^update/(?P<pk>[0-9]+)/$',views.todo_update),

]