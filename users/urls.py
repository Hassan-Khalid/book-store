from django.urls import path, include

from . import views

app_name = ''

urlpatterns = [
    path('index/', views.MainPage.as_view(), name='home'),
    path("", views.MainPage.as_view()),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('users/', include('django.contrib.auth.urls')),

]
