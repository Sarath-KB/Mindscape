from django.urls import path
from Admin import views

app_name="Admin"
urlpatterns = [
    path('district/',views.district,name="district"),
    path('hospitaltype/',views.hospitaltype,name='hospitaltype'),
    path('deldistrict/<int:did>',views.deldistrict,name='deldistrict'),
    path('delhospitaltype/<int:dic>',views.delhospitaltype,name='delhospitaltype'),   
    path('editdistrict/<int:eid>',views.editdistrict,name='editdistrict'),
    path('place/',views.place,name='place'),
    path('delplace/<int:dip>',views.delplace,name='delplace'),
    path('editplace/<int:eip>',views.editplace,name='editplace'),
    path('newhospitalist/',views.newhospitalist,name='newhospitalist'),
    path('acceptedhospitalist/',views.acceptedhospitalist,name='acceptedhospitalist'),
    path('rejectedhospitalist/',views.rejectedhospitalist,name='rejectedhospitalist'),
    path('accepthospital/<int:aid>',views.accepthospital,name='accepthospital'),
    path('rejecthospital/<int:rid>',views.rejecthospital,name='rejecthospital'),

    path('homepage/',views.homepage,name="homepage"),
    path('rescueteam/',views.rescueteam,name="rescueteam"),
    path('viewrescueteam/',views.viewrescueteam,name="viewrescueteam"),

    path('userreport/',views.userreport,name="userreport"),
    # path('viewuser/',views.viewuser,name="viewuser"),

    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
    path('replycomplaint/<int:rc>',views.replycomplaint,name='replycomplaint'),
    
    path('viewuserfeedback/',views.viewuserfeedback,name="viewuserfeedback"),
    path('viewpsychologistfeedback/',views.viewpsychologistfeedback,name="viewpsychologistfeedback"),
    path('viewpsychiatristfeedback/',views.viewpsychiatristfeedback,name="viewpsychiatristfeedback"),
    path('viewhospitalfeedback/',views.viewhospitalfeedback,name="viewhospitalfeedback"),

    
    path('psychiatristlist/',views.psychiatristlist,name="psychiatristlist"),
    path('psychologistlist/',views.psychologistlist,name="psychologistlist"),

    path('psychiatristreport/<int:ar>',views.psychiatristreport,name='psychiatristreport'),
    path('psychologistreport/<int:ar>',views.psychologistreport,name='psychologistreport'),

    path('logout/',views.logout,name="logout"),

    path('adminpaymentreport/',views.adminpaymentreport,name="adminpaymentreport"),
    


]