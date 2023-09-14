from django.shortcuts import render,redirect
from Guest.models import *
from Admin.models import tbl_district,tbl_place,tbl_feedback,tbl_rescueteam
from User.models import *
from Hospital.models import *
from Psychiatrist.models import *
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import qrcode
# Create your views here.
def home(request):
    if 'uid' in request.session:
        return render(request,"User/Home.html")
    else:
        return redirect("Guest:login")

def myprofile(request):
    if 'uid' in request.session:
        userdata=tbl_userregistration.objects.get(id=request.session["uid"])
        return render(request,"User/Myprofile.html",{'data':userdata})
    else:
        return redirect("Guest:login")

def editprofile(request):
    userdata=tbl_userregistration.objects.get(id=request.session["uid"])
    if request.method=='POST':
        userdata.name=request.POST.get('txtname')
        userdata.contact=request.POST.get('txtcontact')
        userdata.email=request.POST.get('txtemail')
        userdata.address=request.POST.get('txtaddress')
        userdata.save()
        return redirect("User:myprofile")
    else:
        return render(request,"User/Editprofile.html",{'data':userdata})

def changepassword(request):
    if request.method=='POST':
        usercount=tbl_userregistration.objects.filter(id=request.session["uid"],password=request.POST.get('txtcurrent')).count()
        if usercount>0:
            if request.POST.get('txtnew')==request.POST.get('txtconfirm'):
                userdata=tbl_userregistration.objects.get(id=request.session["uid"])
                userdata.password=request.POST.get('txtnew')
                userdata.save()
                return redirect("User:home")
            else:
                return render(request,"User/Changepassword.html")
        else:
            return render(request,"User/Changepassword.html")
    else:        
        return render(request,"User/Changepassword.html")


def searchhospital(request):
    if 'uid' in request.session:
        district=tbl_district.objects.all()
        hospital=tbl_newhospital.objects.filter(status=1)
        return render(request,"User/SearchHospital.html",{'district':district,'hospital':hospital})
    else:
        return redirect("Guest:login")

def sendemergencyrequest(request):
    if 'uid' in request.session:
        userdata=tbl_userregistration.objects.get(id=request.session["uid"])
        rescueteam=tbl_rescueteam.objects.all()
        data=tbl_emergencyrequest.objects.filter(user=userdata)
        if request.method=="POST":
            tbl_emergencyrequest.objects.create(content=request.POST.get('txtcontent'),major=request.POST.get('major'),user=userdata)
            
            return render(request,"User/SendEmergencyRequest.html",{'data':data})
        else:
            return render(request,"User/SendEmergencyRequest.html",{'data':data}) 
    else:
        return redirect("Guest:login")

def ajaxhospital(request):
    if request.GET.get('pid')!="":
        placedata=tbl_place.objects.get(id=request.GET.get('pid'))
        data=tbl_newhospital.objects.filter(place=placedata,status=1)
        return render(request,"User/Ajaxhospital.html",{'hospital':data})
    else:
        districtdata=tbl_district.objects.get(id=request.GET.get('did'))
        data=tbl_newhospital.objects.filter(place__district=districtdata,status=1)
        return render(request,"User/Ajaxhospital.html",{'hospital':data})

def myrequest(request):
    if 'uid' in request.session:
        userdata=tbl_userregistration.objects.get(id=request.session["uid"])
        data=tbl_emergencyrequest.objects.filter(user=userdata)
        return render(request,"User/Myrequest.html",{'userdata':userdata,'data':data})
    else:
        return redirect("Guest:login")

def delrequest(request,dr):
    tbl_emergencyrequest.objects.get(id=dr).delete()
    return redirect("User:myrequest")

def viewpsychiatrist(request,vp):
    if 'uid' in request.session:
        hospitaldata=tbl_newhospital.objects.get(id=vp)
        data=tbl_pyschiatrist.objects.filter(hospital=hospitaldata)
        return render(request,"User/ViewPsychiatrist.html",{'data':data}) 
    else:
        return redirect("Guest:login")

