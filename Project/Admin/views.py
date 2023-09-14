from django.shortcuts import render,redirect
from Admin.models import * 
from Guest.models import *
from User.models import *
# Create your views here.



def homepage(request):
    membercount=tbl_newhospital.objects.filter().count()
    memberdata=tbl_newhospital.objects.all()
    relativecount=tbl_pyschiatrist.objects.filter().count()
    reldata=tbl_pyschiatrist.objects.all()
    ccount=tbl_pyschologist.objects.filter().count()
    cdata=tbl_pyschologist.objects.all()
    usercount=tbl_userregistration.objects.all().count()
   
    return render(request,"Admin/homepage.html",{'mcount':membercount,'mdata':memberdata,'rcount':relativecount,'rdata':reldata,'ccount':ccount,'cdata':cdata,'usercount':usercount})
    
def district(request):
    if 'aid' in request.session:
        districtdata=tbl_district.objects.all()
        if request.method=="POST":
            tbl_district.objects.create(district_name=request.POST.get('txtname'))
            return render(request,"Admin/District.html",{'district':districtdata})
        else:
            return render(request,"Admin/District.html",{'district':districtdata})
    else:
        return redirect("Guest:login")

def hospitaltype(request):
    if 'aid' in request.session:
        hospitaltypedata=tbl_hospitaltype.objects.all()
        if request.method=="POST":
            tbl_hospitaltype.objects.create(hospitaltype_name=request.POST.get('txtname'))
            return render(request,"Admin/Hospitaltype.html",{'hospitaltype':hospitaltypedata})
        else:
            return render(request,"Admin/Hospitaltype.html",{'hospitaltype':hospitaltypedata})
    else:
        return redirect("Guest:login")

def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("Admin:district")
    

def delhospitaltype(request,dic):
    tbl_hospitaltype.objects.get(id=dic).delete()
    return redirect("Admin:Hospitaltype")
    

def editdistrict(request,eid):
    seldis=tbl_district.objects.get(id=eid)
    districtdata=tbl_district.objects.all()
    if request.method=="POST":
        seldis.district_name=request.POST.get('txtname')
        seldis.save()
        return redirect("Admin:district")
    else:
        return render(request,"Admin/District.html",{'SelDis':seldis,'district':districtdata})
    


def place(request):
    if 'aid' in request.session:
        disdata=tbl_district.objects.all()
        placedata=tbl_place.objects.all()
        if request.method=="POST":
            dist=tbl_district.objects.get(id=request.POST.get('select_dis'))
            tbl_place.objects.create(place_name=request.POST.get('txtname'),district=dist)
            return render(request,"Admin/Place.html",{'place':placedata,'district':disdata})
        else:
            return render(request,"Admin/Place.html",{'place':placedata,'district':disdata})
    else:
        return redirect("Guest:login")


def delplace(request,dip):
    tbl_place.objects.get(id=dip).delete()
    return redirect("Admin:place")
    
def editplace(request,eip):
    selplace=tbl_place.objects.get(id=eip)
    disdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()
    if request.method=='POST':
        dist=request.POST.get('select_dis')
        selplace.districtr=tbl_district.objects.get(id=dist)
        selplace.place_name=request.POST.get('txtname')
        selplace.save()
        return redirect("Admin:place")
    else:
        return render(request,"Admin/Place.html",{'SelPlace':selplace,'place':placedata,'district':disdata})

def newhospitalist(request):
    if 'aid' in request.session:
        newhospitaldata=tbl_newhospital.objects.filter(status=0)
        
        
        return render(request,"Admin/NewHospitalist.html",{'newhospitaldata':newhospitaldata})
    else:
        return redirect("Guest:login")

def acceptedhospitalist(request):
    if 'aid' in request.session:
        
        anewhospitaldata=tbl_newhospital.objects.filter(status=1)
       
        return render(request,"Admin/AcceptedHospitalList.html",{'anewhospitaldata':anewhospitaldata})
    else:
        return redirect("Guest:login")

def rejectedhospitalist(request):
    if 'aid' in request.session:
        
        rnewhospitaldata=tbl_newhospital.objects.filter(status=2)
       
        return render(request,"Admin/RejectedHospitalList.html",{'rnewhospitaldata':rnewhospitaldata})
    else:
        return redirect("Guest:login")


def accepthospital(request,aid):
    if 'aid' in request.session:
        hosdata=tbl_newhospital.objects.get(id=aid)
        hosdata.status=1
        hosdata.save()
        return redirect("Admin:acceptedhospitalist")
    else:
        return redirect("Guest:login")

def rejecthospital(request,rid):
    if 'aid' in request.session:
        hosdata=tbl_newhospital.objects.get(id=rid)
        hosdata.status=2
        hosdata.save()
        return redirect("Admin:rejectedhospitalist")
    else:
        return redirect("Guest:login")

