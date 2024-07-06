from django.urls import path

from StudentApp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('display',views.display_fun,name='displaystudent'),
    path('add',views.add_studs,name='addstudent'),
    path('edit/<int:id>',views.edit_studs,name='editstudent'),
    path('delete/<int:id>',views.delete_student,name='deletestudent')
]