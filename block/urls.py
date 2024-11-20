from django.urls import path
from codestar import views


urlpatterns = [

    path('<slug:slug>/', views.details, name='post_details'),
]

 




