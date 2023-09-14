from django.urls import path
from Hospital import views
app_name="Hospital"
urlpatterns = [

#Hospital Section

###################################################################################
    path('home/',views.home,name="home"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),   
   
   #HospitalSection End
###################################################################################    
   
   
  
    
    #Psychologist Start 


    path('psychologistreg/',views.psychologistreg,name='psychologistreg'),
    path('delpyschologist/<int:ds>',views.delpyschologist,name='delpyschologist'),
    path('pyschologistavilable/<int:lid>',views.pyschologistavilable,name='pyschologistavilable'),
    path('setPsychologisttoken/<int:avlid>',views.setPsychologisttoken,name='setPsychologisttoken'),
    path('delpyschologistavailability/<int:did>',views.delpyschologistavailability,name='delpyschologistavailability'), 
    path('delpyschiatristavailability/<int:dd>',views.delpyschiatristavailability,name='delpyschiatristavailability'), 
    # path('newpsychologistappointment/',views.newpsychologistappointment,name="newpsychologistappointment"),
    path('apsychologistappointment/',views.apsychologistappointment,name="apsychologistappointment"),
    # path('rpsychologistappointment/',views.rpsychologistappointment,name="rpsychologistappointment"),
    # path('acceptpsychologist/<int:dd>',views.acceptpsychologist,name='acceptpsychologist'),
    # path('rejectpsychologist/<int:dd>',views.rejectpsychologist,name='rejectpsychologist'),
    
    
    #Psychologist End


############################################################################################################################

    #Psychiatrist Start


    path('psychiatristreg/',views.psychiatristreg,name='psychiatristreg'),  
    # path('newpsychiatristappointment/',views.newpsychiatristappointment,name="newpsychiatristappointment"),
    path('apsychiatristappointment/',views.apsychiatristappointment,name="apsychiatristappointment"),
    # path('rpsychiatristappointment/',views.rpsychiatristappointment,name="rpsychiatristappointment"),
    path('delpyschiatrist/<int:dp>',views.delpyschiatrist,name='delpyschiatrist'),
    path('delpyschiatristavailability/<int:did>',views.delpyschiatristavailability,name='delpyschiatristavailability'), 
    path('pyschiatristavilable/<int:cid>',views.pyschiatristavilable,name='pyschiatristavilable'),
    path('setPsychiatristtoken/<int:avid>',views.setPsychiatristtoken,name='setPsychiatristtoken'),
    # path('acceptpsychiatrist/<int:dd>',views.acceptpsychiatrist,name='acceptpsychiatrist'),
    # path('rejectpsychiatrist/<int:dd>',views.rejectpsychiatrist,name='rejectpsychiatrist'),

    #Psychiatrist End


#############################################################################################################################
    path('emergencydetails/', views.emergencydetails, name="emergencydetails"),

    path('emergencydetailsunknown/', views.emergencydetailsunknown, name="emergencydetailsunknown"),

    path('deledetails/<int:did>',views.deledetails,name='deledetails'),
    path('deleunknowndetails/<int:did>',views.deleunknowndetails,name='deleunknowndetails'),

    path('feedback/', views.feedback, name="feedback"),
    path('delfeedback/<int:df>/', views.delfeedback, name="delfeedback"),

    path('logout/',views.logout,name="logout"),

#############appointment report

    
    path('psychiatristreport/<int:ar>',views.psychiatristreport,name='psychiatristreport'),
    path('psychologistreport/<int:ar>',views.psychologistreport,name='psychologistreport'),

    path('doctorsreport/',views.doctorsreport,name="doctorsreport"),

    path('paymentreport/',views.paymentreport,name="paymentreport"),

    path('patienthistory/',views.patienthistory,name="patienthistory"),
    



]


    
