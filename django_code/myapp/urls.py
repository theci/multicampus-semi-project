"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    
    path('', views.gangnam),
    path('gangnam/', views.gangnam),
    
    path('gangdong/', views.gangdong),
    path('gangbuk/', views.gangbuk),
    path('gangseo/', views.gangseo),
    path('gwanak/', views.gwanak),

    path('gwangjin/', views.gwangjin),
    path('guro/', views.guro),
    path('geumcheon/', views.geumcheon),
    path('nowon/', views.nowon),
    path('dobong/', views.dobong),

    path('dongdaemun/', views.dongdaemun),
    path('dongjak/', views.dongjak),
    path('mapo/', views.mapo),
    path('seodaemun/', views.seodaemun),
    path('seocho/', views.seocho),

    path('seongdong/', views.seongdong),
    path('seongbuk/', views.seongbuk),
    path('songpa/', views.songpa),
    path('yangcheon/', views.yangcheon),
    path('yeongdeungpo/', views.yeongdeungpo),

    path('yongsan/', views.yongsan),
    path('eunpyeong/', views.eunpyeong),
    path('jongno/', views.jongno),
    path('junggu/', views.junggu),
    path('jungnang/', views.jungnang),
    ]
