from django.urls import path, include

from . import views

app_name = ''

urlpatterns = [
    path('index/', views.MainPage.as_view(), name='home'),
    path("", views.MainPage.as_view()),
    path('thanks/', views.ThanksPage.as_view(), name='thanks'),
    path('signup/', views.SignUp.as_view(), name='signup'),

]
