from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>', views.user_id, name='user_id'),
    path("register", views.register_request, name="register"),
]