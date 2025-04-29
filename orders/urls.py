from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('order/create/', views.create_order, name='create_order'),  # Changed this line
    path('profile/', views.profile, name='profile'),
    path('admin/orders/', views.admin_orders, name='admin_orders'),
    path('order/edit/<int:pk>/', views.edit_order, name='edit_order'),
    path('order/delete/<int:pk>/', views.delete_order, name='delete_order'),
]
