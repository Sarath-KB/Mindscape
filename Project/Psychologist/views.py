from django.shortcuts import render,redirect
from Admin.models import *
from Hospital.models import *
from User.models import *
from Guest.models import tbl_newhospital,tbl_userregistration
from .models import *
# Create your views here.
def homepage(request):
    if 'plid' in request.session:
        return render(request,"Psychologist/Homepage.html")
    else:
        return redirect("Guest:login")

def myprofile(request):
    if 'plid' in request.session:
        psychologistdata=tbl_pyschologist.objects.get(id=request.session["plid"])
        return render(request,"Psychologist/Myprofile.html",{'data':psychologistdata})
    else:
        return redirect("Guest:login")

def editprofile(request):
    psychologistdata=tbl_pyschologist.objects.get(id=request.session["plid"])
    if request.method=='POST':
        psychologistdata.name=request.POST.get('txtname')
        psychologistdata.contact=request.POST.get('txtcontact')
        psychologistdata.email=request.POST.get('txtemail')
        psychologistdata.address=request.POST.get('txtaddress')
        psychologistdata.save()
        return redirect("Psychologist:myprofile")
    else:
        return render(request,"Psychologist/Editprofile.html",{'data':psychologistdata})

def changepassword(request):
    if request.method=='POST':
        psychologistcount=tbl_pyschologist.objects.filter(id=request.session["plid"],password=request.POST.get('txtcurrent')).count()
        if psychologistcount>0:
            if request.POST.get('txtnew')==request.POST.get('txtconfirm'):
                psychologistdata=tbl_pyschologist.objects.get(id=request.session["plid"])
                psychologistdata.password=request.POST.get('txtnew')
                psychologistdata.save()
                return redirect("Psychologist:homepage")
            else:
                return render(request,"Psychologist/Changepassword.html")
        else:
            return render(request,"Psychologist/Changepassword.html")
    else:        
        return render(request,"Psychologist/Changepassword.html")

def myappointments(request):
    if 'plid' in request.session:
        psychologistdata=tbl_pyschologist.objects.get(id=request.session["plid"])
        data=tbl_psychologistappointment.objects.filter(token__availability__psychologist=psychologistdata,status__gte=1,status__lt=4)
        return render(request,"Psychologist/MyAppointments.html",{'data':data})
    else:
        return redirect("Guest:login")

def delappointment(request,dd):
    data=tbl_psychologistappointment.objects.get(id=dd)
    data.status=4
    data.save()
    return redirect("Psychologist:myappointments")

def consultedappointments(request):
    if 'plid' in request.session:
        psychologistdata=tbl_pyschologist.objects.get(id=request.session["plid"])
        data=tbl_psychologistappointment.objects.filter(token__availability__psychologist=psychologistdata,status__gte=4)
        return render(request,"Psychologist/ConsultedAppointments.html",{'data':data})
    else:
        return redirect("Guest:login")

def referpsychiatrist(request,rp):
    if 'plid' in request.session:
        psychiatristdata=tbl_pyschiatrist.objects.get(id=rp)
        appointmentdata=tbl_psychologistappointment.objects.get(id=request.session["rpid"])
        tbl_refer.objects.create(referappointment=appointmentdata,psychiatrist=psychiatristdata)
        return redirect("Psychologist:myappointments")
    else:
        return redirect("Guest:login")


def viewpsychiatrist(request,rp):
    if 'plid' in request.session:
        request.session["rpid"]=rp
        psychologistdata=tbl_pyschologist.objects.get(id=request.session["plid"])
        hospit=psychologistdata.hospital.id
        hospitaldata=tbl_newhospital.objects.get(id=hospit)
        psychiatristdata=tbl_pyschiatrist.objects.filter(hospital=hospitaldata)
        return render(request,"Psychologist/ViewPsychiatrist.html",{'data':psychiatristdata})
    else:
        return redirect("Guest:login")



def chatuserl(request, cid):
    chatobj = tbl_psychologistappointment.objects.get(id=cid)
    if request.method == "POST":
        cied = request.POST.get("cid")
        # print(cied)
        ciedobj = tbl_userregistration.objects.get(id=cied)
        sobj = tbl_pyschologist.objects.get(id=request.session["plid"])
        content = request.POST.get("msg")
        # print(cied)
        # print(content)
        lchat.objects.create(
            from_lid=sobj, to_user1=ciedobj, content=content, from_user1=None, to_lid=None)
        return render(request, 'Psychologist/Chat2.html', {"chatobj": chatobj})
    else:
        return render(request, 'Psychologist/Chat2.html', {"chatobj": chatobj})


def loadchatuserl(request):
    cid = request.GET.get("cid")
    request.session["cid"] = cid

    cid1 = request.session["cid"]
    # print(cid1)

    # print(cid)
    shopobj = tbl_userregistration.objects.get(id=cid)
    # print(userobj)
    sid = request.session["plid"]
    # print(sid)
    suserobj = tbl_pyschologist.objects.get(id=request.session["plid"])
    # chatobj1 = Chat.objects.filter(Q(to_user=suserobj) | Q(
    #     from_user=suserobj), Q(to_shop=shopobj) | Q(from_shop=shopobj))
    # print(chatobj1)  # send message

    # print(chatobj2)  # recived msg
    chatobj = lchat.objects.raw(
        "select * from User_lchat c inner join Hospital_tbl_pyschologist u on (u.id=c.from_lid_id) or (u.id=c.to_lid_id) WHERE  c.from_user1_id=%s or c.to_user1_id=%s order by c.date", params=[(cid1), (cid1)])

    print(chatobj.query)

    return render(request, 'Psychologist/Load2.html', {"obj": chatobj, "sid": sid, "shop": shopobj, "userobj": suserobj})


def feedback(request):
    if 'plid' in request.session:
        psychologistdata=tbl_pyschologist.objects.get(id=request.session["plid"])
        data=tbl_feedback.objects.filter(psychologist=psychologistdata)
        if request.method=="POST":
            tbl_feedback.objects.create(content=request.POST.get('txtcontent'),psychologist=psychologistdata)
            return render(request,"Psychologist/Feedback.html",{'data':data})
        else:
            return render(request,"Psychologist/Feedback.html",{'data':data})
    else:
        return redirect("Guest:login")

def delfeedback(request,df):
    tbl_feedback.objects.get(id=df).delete()
    return redirect("Psychologist:feedback")

def logout(request):
    del request.session["plid"]
    return redirect("Guest:login")