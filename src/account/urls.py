from account import views

from django.urls import path

app_name = 'account'

urlpatterns = [
    path('smoke/', views.smoke, name='smoke'),
    # path('my-profile/<int:pk>/', views.UpdateUserView.as_view(), name='my-profile'),
    path('my-profile/', views.UpdateUserView.as_view(), name='my-profile'),
]
