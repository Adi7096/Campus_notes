from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload_note, name='upload_note'),
      path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('download/<int:note_id>/', views.download_note, name='download_note'),
      # path('preview/<int:note_id>/', views.preview_note, name='preview_note'),

]