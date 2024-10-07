from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreationListView.as_view(), name='creation_list'),
    path('creation/<int:pk>/', views.CreationDetailView.as_view(), name='creation_detail'),
    path('creation/new/', views.CreationCreateView.as_view(), name='creation_create'),
    path('creation/<int:pk>/comment/', views.add_comment, name='add_comment'),
]