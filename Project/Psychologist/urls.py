from django.urls import path
from Psychologist import views
app_name="Psychologist"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('myappointments/',views.myappointments,name='myappointments'),
    path('delappointment/<int:dd>',views.delappointment,name='delappointment'),   
    path('changepassword/',views.changepassword,name='changepassword'),   
    path('consultedappointments/',views.consultedappointments,name='consultedappointments'),
    path('viewpsychiatrist/<int:rp>',views.viewpsychiatrist,name='viewpsychiatrist'),   
    path('referpsychiatrist/<int:rp>',views.referpsychiatrist,name='referpsychiatrist'),
    path('Chatl/<int:cid>/', views.chatuserl, name="Chat-luser"),
    path('loadchatl/', views.loadchatuserl, name="load-lchat"),

    path('feedback/', views.feedback, name="feedback"),
    path('delfeedback/<int:df>/', views.delfeedback, name="delfeedback"),

    path('logout/', views.logout, name="logout"),
]    