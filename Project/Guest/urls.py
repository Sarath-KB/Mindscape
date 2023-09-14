from django.urls import path
from Guest import views
app_name="Guest"
urlpatterns = [
    path('userregistration/',views.userregistration,name="userregistration"),
    path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
    path('newhospital/',views.newhospital,name='newhospital'),
    path('login/',views.login,name='login'),   
    path('fpass/', views.ForgetPassword,name="forpass"),
    path('otpver/', views.OtpVerification,name="verification"),
    path('create/', views.CreateNewPass,name="create"),
    path('emergency/', views.emergency,name="emergency"),
    path('', views.home,name="home"),
]