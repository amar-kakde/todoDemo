from django.contrib import admin
from django.urls import path, include

from todo import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("todo.urls")),
    path("todo/", include("todo.urls")),
    path("signup/", view=views.signup, name="signup"),
]
