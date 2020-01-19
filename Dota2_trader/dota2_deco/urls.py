from django.urls import path
 
from . import views
app_name = 'dota2_deco'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('search_keyword/',views.search, name='search'),
]
