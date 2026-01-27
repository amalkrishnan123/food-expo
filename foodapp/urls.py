from django.urls import path,include
from .import views
# from .views import register_ajax, payment_success
urlpatterns = [
    path('',views.food_home,name='home'),
    path('register/', views.register, name='register'),
    path('partner/register/', views.partner_register, name='partner_register'),
    # path('register/ajax/', register_ajax, name='register_ajax'),
    # path('payment/success/', payment_success, name='payment_success'),
]


