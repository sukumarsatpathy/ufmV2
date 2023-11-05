from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # User Management
    path('user/', views.userListView, name='userList'),  # Read
    path('user/add/', views.userAddView, name='userAdd'),  # Create
    path('user/edit/<int:pk>', views.userEditView, name='userEdit'),  # Update
    path('user/delete/<int:pk>', views.userDeleteView, name='userDelete'),  # Delete

    path('addr-edit/<int:pk>/', views.addressEditView, name='addressEdit'),  # Update
]