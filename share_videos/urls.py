"""
URL configuration for share_videos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from halls import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    # AUTH
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    # Hall
    path('hall/create', views.create_hall, name = 'create_hall'),
    path('hall/detail/<int:pk>/', views.detail_hall, name = 'detail_hall'),
    path('hall/update/<int:pk>/', views.update_hall, name = 'update_hall'),
    path('hall/delete/<int:pk>/', views.delete_hall, name = 'delete_hall'),
    # Video
    path('hall/addvideo/<int:pk>/', views.add_video, name = 'add_video'),
    path('hall/searchvideo/', views.search_video, name = 'search_video'),
]

urlpatterns += static(settings.STATIC_URL,
                      document_root = settings.STATIC_ROOT)
