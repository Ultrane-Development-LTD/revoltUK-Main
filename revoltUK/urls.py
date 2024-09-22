from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import signup_view
from .views import submit_vote

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='index.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),  # Ensure next_page is set
    path('signup/', signup_view, name='signup'),
    path('submit_vote/<int:session_id>/', views.submit_vote, name='submit_vote'),
]