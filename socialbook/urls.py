from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signin/', views.signin, name='login'),
    path('signup/', views.signup, name='signup'),
    path('pricing/', views.pricing, name='pricing'),
    path('faq/', views.faq, name='faq'),
]
