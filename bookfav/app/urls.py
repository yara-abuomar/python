from django.urls import path 
from.import views

urlpatterns = [
    path('',views.registrationandlogin ),
    path('reg',views.registration),
    path('login',views.login),
    path('books',views.bookform),
    path('addbook',views.addbook),
    path('logout',views.logout),
    path('books/<id>',views.vieworupdate),
    path('del/<num>/<num1>',views.delete),
    path('update/<id1>/<id2>',views.updatbook), 
    path('addfav/<idbook>',views.addfav),
    path('unfav/<numbook>',views.unfav),
]
