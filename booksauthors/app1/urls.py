from django.urls import path 
from.import views
urlpatterns = [
    path('',views.method),
    path('route1',views.method1),
    path('author',views.method2),
    path('route2',views.method3),
    path('books/<int:id>',views.method4),
    path('authors/<int:id1>',views.method5),
    path('auth/<int:num>',views.method6),
    path('book/<int:num1>',views.method7)
]