def viewpsychiatristavailable(request,vpa):
    if 'uid' in request.session:
        psychiatristdata=tbl_pyschiatrist.objects.get(id=vpa)
        data=tbl_availablepyschiatrist.objects.filter(psychiatrist=psychiatristdata)
        return render(request,"User/ViewAvailablePsychiatrist.html",{'data':data})
    else:
        return redirect("Guest:login")
def viewpsychologist(request,vl):
    if 'uid' in request.session:
        hospitaldata=tbl_newhospital.objects.get(id=vl)
        data=tbl_pyschologist.objects.filter(hospital=hospitaldata)
        return render(request,"User/ViewPsychologist.html",{'data':data}) 
    else:
        return redirect("Guest:login")
def viewpsychologistavailable(request,vla):
    if 'uid' in request.session:
        psychologistdata=tbl_pyschologist.objects.get(id=vla)
        data=tbl_availablepsychologist.objects.filter(psychologist=psychologistdata)
        return render(request,"User/ViewAvailablePsychologist.html",{'data':data})
    else:
        return redirect("Guest:login")

def booklslot(request,avid):
    if 'uid' in request.session:
        availabledata=tbl_availablepsychologist.objects.get(id=avid)
        datacount=tbl_pyschologisttoken.objects.filter(status=0,availability=availabledata).count()
        if datacount>0:
            data=tbl_pyschologisttoken.objects.filter(status=0,availability=availabledata)[0]
            return render(request,"User/Booklslot.html",{'data':data})
        else:
            return render(request,"User/Booklslot.html")
    else:
        return redirect("Guest:login")

def confirmbooklslot(request,avid):
    if 'uid' in request.session:
        message="Already Booked a Slot Please Try Again Later..."
        data=tbl_pyschologisttoken.objects.get(id=avid)
        userdata=tbl_userregistration.objects.get(id=request.session["uid"])
        bdate=data.availability.date
        ftime=data.availability.from_time
        if request.method=="POST":

            bcount=tbl_psychologistappointment.objects.filter(booking_to_date=bdate,token__availability__from_time=ftime,user=userdata).count()
            if bcount>0:
                return render(request,"User/ConfirmBooklslot.html",{'mess':message})
            else:
                if request.POST.get('offl')=="Yes":
                    tbl_psychologistappointment.objects.create(user=userdata,token=data,booking_to_date=bdate,status=1,offline_status="Yes")
                    data.status=1
                    data.save()
                    return redirect("User:home")
                else:
                    tbl_psychologistappointment.objects.create(user=userdata,token=data,booking_to_date=bdate,status=1,offline_status="No")
                    data.status=1
                    avdata="Doctor Available In "+str(data.availability.date)+"From "+str(data.availability.from_time)+"To"+str(data.availability.to_time)
                    email=userdata.email
                    name=userdata.name
                    send_mail(
            'Respected Sir/Madam '+name,#subject
            ""+avdata,#body
            settings.EMAIL_HOST_USER,
            [email],
        )
                    data.save()
                    return redirect("User:home")
        else:
            return render(request,"User/ConfirmBooklslot.html",{'data':data})
    else:
        return redirect("Guest:login")
def bookcslot(request,avlid):
    if 'uid' in request.session:
        availabledata=tbl_availablepyschiatrist.objects.get(id=avlid)
        datacount=tbl_pyschiatristtoken.objects.filter(status=0,availability=availabledata).count()
        if datacount>0:
            data=tbl_pyschiatristtoken.objects.filter(status=0,availability=availabledata)[0]
            return render(request,"User/Bookcslot.html",{'data':data})
        else:
            return render(request,"User/Bookcslot.html")
    else:
        return redirect("Guest:login")

