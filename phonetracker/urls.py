from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from inventory.views import HomePageView, DeviceDeleteView, DeviceEditView, RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('delete/<int:pk>/', DeviceDeleteView.as_view(), name='delete_device'),
    path('edit/<int:pk>/', DeviceEditView.as_view(), name='edit_device'),
    path('login/', auth_views.LoginView.as_view(template_name='phone/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]