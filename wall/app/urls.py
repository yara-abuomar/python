from django.urls import path
from.import views
urlpatterns = [
    path('',views.form ),
    path('regester',views.registrationuser),
    path('login',views.log),
    path('suc',views.succses),
    path('logout',views.logout),
    path('addmsg',views.addmsg),
    path('com/<num>',views.addcomment)  ,
    path('del/<num1>',views.delete),
]