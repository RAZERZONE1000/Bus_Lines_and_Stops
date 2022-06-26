from django.urls import path
from . import views


# app_name = ''

urlpatterns = [
    # path('', views.AutobuskeLinijeView, name='autobuske_linije'),
    # path('add_stajaliste/', views.AddStajalisteView, name='add_stajaliste'),
    # path('add_linija/', views.AddLinijaView, name='add_linija'),
    # path('stajaliste_create/', views.stajaliste_create_view, name='stajaliste_create_form'),
    # path('linija_create/', views.linija_create_view, name='linija_create_form'),    
    path('stajaliste_create/', views.StajalisteCreateView.as_view(), name='stajaliste_create'),
    path('linija_create/', views.LinijaCreateView.as_view(), name='linija_create'),
    path('stajalista/', views.StajalisteListView.as_view(), name='stajaliste_list'),
    path('', views.LinijaListView.as_view(), name='linija_list'),
    path('<int:id>/update/', views.LinijaUpdateView.as_view(), name='linija_update'),
    path('stajalista/<int:id>/update/', views.StajalisteUpdateView.as_view(), name='stajaliste_update'),
    path('<int:id>/delete/', views.LinijaDeleteView.as_view(), name='linija_delete'),
    path('stajalista/<int:id>/delete/', views.StajalisteDeleteView.as_view(), name='stajaliste_delete'),
    path('<int:pk>/', views.LinijaDetailView.as_view(), name='linija_detail'),
    path('stajalista/<int:pk>/', views.StajalisteDetailView.as_view(), name='stajaliste_detail'),
]
