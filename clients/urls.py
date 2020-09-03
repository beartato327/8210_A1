from django.urls import path
from . import views
from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    CommentCreateView,
    VehicleUpdateView,
    VehicleDetailView,
)


urlpatterns = [
     path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
     path('<int:pk>/',
          ClientDetailView.as_view(), name='client_detail'),
     path('<int:pk>/delete/',
          ClientDeleteView.as_view(), name='client_delete'),
     path('', views.ClientListView.as_view(), name='client_list'),
     path('new/', ClientCreateView.as_view(), name='client_new'),
     path('<int:pk>/new_comment/',
          CommentCreateView.as_view(), name='comment_new'),
     path('<int:pk>/vehicle_edit/',
          VehicleUpdateView.as_view(), name='vehicle_edit'),
     path('<int:pk>/vehicle_detail/',
          VehicleDetailView.as_view(), name='vehicle_detail'),

]
