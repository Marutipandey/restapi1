"""
URL configuration for gs14 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views
# from api.views import StudentList

# from api.views import StudentCreate


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('mymodels/', StudentList.as_view(), name='mymodel-list'),
    # path('studentapi/', StudentCreate.as_view(), name='mymodel-list'),
    # path('studentapi/<int:pk>/',views.StudentRetrive.as_view()),
    # path('mymodels/<int:pk>/', StudentList.as_view(), name='mymodel-detail'),
    path('studentapi/', views.LCStudent.as_view(), name='studentapi'),
    path('studentapi/<int:pk>/', views.RUDStudent.as_view(), name='studentapi'),

]
