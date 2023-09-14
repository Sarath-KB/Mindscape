from django.shortcuts import render,redirect
from Admin.models import *
from Hospital.models import *
from User.models import *
from .models import *
from Psychologist.models import tbl_refer
from Guest.models import tbl_userregistration
# Create your views here.
def homepage(request):
    if 'psid' in request.session:
        return render(request,"Psychiatrist/Homepage.html")
    else:
        return redirect("Guest:login")

def myprofile(request):
    if 'psid' in request.session:
        psychiatristdata=tbl_pyschiatrist.objects.get(id=request.session["psid"])
        return render(request,"Psychiatrist/Myprofile.html",{'data':psychiatristdata})
    else:
        return redirect("Guest:login")
def editprofile(request):
    psychiatristdata=tbl_pyschiatrist.objects.get(id=request.session["psid"])
    if request.method=='POST':
        psychiatristdata.name=request.POST.get('txtname')
        psychiatristdata.contact=request.POST.get('txtcontact')
        psychiatristdata.email=request.POST.get('txtemail')
        psychiatristdata.address=request.POST.get('txtaddress')
        psychiatristdata.save()
        return redirect("Psychiatrist:myprofile")
    else:
        return render(request,"Psychiatrist/Editprofile.html",{'data':psychiatristdata})

def changepassword(request):
    if request.method=='POST':
        psychiatristcount=tbl_pyschiatrist.objects.filter(id=request.session["psid"],password=request.POST.get('txtcurrent')).count()
        if psychiatristcount>0:
            if request.POST.get('txtnew')==request.POST.get('txtconfirm'):
                psychiatristdata=tbl_pyschiatrist.objects.get(id=request.session["psid"])
                psychiatristdata.password=request.POST.get('txtnew')
                psychiatristdata.save()
                return redirect("Psychiatrist:homepage")
            else:
                return render(request,"Psychiatrist/Changepassword.html")
        else:
            return render(request,"Psychiatrist/Changepassword.html")
    else:        
        return render(request,"Psychiatrist/Changepassword.html")

def myappointments(request):
    if 'psid' in request.session:
        psychiatristdata=tbl_pyschiatrist.objects.get(id=request.session["psid"])
        data=tbl_psychiatristappointment.objects.filter(token__availability__psychiatrist=psychiatristdata,status__gte=1,status__lt=4)
        return render(request,"Psychiatrist/MyAppointments.html",{'data':data})
    else:
        return redirect("Guest:login")

def delappointment(request,dd):
    data=tbl_psychiatristappointment.objects.get(id=dd)
    data.status=4
    data.save()
    return redirect("Psychiatrist:myappointments")

def consultedappointments(request):
    if 'psid' in request.session:
        psychiatristdata=tbl_pyschiatrist.objects.get(id=request.session["psid"])
        data=tbl_psychiatristappointment.objects.filter(token__availability__psychiatrist=psychiatristdata,status__gte=4)
        return render(request,"Psychiatrist/ConsultedAppointments.html",{'data':data})
    else:
        return redirect("Guest:login")

def prescription(request,pp):
    if 'psid' in request.session:
        appointmentdata=tbl_psychiatristappointment.objects.get(id=pp)
        if request.method=="POST":
            tbl_prescription.objects.create(appointment=appointmentdata,medicine=request.POST.get('txtmedicine'))
            appointmentdata.status=5
            appointmentdata.save()
            return redirect("Psychiatrist:myappointments")
        else:
            return render(request,"Psychiatrist/Prescription.html")
    else:
        return redirect("Guest:login")
def viewreference(request):
    if 'psid' in request.session:
        psychiatristdata=tbl_pyschiatrist.objects.get(id=request.session["psid"])
        data=tbl_refer.objects.filter(psychiatrist=psychiatristdata)
        return render(request,"Psychiatrist/Reference.html",{'data':data})
    else:
        return redirect("Guest:login")


def chatuser(request, cid):
    chatobj = tbl_psychiatristappointment.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = tbl_userregistration.objects.get(id=cied)
        sobj = tbl_pyschiatrist.objects.get(id=request.session["psid"])
        content = request.POST.get("msg")
        # print(cied)
        # print(content)
        cchat.objects.create(
            from_cid=sobj, to_user=ciedobj, content=content, from_user=None, to_cid=None)
        return render(request, 'Psychiatrist/Chat1.html', {"chatobj": chatobj})
    else:
        return render(request, 'Psychiatrist/Chat1.html', {"chatobj": chatobj})


def loadchatuser(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = tbl_userregistration.objects.get(id=cid)
    # print(userobj)
    sid = request.session["psid"]
    # print(sid)
    suserobj = tbl_pyschiatrist.objects.get(id=request.session["psid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = cchat.objects.raw(
        "select * from User_cchat c inner join Hospital_tbl_pyschiatrist u on (u.id=c.from_cid_id) or (u.id=c.to_cid_id) WHERE  c.from_user_id=%s or c.to_user_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'Psychiatrist/Load1.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})


def feedback(request):
    if 'psid' in request.session:
        psychiatristdata=tbl_pyschiatrist.objects.get(id=request.session["psid"])
        data=tbl_feedback.objects.filter(psychiatrist=psychiatristdata)
        if request.method=="POST":
            tbl_feedback.objects.create(content=request.POST.get('txtcontent'),psychiatrist=psychiatristdata)
            return render(request,"Psychiatrist/Feedback.html",{'data':data})
        else:
            return render(request,"Psychiatrist/Feedback.html",{'data':data})
    else:
        return redirect("Guest:login")

def delfeedback(request,df):
    tbl_feedback.objects.get(id=df).delete()
    return redirect("Psychiatrist:feedback")


def patienthistory(request,cid):
    if 'psid' in request.session:
        appointmentdata=tbl_psychiatristappointment.objects.get(id=cid)
        userid=appointmentdata.user.id
        userdata=tbl_userregistration.objects.get(id=userid)
        appcount=tbl_psychiatristappointment.objects.filter(user=userdata).count()
        if appcount>0:
            appdata=tbl_psychiatristappointment.objects.filter(user=userdata)
            j=1
            parray=[0 for i in range(1,appcount+2)]
            for i in appdata:
                parray[j]=i.id
                j=j+1
            pdata=tbl_prescription.objects.filter(appointment__in=parray)
            return render(request,"Psychiatrist/PatientHistory.html",{'data':pdata})
        else:
            return render(request,"Psychiatrist/PatientHistory.html",{'Mess':1})
    else:
        return redirect("Guest:login")

       
def logout(request):
    del request.session["psid"]
    return redirect("Guest:login")