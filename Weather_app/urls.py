from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from Weather_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

# urlpatterns += [
#     path('', views.login_view, name='login'),
#     path('signup/', views.signup_view, name="signup"),
#     path('logout', views.logout_view, name='logout'),
# ]