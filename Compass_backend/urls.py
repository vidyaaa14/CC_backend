from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 1. Admin panel (standard Django)
    path('admin/', admin.site.urls),
    
    # 2. This points all user-related requests to your 'users' app
    # The URL will be http://127.0.0.1:8000/api/users/register/
    path('api/users/', include('users.urls')),
]