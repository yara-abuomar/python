from django.urls import path
from.import views
urlpatterns=[
    path('form',views.guees),
    path('route',views.handle),
    path('low',views.low),
    path('high',views.high),
    path('correct',views.correct),
    
  
  
]