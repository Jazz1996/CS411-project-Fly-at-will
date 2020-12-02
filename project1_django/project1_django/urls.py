"""project1_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from FlyAtWill import views
from FlyAtWill.views import FlyAtWill
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fly-at-will/', views.FlyAtWillPage),
    path('search-results', views.SearchFlight),
    path('recommend/', views.RecommendPage),
    path('recommend-results', views.RecommendFlight),
    path('transfer/', views.TransferPage),
    path('transfer-results', views.Transfer),
    path('search/', views.search),
    path('search/result', views.search_result),
    path('manage/', views.manage),
    path('manage/delete/', views.delete),
    path('manage/insert/', views.insert),
    path('manage/update/', views.update)
]
urlpatterns += staticfiles_urlpatterns()
