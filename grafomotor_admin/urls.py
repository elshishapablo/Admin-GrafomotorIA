from django.contrib import admin
from django.urls import path
from terapeuta import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),
]