def rescueteam(request):
    if 'aid' in request.session:
        districtdata=tbl_district.objects.all()
        rescuedata=tbl_rescueteam.objects.all()
        if request.method=="POST":
            placedata=tbl_place.objects.get(id=request.POST.get('select_place'))
            tbl_rescueteam.objects.create(name=request.POST.get('txtname'),contact=request.POST.get('txtcontact'),email=request.POST.get('txtemail'),
            address=request.POST.get('txtaddress'),headname=request.POST.get('txtheadname'),headcontact=request.POST.get('txtheadcontact'),logo=request.FILES.get('txtlogo'),password=request.POST.get('txtpass'),place=placedata)
            return redirect("Admin:rescueteam")
        else:
            return render(request,"Admin/NewRescueTeam.html",{'district':districtdata, 'rescuedata':rescuedata})
    else:
        return redirect("Guest:login")

def viewcomplaint(request):
    if 'aid' in request.session:
        complaintdata=tbl_complaint.objects.filter(status=0)
        return render(request,"Admin/ViewComplaint.html",{'complaint':complaintdata})
    else:
        return redirect("Guest:login")

def replycomplaint(request,rc):
    if 'aid' in request.session:
        complaintdata=tbl_complaint.objects.get(id=rc)
        if request.method=="POST":
            complaintdata.reply=request.POST.get('txtreply')
            complaintdata.status=1
            complaintdata.save()
            return redirect("Admin:viewcomplaint")
        else:
            return render(request,"Admin/ReplyCompliant.html")
    else:
        return redirect("Guest:login")


def viewuserfeedback(request):
    if 'aid' in request.session:
        userdata=tbl_userregistration.objects.all()
        data=tbl_feedback.objects.filter(user__in=userdata)
        return render(request,"Admin/ViewUserFeedback.html",{'feedback':data})
    else:
        return redirect("Guest:login")

def viewpsychologistfeedback(request):
    if 'aid' in request.session:
        psychologistdata=tbl_pyschologist.objects.all()
        data=tbl_feedback.objects.filter(psychologist__in=psychologistdata)
        return render(request,"Admin/ViewPsychologistFeedback.html",{'feedback':data})
    else:
        return redirect("Guest:login")

def viewpsychiatristfeedback(request):
    if 'aid' in request.session:
        psychiatristdata=tbl_pyschiatrist.objects.all()
        data=tbl_feedback.objects.filter(psychiatrist__in=psychiatristdata)
        return render(request,"Admin/ViewPsychiatristFeedback.html",{'feedback':data})
    else:
        return redirect("Guest:login")

def viewhospitalfeedback(request):
    if 'aid' in request.session:
        hospitaldata=tbl_newhospital.objects.all()
        data=tbl_feedback.objects.filter(hospital__in=hospitaldata)
        return render(request,"Admin/ViewHospitalFeedback.html",{'feedback':data})
    else:
        return redirect("Guest:login")



def psychiatristreport(request,ar):
    
    if 'aid' in request.session:
        psychiatristdata=tbl_pyschiatrist.objects.get(id=ar)

        if request.method=="POST":
            
            if request.POST.get('txtft')!="" and request.POST.get('txttt')!="":
                data=tbl_psychiatristappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),booking_to_date__lt=request.POST.get('txttt'),token__availability__psychiatrist=psychiatristdata)
                return render(request,"Admin/AppointmentReport.html",{'data':data})
            elif request.POST.get('txtft')!="":
                data=tbl_psychiatristappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),token__availability__psychiatrist=psychiatristdata)
                return render(request,"Admin/AppointmentReport.html",{'data':data})
            else:
                data=tbl_psychiatristappointment.objects.filter(booking_to_date__lt=request.POST.get('txttt'),token__availability__psychiatrist=psychiatristdata)
                return render(request,"Admin/AppointmentReport.html",{'data':data})
        else:
            return render(request,"Admin/AppointmentReport.html")
    else:
        return redirect("Guest:login")
    


def psychologistreport(request,ar):
    
    if 'aid' in request.session:
        psychologistdata=tbl_pyschologist.objects.get(id=ar)

        if request.method=="POST":
            
            if request.POST.get('txtft')!="" and request.POST.get('txttt')!="":
                data1=tbl_psychologistappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),booking_to_date__lt=request.POST.get('txttt'),token__availability__psychologist=psychologistdata)
                return render(request,"Admin/AppointmentReport.html",{'data1':data1})
            elif request.POST.get('txtft')!="":
                data1=tbl_psychologistappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),token__availability__psychologist=psychologistdata)
                return render(request,"Admin/AppointmentReport.html",{'data1':data1})
            else:
                data1=tbl_psychologistappointment.objects.filter(booking_to_date__lt=request.POST.get('txttt'),token__availability__psychologist=psychologistdata)
                return render(request,"Admin/AppointmentReport.html",{'data1':data1})
        else:
            return render(request,"Admin/AppointmentReport.html")
    else:
        return redirect("Guest:login")
    

