from django.urls import path
from api import views
urlpatterns = [
    path('', views.hello),
    path('hello1/<int:pk>/', views.hello1),

]
