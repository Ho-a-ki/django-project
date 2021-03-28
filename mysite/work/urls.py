from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='work_list'),
    path('new/', views.new_view, name='new_work'),
]

