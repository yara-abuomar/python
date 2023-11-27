from django.urls import path
from.import views
urlpatterns = [
    path('',views.addform ),
    path('checkout/<id>',views.add),
    path('route',views.des),
    path('show/<num>',views.one),
]
