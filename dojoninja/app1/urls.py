from django.urls import path
from.import views
urlpatterns = [
    path('', views.method),
    path('route1',views.method2),
    path('route2',views.method4),
    path('del/<id>',views.method3)
]