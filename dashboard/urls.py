from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index, name= 'dashboard-index' ),
    path ('staff/', views.staff, name= 'dashboard-staff'),
    path ('products/', views.products, name= 'dashboard-products'),
    path ('orders/', views.order, name= 'dashboard-orders'),
]