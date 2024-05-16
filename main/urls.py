from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main),  # page with links to all apps
    path('admin/', admin.site.urls),
    path('todo/', include('todo_app.urls')),
]