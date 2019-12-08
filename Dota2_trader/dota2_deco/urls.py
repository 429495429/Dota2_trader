from django.urls import path
 
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('<string:keyword',views.search, name='search'),
]
