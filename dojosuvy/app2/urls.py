from django.urls import path
from.import views
urlpatterns = [
    path('form',views.creatform),
    path('route',views.handle),
    path('result',views.result),
]