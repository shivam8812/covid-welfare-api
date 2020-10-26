from django.urls import path

from .views import UserDetailView

urlpatterns = [
    path('<str:slug>/', UserDetailView.as_view({'get' : 'list'})),
]