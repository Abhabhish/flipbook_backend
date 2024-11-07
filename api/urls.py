from django.urls import path,include
from . import views

urlpatterns = [
    path('register/', views.register,name='register'),
    path('login/', views.login_view,name='login_view'),
    path('get_books/', views.get_books,name='get_books'),
    path('years_list/', views.years_list,name='years_list'),
    path('filter_documents/', views.filter_documents,name='filter_documents'),
]

