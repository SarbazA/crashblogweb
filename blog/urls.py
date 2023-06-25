from django.urls import path

from . import views



urlpatterns = [
    path('search/',views.search , name='search'),
    path('<slug:category_slug>/<slug:slug>/', views.detail , name='detail_post' ),
    path('<slug:slug>/' ,views.category , name='amir')
  
    
]