from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('user/register/', RegisterEmployeeView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('pricing/', pricing, name='pricing'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('doctor/', doctor, name='doctor'),
    path('department/', department, name='department'),
    path('subscription/fee/<int:cost>/', SubscriptionFee.as_view(), name='payment'),
    path('chareged/', charge, name='charge'),
    path('update/profile/', EditProfileView.as_view(), name='update-profile'),
]