from django.urls import path
from basic_app import views
from basic_app.views import special, user_login

app_name = 'basic_app'

urlpatterns = [
    path('register/',views.register, name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('special/', views.special, name='special'),
    path('user_login/',views.user_login, name='user_login')
]
