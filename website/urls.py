from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home_page'),
    path('logout/',views.logout_user,name='logout_user'),
    path('register/',views.register,name='register_page'),
    path('customer_record/<str:pk>/',views.record,name='record_page'),
    path('delete_record/<str:pk>/',views.deleterecord,name='delete_record'),
    path('add_record/',views.addrecord,name='add_record'),
    path('update_record/<str:pk>/',views.updaterecord,name='update_record'),
]