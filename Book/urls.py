
from .import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('',views.home,name="home"),
    path('show/',views.show,name="show"),
    path('add/',views.add,name="add"),
    path('showemployee/',views.showemployee,name="showemployee"),
    path('addemp/', views.addemp, name='addemp'),
    path('delete/<int:id>', views.deleteb, name='deleteb'),
    path('update/<int:id>', views.updateb, name='updateb'),
    path('deletee/<int:id>', views.deletee, name='deletee'),
    path('updateemp/<int:id>', views.updateemp, name='updateemp'),

]
