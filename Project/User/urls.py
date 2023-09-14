from django.urls import path
from User import views
app_name="User"
urlpatterns = [
    path('home/',views.home,name="home"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),   
    path('searchhospital/',views.searchhospital,name='searchhospital'),
    path('sendemergencyrequest/',views.sendemergencyrequest,name='sendemergencyrequest'),
    path('ajaxhospital/',views.ajaxhospital,name='ajaxhospital'),
    path('myrequest/',views.myrequest,name='myrequest'), 
    path('delrequest/<int:dr>',views.delrequest,name='delrequest'), 
    path('viewpsychiatrist/<int:vp>',views.viewpsychiatrist,name='viewpsychiatrist'), 
    path('viewpsychologist/<int:vl>',views.viewpsychologist,name='viewpsychologist'), 
    path('viewpsychiatristavailable/<int:vpa>',views.viewpsychiatristavailable,name='viewpsychiatristavailable'), 
    path('viewpsychologistavailable/<int:vla>',views.viewpsychologistavailable,name='viewpsychologistavailable'), 
    path('booklslot/<int:avid>',views.booklslot,name='booklslot'), 
    path('bookcslot/<int:avlid>',views.bookcslot,name='bookcslot'), 
    path('confirmbooklslot/<int:avid>',views.confirmbooklslot,name='confirmbooklslot'), 
    path('confirmbookcslot/<int:avcid>',views.confirmbookcslot,name='confirmbookcslot'), 
    path('mypsychologist/',views.mypsychologist,name='mypsychologist'),
    path('mypsychiatrist/',views.mypsychiatrist,name='mypsychiatrist'),
    path('delpyschologistbooking/<int:dp>',views.delpyschologistbooking,name='delpyschologistbooking'), 
    path('delpyschiatristbooking/<int:ds>',views.delpyschiatristbooking,name='delpyschiatristbooking'), 

    # paymentstarts
    path('psychologistpayment/<int:did>',views.psychologistpayment,name="psychologistpayment"),
    path('loader/',views.loader,name="loader"),
    path('success/',views.success,name="success"),
    path('psychiatristpayment/<int:dia>',views.psychiatristpayment,name="psychiatristpayment"),
    path('viewprescription/<int:vpc>',views.viewprescription,name="viewprescription"),
    # paymentends

    # psychiatristchat
    path('Chat/<int:cid>/', views.chatuser, name="Chat-user"),
    path('loadchat/', views.loadchatuser, name="load-chat"),
    path('psychiatristqrcode/<int:did>', views.psychiatristqrcode, name="psychiatristqrcode"),
     path('chqr/<int:did>', views.chqr_code, name="chqr_code"),

    # psychologistchat
    path('Chatl/<int:cid>/', views.chatuserl, name="Chat-luser"),
    path('loadchatl/', views.loadchatuserl, name="load-lchat"),
    path('psychologistqrcode/<int:did>', views.psychologistqrcode, name="psychologistqrcode"),
    path('chlqr/<int:did>', views.chlqr_code, name="chlqr_code"),

    
    # complaint
    path('sendcomplaint/', views.sendcomplaint, name="sendcomplaint"),
    path('delcomplaint/<int:dc>/', views.delcomplaint, name="delcomplaint"),
    
    # feedback
    path('feedback/', views.feedback, name="feedback"),
    path('delfeedback/<int:df>/', views.delfeedback, name="delfeedback"),

    #logout
    path('logout/',views.logout,name="logout"),
]    

