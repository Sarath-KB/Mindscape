from django.urls import path
from Psychiatrist import views
app_name="Psychiatrist"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('myappointments/',views.myappointments,name='myappointments'),
    path('consultedappointments/',views.consultedappointments,name='consultedappointments'),
    path('changepassword/',views.changepassword,name='changepassword'),   
    path('delappointment/<int:dd>',views.delappointment,name='delappointment'),   
    path('prescription/<int:pp>',views.prescription,name='prescription'),   

    path('viewreferences/',views.viewreference,name='viewreference'),

    path('Chat/<int:cid>/', views.chatuser, name="Chat-user"),
    path('loadchat/', views.loadchatuser, name="load-chat"),

    path('patienthistory/<int:cid>/', views.patienthistory, name="patienthistory"),

    path('feedback/', views.feedback, name="feedback"),
    path('delfeedback/<int:df>/', views.delfeedback, name="delfeedback"),

    path('logout/', views.logout, name="logout"),
]    