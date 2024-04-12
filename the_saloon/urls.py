from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_user, name='login'),
    path('home/', login_required(views.home), name='home'),
    path('profile_list/', views.profile_list, name='profile_list'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('update_user/', views.update_user, name='update_user'),
    path('shout_like/<int:pk>', views.shout_like, name="shout_like"),
    path('delete_shout/<int:pk>', views.delete_shout, name="delete_shout"),
    path('edit_shout/<int:pk>', views.edit_shout, name="edit_shout"),
    path('upload/', views.upload_image, name='upload_image'),
    path('delete_image/<int:pk>', views.delete_image, name='delete_image'),
]
