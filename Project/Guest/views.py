from django.shortcuts import render,redirect
from Admin.models import * 
from Guest.models import *
from Hospital.models import *
from django.core.mail import send_mail
from django.conf import settings
import random
def userregistration(request):
    districtdata=tbl_district.objects.all()
    userdata=tbl_userregistration.objects.all()
    if request.method=="POST":
        placedata=tbl_place.objects.get(id=request.POST.get('select_place'))
        tbl_userregistration.objects.create(name=request.POST.get('txtname'),contact=request.POST.get('txtcontact'),email=request.POST.get('txtemail'),
        address=request.POST.get('txtaddress'),photo=request.FILES.get('txtfile'),password=request.POST.get('txtpass'),place=placedata)
        
        return redirect("Guest:userregistration")
    else:
        return render(request,"Guest/UserRegistration.html",{'district':districtdata, 'userdata':userdata})
def ajaxplace(request):
    dist=tbl_district.objects.get(id=request.GET.get('did'))
    placedata=tbl_place.objects.filter(district=dist)
    return render(request,"Guest/Ajaxplace.html",{'place':placedata})

def newhospital(request):
    districtdata=tbl_district.objects.all()
    hospitaltypedata=tbl_hospitaltype.objects.all()
    if request.method=="POST":
        placedata=tbl_place.objects.get(id=request.POST.get('select_place'))
        hostype=tbl_hospitaltype.objects.get(id=request.POST.get('select_htype'))
        tbl_newhospital.objects.create(name=request.POST.get('txtname'),contact=request.POST.get('txtcontact'),email=request.POST.get('txtemail'),
        address=request.POST.get('txtaddress'),logo=request.FILES.get('txtlogo'),proof=request.FILES.get('txtproof'),password=request.POST.get('txtpass'),place=placedata,hospitaltype=hostype)
        
        return redirect("Guest:newhospital")
    else:
        return render(request,"Guest/newhospital.html",{'district':districtdata, 'hospitaltype':hospitaltypedata})

def login(request):
    message="Invalid User"
    if request.method=="POST":
        admincount=tbl_adminlogin.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpass')).count()
        usercount=tbl_userregistration.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpass')).count()
        rescuecount=tbl_rescueteam.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpass')).count()
        hospitalcount=tbl_newhospital.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpass'),status=1).count()
        psychologistcount=tbl_pyschologist.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpass')).count()
        psychiatristcount=tbl_pyschiatrist.objects.filter(email=request.POST.get('txtemail'),password=request.POST.get('txtpass')).count()
        if admincount>0:
            admindata=tbl_adminlogin.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpass'))
            request.session["aid"]=admindata.id
            return redirect("Admin:homepage")
        elif usercount>0:
            userdata=tbl_userregistration.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpass'))
            request.session["uid"]=userdata.id
            return redirect("User:home")
        elif hospitalcount>0:
            hospitaldata=tbl_newhospital.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpass'),status=1)
            request.session["hid"]=hospitaldata.id
            return redirect("Hospital:home")
        elif rescuecount>0:
            rescuedata=tbl_rescueteam.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpass'))
            request.session["rid"]=rescuedata.id
            request.session["pid"]=rescuedata.place.id
            return redirect("Rescueteam:homepage")
        elif psychologistcount>0:
            psychologistdata=tbl_pyschologist.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpass'))
            request.session["plid"]=psychologistdata.id
            return redirect("Psychologist:homepage")
        elif psychiatristcount>0:
            psychiatristdata=tbl_pyschiatrist.objects.get(email=request.POST.get('txtemail'),password=request.POST.get('txtpass'))
            request.session["psid"]=psychiatristdata.id
            return redirect("Psychiatrist:homepage")
        else:    
            return render(request,"Guest/Login.html",{'message':message})
    else:    
        return render(request,"Guest/Login.html")


def ForgetPassword(request):
    
    if request.method=="POST":
        otp=random.randint(10000, 999999)
        request.session["otp"]=otp
        request.session["femail"]=request.POST.get('txtemail')
        send_mail(
            'Respected Sir/Madam ',#subject
            "\rYour OTP for Reset Password Is"+str(otp),#body
            settings.EMAIL_HOST_USER,
            [request.POST.get('txtemail')],
        )
        return redirect("Guest:verification")
    else:
        return render(request,"Guest/ForgetPassword.html")

def OtpVerification(request):
    if request.method=="POST":
        otp=int(request.session["otp"])
        if int(request.POST.get('txtotp'))==otp:
            return redirect("Guest:create")
    return render(request,"Guest/OTPVerification.html")

def CreateNewPass(request):
    if request.method=="POST":
        if request.POST.get('txtpassword2')==request.POST.get('txtpassword3'):
            usercount=tbl_userregistration.objects.filter(email=request.session["femail"]).count()
            psychiatristcount=tbl_pyschiatrist.objects.filter(email=request.session["femail"]).count()
            psychologistcount=tbl_pyschologist.objects.filter(email=request.session["femail"]).count()
            hospitalcount=tbl_newhospital.objects.filter(email=request.session["femail"]).count()
            if usercount>0:
                user=tbl_userregistration.objects.get(email=request.session["femail"])
                user.password=request.POST.get('txtpassword2')
                user.save()
                return redirect("Guest:login")

            elif psychiatristcount>0:
                doc=tbl_pyschiatrist.objects.get(email=request.session["femail"])
                doc.password=request.POST.get('txtpassword2')
                doc.save()
                return redirect("Guest:login")

            elif psychologistcount>0:
                con=tbl_pyschologist.objects.get(email=request.session["femail"])
                con.password=request.POST.get('txtpassword2')
                con.save()
                return redirect("Guest:login")

            else:
                hos=tbl_new.objects.get(email=request.session["femail"])
                hos.tbl_newhospital=request.POST.get('txtpassword2')
                hos.save()
                return redirect("Guest:login")
    else:       
        return render(request,"Guest/CreateNewPassword.html")

def home(request):
    return render(request,"Guest/Home.html")


def emergency(request):
    districtdata=tbl_district.objects.all() 
    if request.method=="POST":
        placedata=tbl_place.objects.get(id=request.POST.get('select_place'))
        tbl_unknownemergency.objects.create(content=request.POST.get('txtcontent'), major=request.POST.get('major'),place=placedata)
        return redirect("Guest:emergency")
    else:
        return render(request,"Guest/Emergency.html",{'district':districtdata})