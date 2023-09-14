from django.urls import path
from Rescueteam import views
app_name="Rescueteam"
urlpatterns = [
    path('homepage/',views.homepage,name="homepage"),
    path('myprofile/',views.myprofile,name="myprofile"),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),  
    path('emergencyrequest/',views.emergencyrequest,name='emergencyrequest'),   
    path('aemergencyrequest/',views.aemergencyrequest,name='aemergencyrequest'),   
    path('remergencyrequest/',views.remergencyrequest,name='remergencyrequest'),   
    path('acceptrequest/<int:dd>',views.acceptrequest,name='acceptrequest'),
    path('rejectrequest/<int:dd>',views.rejectrequest,name='rejectrequest'),
    path('informhospital/<int:hh>',views.informhospital,name='informhospital'),
    path('inform/<int:hid>',views.inform,name='inform'),
    path('emergencydetails/',views.emergencydetails,name='emergencydetails'), 
    path('deledetails/<int:did>',views.deledetails,name='deledetails'),


    ## unknown emergency 

    path('unknownemergencyrequest/',views.unknownemergencyrequest,name='unknownemergencyrequest'),   
    path('uaemergencyrequest/',views.uaemergencyrequest,name='uaemergencyrequest'),   
    path('uremergencyrequest/',views.uremergencyrequest,name='uremergencyrequest'),   
    path('acceptunknownrequest/<int:dd>',views.acceptunknownrequest,name='acceptunknownrequest'),
    path('rejectunknownrequest/<int:dd>',views.rejectunknownrequest,name='rejectunknownrequest'),
    path('informhospitalunknown/<int:hh>',views.informhospitalunknown,name='informhospitalunknown'),
    path('informunknown/<int:hid>',views.informunknown,name='informunknown'),
    path('emergencydetailsunknown/',views.emergencydetailsunknown,name='emergencydetailsunknown'),
    path('deleunknowndetails/<int:did>',views.deleunknowndetails,name='deleunknowndetails'),

    path('logout/',views.logout,name='logout'),   
]