def psychiatristlist(request):
    if 'aid' in request.session:
        psychiatristdata=tbl_pyschiatrist.objects.all()
        
        return render(request,"Admin/PsychiatristList.html",{'data':psychiatristdata})
    else:
        return redirect("Guest:login")

def psychologistlist(request):
    if 'aid' in request.session:
        
        psychologistdata=tbl_pyschologist.objects.all()
        return render(request,"Admin/PsychologistList.html",{'data1':psychologistdata})
    else:
        return redirect("Guest:login")



def userreport(request):
    if 'aid' in request.session:
        userdata=tbl_userregistration.objects.all()
        if request.method=="POST":
            
            if request.POST.get('txtft')!="" and request.POST.get('txttt')!="":
                data=tbl_userregistration.objects.filter(doj__gt=request.POST.get('txtft'),doj__lt=request.POST.get('txttt'))
                return render(request,"Admin/UserReport.html",{'data':data,'user':userdata})
            elif request.POST.get('txtft')!="":
                data=tbl_userregistration.objects.filter(doj__gt=request.POST.get('txtft'))
                return render(request,"Admin/UserReport.html",{'data':data,'user':userdata})
            else:
                data=tbl_userregistration.objects.filter(doj__lt=request.POST.get('txttt'))
                return render(request,"Admin/UserReport.html",{'data':data,'user':userdata})
        else:
            return render(request,"Admin/UserReport.html")
    else:
        return redirect("Guest:login")


def viewrescueteam(request):
    if 'aid' in request.session:
        rescuedata=tbl_rescueteam.objects.all()
        return render(request,"Admin/ViewRescueteam.html",{'data':rescuedata})
    else:
        return redirect("Guest:login")


def logout(request):
    del request.session["aid"]
    return redirect("Guest:login")


def adminpaymentreport(request):
    totals=[]
    counts=[]
    if request.method=="POST":
            
        hosdata=tbl_newhospital.objects.all()

        if request.POST.get('txtft')!="" and request.POST.get('txttt')!="":
            
            for i in hosdata:
               
                co=0
                datacount=tbl_psychologistappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),booking_to_date__lt=request.POST.get('txttt'),token__availability__psychologist__hospital=i.id).count()
            # data=tbl_psychologistappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),booking_to_date__lt=request.POST.get('txttt'))
                data1count=tbl_psychiatristappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),booking_to_date__lt=request.POST.get('txttt'),token__availability__psychiatrist__hospital=i.id).count()
                co=co+datacount+data1count
                counts.append(co)
                tot=co*50
                totals.append(tot)
            datas=zip(hosdata,counts,totals)
            # data1=tbl_psychiatristappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),booking_to_date__lt=request.POST.get('txttt'))
            # data1total=50*data1count
            # datatotal=50*datacount
            return render(request,"Admin/PaymentReport.html",{'data':datas})
        elif request.POST.get('txtft')!="":
            for i in hosdata:
               
                co=0
            # data=tbl_psychologistappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'))
            # data1=tbl_psychiatristappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),)
                datacount=tbl_psychologistappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),token__availability__psychologist__hospital=i.id).count()
                data1count=tbl_psychiatristappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),token__availability__psychiatrist__hospital=i.id).count()
                co=co+datacount+data1count
                counts.append(co)
                tot=co*50
                totals.append(tot)
            datas=zip(hosdata,counts,totals)
            # data1total=50*data1count
            # datatotal=50*datacount
            return render(request,"Admin/PaymentReport.html",{'data':datas})
        else:
            for i in hosdata:
               
                co=0
            # data=tbl_psychologistappointment.objects.filter(booking_to_date__lt=request.POST.get('txttt'))
            # data1=tbl_psychiatristappointment.objects.filter(booking_to_date__lt=request.POST.get('txttt'),)
                datacount=tbl_psychologistappointment.objects.filter(booking_to_date__lt=request.POST.get('txttt'),token__availability__psychologist__hospital=i.id).count()
                data1count=tbl_psychiatristappointment.objects.filter(booking_to_date__lt=request.POST.get('txttt'),token__availability__psychiatrist__hospital=i.id).count()
                co=co+datacount+data1count
                counts.append(co)
                tot=co*50
                totals.append(tot)
            datas=zip(hosdata,counts,totals)
            return render(request,"Admin/PaymentReport.html",{'data':datas})
    else:
        return render(request,"Admin/PaymentReport.html")


