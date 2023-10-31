from django.urls import path
from file import views
urlpatterns = [

    path('', views.index, name='home'),
    path('login/', views.Login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contents/', views.Download, name='download'),
]
