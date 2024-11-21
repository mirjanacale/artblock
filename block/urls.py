from django.urls import path
from codestar import views


urlpatterns = [
    path('<slug:category_slug>/', views.category, name='category_details'),
    path('<slug:category_slug>/<slug:slug>/', views.details, name='post_details'),
    
   ]