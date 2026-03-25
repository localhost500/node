from django.urls import path
from . import views

urlpatterns = [
    path('', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
    path('redirect/', views.go_to_page2, name='go_to_page2'),
]