def confirmbookcslot(request,avcid):
    if 'uid' in request.session:
        message="Already Booked a Slot Please Try Again Later..."
        data=tbl_pyschiatristtoken.objects.get(id=avcid)
        userdata=tbl_userregistration.objects.get(id=request.session["uid"])
        bdate=data.availability.date
        ftime=data.availability.from_time
        if request.method=="POST":
            bcount=tbl_psychiatristappointment.objects.filter(booking_to_date=bdate,token__availability__from_time=ftime,user=userdata).count()
            if bcount>0:
                return render(request,"User/ConfirmBookcslot.html",{'mess':message})
            else:
                if request.POST.get('offl')=="Yes":
                    tbl_psychiatristappointment.objects.create(user=userdata,token=data,booking_to_date=bdate,status=1,offline_status="Yes")
                    data.status=1
                    data.save()
                    return redirect("User:home")
                else:
                    tbl_psychiatristappointment.objects.create(user=userdata,token=data,booking_to_date=bdate,status=1,offline_status="No")
                    data.status=1
                    avdata="Doctor Available In "+str(data.availability.date)+"From "+str(data.availability.from_time)+"To"+str(data.availability.to_time)
                    email=userdata.email
                    name=userdata.name
                    send_mail(
            'Respected Sir/Madam '+name,#subject
            ""+avdata,#body
            settings.EMAIL_HOST_USER,
            [email],
        )
                    data.save()
                    return redirect("User:home")
        else:
            return render(request,"User/ConfirmBookcslot.html",{'data':data})
    else:
        return redirect("Guest:login")

def mypsychologist(request):
    if 'uid' in request.session:
        userdata=tbl_userregistration.objects.get(id=request.session["uid"])
        data=tbl_psychologistappointment.objects.filter(user=userdata)
        return render(request,"User/MyPsychologistBookings.html",{'data':data})
    else:
        return redirect("Guest:login")

def delpyschologistbooking(request,dp):
    tbl_psychologistappointment.objects.get(id=dp).delete()
    return redirect("User:mypsychologist")

def mypsychiatrist(request):
    if 'uid' in request.session:
        userdata=tbl_userregistration.objects.get(id=request.session["uid"])
        data=tbl_psychiatristappointment.objects.filter(user=userdata)
        return render(request,"User/MyPsychiatristBookings.html",{'data':data})
    else:
        return redirect("Guest:login")

def delpyschiatristbooking(request,ds):
    tbl_psychiatristappointment.objects.get(id=ds).delete()
    return redirect("User:mypsychiatrist")

def psychologistpayment(request,did):
    data=tbl_psychologistappointment.objects.get(id=did)
    if request.method=="POST":
        data.status=3
        data.save()
        return redirect("User:loader")
    else:
        return render(request,"User/psychologistPayment.html")

def psychiatristpayment(request,dia):
    data=tbl_psychiatristappointment.objects.get(id=dia)
    if request.method=="POST":
        data.status=3
        data.save()
        return redirect("User:loader")
    else:
        return render(request,"User/psychiatristPayment.html")

def loader(request):
    return render(request,"User/Loader.html")

def success(request):
    return render(request,"User/Success.html")



def viewprescription(request,vpc):
    if 'uid' in request.session:
        udata=tbl_psychiatristappointment.objects.get(id=vpc)
        data=tbl_prescription.objects.get(appointment=udata)
        return render(request,"User/ViewPrescription.html",{'data':data})
    else:
        return redirect("Guest:login")

################################# psychiatristchat

def chatuser(request, cid):
    chatobj = tbl_psychiatristappointment.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = tbl_pyschiatrist.objects.get(id=cied)
        sobj = tbl_userregistration.objects.get(id=request.session["uid"])
        content = request.POST.get("msg")
        # print(cied)
        # print(content)
        cchat.objects.create(
            from_user=sobj, to_cid=ciedobj, content=content, from_cid=None, to_user=None)
        return render(request, 'User/Chat1.html', {"chatobj": chatobj})
    else:
        return render(request, 'User/Chat1.html', {"chatobj": chatobj})


