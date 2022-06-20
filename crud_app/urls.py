from django.urls import path

from crud_app import views

urlpatterns = [
    path('', views.GetHome.as_view(), name='home'),
    path('create', views.CreateHome.as_view(), name='create'),
    path('delete', views.DeleteHome.as_view(), name='delete'),
    path('read', views.ReadHome.as_view(), name='read'),
    path('update', views.UpdateHome.as_view(), name='update'),
]