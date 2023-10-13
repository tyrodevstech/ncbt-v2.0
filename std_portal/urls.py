from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('financialcollege/',views.financial_college_view,name='financialcollege'),
    path('financial/',views.financial_view,name='financial'),
    path('result/',views.result_view,name='result'),
    path('enroll/',views.enroll_view,name='enroll'),
    path('login/',views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
    path('',views.index_view,name='dashboard'),
]