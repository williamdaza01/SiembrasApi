from django.urls import path, re_path
from SiembrasApp import views

urlpatterns=[
    path('municipios/', views.municipiosApi),
    path('municipios/([0-9]+)', views.municipiosApi),
    path('veredas/', views.veredasApi),
    path('veredas/([0-9]+)', views.veredasApi),
    path('arboles/', views.arbolesApi),
    path('arboles/([0-9]+)', views.arbolesApi),
    path('contratistas/', views.contratistasApi),
    path('contratistas/([0-9]+)', views.contratistasApi),
    path('siembras/', views.siembrasApi),
    re_path(r'^siembras/([0-9]+)$', views.siembrasApi),
]