def loadchatuser(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = tbl_pyschiatrist.objects.get(id=cid)
    # print(userobj)
    sid = request.session["uid"]
    # print(sid)
    suserobj = tbl_userregistration.objects.get(id=request.session["uid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = cchat.objects.raw(
        "select * from User_cchat c inner join Guest_tbl_userregistration u on (u.id=c.from_user_id) or (u.id=c.to_user_id) WHERE  c.from_cid_id=%s or c.to_cid_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'User/Load1.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})


################################# psychologistchat


def chatuserl(request, cid):
    chatobj = tbl_psychologistappointment.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = tbl_pyschologist.objects.get(id=cied)
        sobj = tbl_userregistration.objects.get(id=request.session["uid"])
        content = request.POST.get("msg")
        # print(cied)
        # print(content)
        lchat.objects.create(
            from_user1=sobj, to_lid=ciedobj, content=content, from_lid=None, to_user1=None)
        return render(request, 'User/Chat2.html', {"chatobj": chatobj})
    else:
        return render(request, 'User/Chat2.html', {"chatobj": chatobj})


def loadchatuserl(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = tbl_pyschologist.objects.get(id=cid)
    # print(userobj)
    sid = request.session["uid"]
    # print(sid)
    suserobj = tbl_userregistration.objects.get(id=request.session["uid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = lchat.objects.raw(
        "select * from User_lchat c inner join Guest_tbl_userregistration u on (u.id=c.from_user1_id) or (u.id=c.to_user1_id) WHERE  c.from_lid_id=%s or c.to_lid_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'User/Load2.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})


def sendcomplaint(request):
    if 'uid' in request.session:
        userdata=tbl_userregistration.objects.get(id=request.session["uid"])
        data=tbl_complaint.objects.filter(user=userdata)
        if request.method=="POST":
            tbl_complaint.objects.create(content=request.POST.get('txtcontent'),user=userdata)
            return render(request,"User/SendComplaint.html",{'data':data})
        else:
            return render(request,"User/SendComplaint.html",{'data':data})
    else:
        return redirect("Guest:login")

def delcomplaint(request,dc):
    tbl_complaint.objects.get(id=dc).delete()
    return redirect("User:sendcomplaint")

def feedback(request):
    if 'uid' in request.session:
        userdata=tbl_userregistration.objects.get(id=request.session["uid"])
        data=tbl_feedback.objects.filter(user=userdata)
        if request.method=="POST":
            tbl_feedback.objects.create(content=request.POST.get('txtcontent'),user=userdata)
            return render(request,"User/Feedback.html",{'data':data})
        else:
            return render(request,"User/Feedback.html",{'data':data})
    else:
        return redirect("Guest:login")

def delfeedback(request,df):
    tbl_feedback.objects.get(id=df).delete()
    return redirect("User:feedback")

def logout(request):
    del request.session["uid"]
    return redirect("Guest:login")


######################################################


def chqr_code(request,did):
    # Define the data for the QR code
    tokens=tbl_psychiatristappointment.objects.get(id=did)
    tokendata=tokens.token.token_no
    Psychiatristname=tokens.token.availability.psychiatrist.name
    avdate=tokens.token.availability.date
    data = "Token Number :"+str(tokendata)+" Psychiartist Name:"+str(Psychiatristname)+"    Date:"+str(avdate)

    # Generate the QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    image = qr.make_image(fill_color="black", back_color="white")

    # Prepare the response as image/png
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response

def psychiatristqrcode(request,did):
    tokens=tbl_psychiatristappointment.objects.get(id=did)
    return render(request, 'User/PsychiatristQRcode.html',{'did':did,'data':tokens})
    #return render(request, 'User/PsychiatristQRcode.html', {'qr_image': qr_image, 'token': token})


######################################################### 


def chlqr_code(request,did):
    # Define the data for the QR code
    tokens=tbl_psychologistappointment.objects.get(id=did)
    tokendata=tokens.token.token_no
    Psychiatristname=tokens.token.availability.psychologist.name
    avdate=tokens.token.availability.date
    data = "Token Number :"+str(tokendata)+" psychologist Name:"+str(Psychiatristname)+"    Date:"+str(avdate)

    # Generate the QR code
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    image = qr.make_image(fill_color="black", back_color="white")

    # Prepare the response as image/png
    response = HttpResponse(content_type="image/png")
    image.save(response, "PNG")
    return response
    
def psychologistqrcode(request,did):
    tokens=tbl_psychologistappointment.objects.get(id=did)
    return render(request, 'User/PsychologistQRcode.html',{'did':did,'data':tokens})
    

