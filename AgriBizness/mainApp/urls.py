from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.home, name='home'),
    path('marketplace/', views.product_list, name='product_list'),
    path('about/', views.about, name='about'), 
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

    # Authentication
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='mainApp/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='product_list'), name='logout'),

    #Farmer
    path('add-product/', views.add_product, name='add_product'),
    path('farmer/dashboard/', views.farmer_dashboard, name='farmer_dashboard'),
    path('farmer/product/<int:pk>/edit/', views.edit_product, name='edit_product'),
    path('farmer/product/<int:pk>/delete/', views.delete_product, name='delete_product'),

    path('farmer/orders/', views.farmer_orders, name='farmer_orders'),
    path('farmer/orders/<int:order_id>/update/', views.update_order_status, name='update_order_status'),


    #Corporate
    path('corporate/orders/', views.corporate_orders, name='corporate_orders'),

]
