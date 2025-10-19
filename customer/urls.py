from django.urls import path
from . import views
from  django.contrib.auth import views as auth_views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('signup/', views.signup, name='signup'),
    path('', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('user', views.user_list, name='user_profile'),
    path('user/update/', views.user_update, name='user_update'),
    path("api-call/", views.fetch_api_data, name="api_call"),
]
