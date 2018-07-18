from django.urls import path
from django.conf.urls import url, include
from . import views


urlpatterns = [
	path('tickets/', views.index.as_view(), name='ticket-list'),
	path('tickets/<int:pk>/detail/', views.detail.as_view(), name='ticket-detail'),
	path('tickets/users/', views.UserList.as_view(), name='user-list'),
	path('tickets/users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
	path('', views.api_root),
]
