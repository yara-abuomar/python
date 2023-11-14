from django.urls import path
from.import views
urlpatterns=[
    path('gold',views.gold),
    path('process_money',views.farm),
    path('final',views.final)
]