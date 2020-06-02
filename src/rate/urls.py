from rate import views

from django.urls import path

app_name = 'rate'

urlpatterns = [
    path('list/', views.RateListView.as_view(), name='list'),
]
