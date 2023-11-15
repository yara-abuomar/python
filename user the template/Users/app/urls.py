from django.urls import path
from.import views
urlpatterns = [
    path('', views.form),
    path('route' ,views.handle),
    path('form',views.result),
]