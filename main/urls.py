from django.urls import path
from main import views

urlpatterns = [
    path('', views.ClientListView.as_view()),
    path('create', views.ClientCreateView.as_view()),
    path('<int:pk>/delete', views.ClientDeleteView.as_view()),
    path('<int:pk>/update', views.ClientUpdateView.as_view())
]
