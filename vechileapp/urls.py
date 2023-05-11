
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('/login', views.login,name='login'),
    path('/signup',views.signup,name='signup'),
    path('task/<int:task_id>/', views.details, name='details'),
    path('logout/',views.logout,name='logout'),
    path('adminview', views.adminview,name='adminview'),
    path('admintask/<int:admintask_id>/', views.admindetail, name='admindetail'),
    path('update/<int:id>/', views.update, name='update'),
]