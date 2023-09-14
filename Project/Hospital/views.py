from django.shortcuts import render,redirect
from Guest.models import tbl_newhospital
from Admin.models import *
from Hospital.models import *
from User.models import *
from Rescueteam.models import *
# Create your views here.
def home(request):
    if 'hid' in request.session:
        return render(request,"Hospital/Home.html")
    else:
        return redirect("Guest:login")
    
def myprofile(request):
    if 'hid' in request.session:
        userdata=tbl_newhospital.objects.get(id=request.session["hid"])
        return render(request,"Hospital/Myprofile.html",{'data':userdata})
    else:
        return redirect("Guest:login")
    
def editprofile(request):
    userdata=tbl_newhospital.objects.get(id=request.session["hid"])
    if request.method=='POST':
        userdata.name=request.POST.get('txtname')
        userdata.contact=request.POST.get('txtcontact')
        userdata.email=request.POST.get('txtemail')
        userdata.address=request.POST.get('txtaddress')
        userdata.save()
        return redirect("Hospital:myprofile")
    else:
        return render(request,"Hospital/Editprofile.html",{'data':userdata})


def changepassword(request):
    if request.method=='POST':
        hospitalcount=tbl_newhospital.objects.filter(id=request.session["hid"],password=request.POST.get('txtcurrent')).count()
        if hospitalcount>0:
            if request.POST.get('txtnew')==request.POST.get('txtconfirm'):
                hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
                hospitaldata.password=request.POST.get('txtnew')
                hospitaldata.save()
                return redirect("Hospital:home")
            else:
                return render(request,"Hospital/Changepassword.html")
        else:
            return render(request,"Hospital/Changepassword.html")
    else:        
        return render(request,"Hospital/Changepassword.html")


def psychiatristreg(request):
    if 'hid' in request.session:
        hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
        districtdata=tbl_district.objects.all()
        userdata=tbl_pyschiatrist.objects.filter(hospital=hospitaldata)
        if request.method=="POST":
            placedata=tbl_place.objects.get(id=request.POST.get('select_place'))
            tbl_pyschiatrist.objects.create(name=request.POST.get('txtname'),contact=request.POST.get('txtcontact'),email=request.POST.get('txtemail'),gender=request.POST.get('gender'),
            address=request.POST.get('txtaddress'),photo=request.FILES.get('txtfile'),password=request.POST.get('txtpass'),place=placedata,hospital=hospitaldata)
        
            return redirect("Hospital:psychiatristreg")
        else:
            return render(request,"Hospital/Psychiatristreg.html",{'district':districtdata, 'userdata':userdata})
    else:
        return redirect("Guest:login")
    
def psychologistreg(request):
    if 'hid' in request.session:
        hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
        districtdata=tbl_district.objects.all()
        userdata=tbl_pyschologist.objects.filter(hospital=hospitaldata)
        if request.method=="POST":
            placedata=tbl_place.objects.get(id=request.POST.get('select_place'))
            tbl_pyschologist.objects.create(name=request.POST.get('txtname'),contact=request.POST.get('txtcontact'),email=request.POST.get('txtemail'),gender=request.POST.get('gender'),
            address=request.POST.get('txtaddress'),photo=request.FILES.get('txtfile'),password=request.POST.get('txtpass'),place=placedata,hospital=hospitaldata)
        
            return redirect("Hospital:psychologistreg")
        else:
            return render(request,"Hospital/Psychologistreg.html",{'district':districtdata, 'userdata':userdata})
    else:
        return redirect("Guest:login")

def delpyschiatrist(request,dp):
    tbl_pyschiatrist.objects.get(id=dp).delete()
    return redirect("Hospital:psychiatristreg")

def pyschiatristavilable(request,cid):
    if 'hid' in request.session:
        chatristdata=tbl_pyschiatrist.objects.get(id=cid)
        data=tbl_availablepyschiatrist.objects.filter(psychiatrist=chatristdata)
        if request.method=="POST":
            tbl_availablepyschiatrist.objects.create(psychiatrist=chatristdata,date=request.POST.get('txtdate'),from_time=request.POST.get('txtft'),to_time=request.POST.get('txttt'))
            return redirect("Hospital:psychiatristreg")
        else:
            return render(request,"Hospital/PsychiatristAvailable.html",{'data':data})
    else:
        return redirect("Guest:login")

def delpyschiatristavailability(request,dd):
    tbl_availablepyschiatrist.objects.get(id=dd).delete()
    return redirect("Hospital:psychiatristreg")

def setPsychiatristtoken(request,avid):
    if 'hid' in request.session:
        availabledata=tbl_availablepyschiatrist.objects.get(id=avid)
        if request.method=="POST":
            tokencount=int(request.POST.get('tokencount'))
            for i in range(1,tokencount+1):
                tbl_pyschiatristtoken.objects.create(availability=availabledata,token_no=i)
            return redirect("Hospital:psychiatristreg")
        else:
            return render(request,"Hospital/PsychiatristToken.html")
    else:
        return redirect("Guest:login")

def delpyschologist(request,ds):
    tbl_pyschologist.objects.get(id=ds).delete()
    return redirect("Hospital:psychologistreg")

def pyschologistavilable(request,lid):
    if 'hid' in request.session:
        psychologistdata=tbl_pyschologist.objects.get(id=lid)
        data=tbl_availablepsychologist.objects.filter(psychologist=psychologistdata)
        if request.method=="POST":
            tbl_availablepsychologist.objects.create(psychologist=psychologistdata,date=request.POST.get('txtdate'),from_time=request.POST.get('txtft'),to_time=request.POST.get('txttt'))
            return redirect("Hospital:psychologistreg")
        else:
            return render(request,"Hospital/PsychologistAvailable.html",{'data':data})
    else:
        return redirect("Guest:login")


def delpyschologistavailability(request,did):
    tbl_availablepsychologist.objects.get(id=did).delete()
    return redirect("Hospital:psychologistreg")

def setPsychologisttoken(request,avlid):
    if 'hid' in request.session:
        availabledata=tbl_availablepsychologist.objects.get(id=avlid)
        if request.method=="POST":
            tokencount=int(request.POST.get('tokencount'))
            for i in range(1,tokencount+1):
                tbl_pyschologisttoken.objects.create(availability=availabledata,token_no=i)
            return redirect("Hospital:psychologistreg")
        else:
            return render(request,"Hospital/PsychologistToken.html")
    else:
        return redirect("Guest:login")


def newpsychologistappointment(request):
    if 'hid' in request.session:
        hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
        data=tbl_psychologistappointment.objects.filter(token__availability__psychologist__hospital=hospitaldata,status=0)
        return render(request,"Hospital/NewPsychologistAppointment.html",{'data':data})
    else:
        return redirect("Guest:login")


def apsychologistappointment(request):
    if 'hid' in request.session:    
        hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
        data=tbl_psychologistappointment.objects.filter(token__availability__psychologist__hospital=hospitaldata,status__gte=1)
        return render(request,"Hospital/AcceptPsychologistAppointment.html",{'data':data})
    else:
        return redirect("Guest:login")

def rpsychologistappointment(request):
    if 'hid' in request.session:  
        hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
        data=tbl_psychologistappointment.objects.filter(token__availability__psychologist__hospital=hospitaldata,status=2)
        return render(request,"Hospital/RejectPsychologistAppointment.html",{'data':data})
    else:
        return redirect("Guest:login")


def newpsychiatristappointment(request):
    if 'hid' in request.session:
        hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
        data=tbl_psychiatristappointment.objects.filter(token__availability__psychiatrist__hospital=hospitaldata,status=0)
        return render(request,"Hospital/NewPsychiatristAppointment.html",{'data':data})
    else:
        return redirect("Guest:login")

def apsychiatristappointment(request):
    if 'hid' in request.session:
        hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
        data=tbl_psychiatristappointment.objects.filter(token__availability__psychiatrist__hospital=hospitaldata,status__gte=1)
        return render(request,"Hospital/AcceptPsychiatristAppointment.html",{'data':data})
    else:
        return redirect("Guest:login")


def rpsychiatristappointment(request):
    if 'hid' in request.session:
        hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
        data=tbl_psychiatristappointment.objects.filter(token__availability__psychiatrist__hospital=hospitaldata,status=2)
        return render(request,"Hospital/RejectPsychiatristAppointment.html",{'data':data})
    else:
        return redirect("Guest:login")

def acceptpsychiatrist(request,dd):
    if 'hid' in request.session:
        data=tbl_psychiatristappointment.objects.get(id=dd)
        data.status=1
        data.save()
        return redirect("Hospital:newpsychiatristappointment")
    else:
        return redirect("Guest:login")

def rejectpsychiatrist(request,dd):
    if 'hid' in request.session:
        data=tbl_psychiatristappointment.objects.get(id=dd)
        data.status=2
        data.save()
        return redirect("Hospital:newpsychiatristappointment")
    else:
        return redirect("Guest:login")


def acceptpsychologist(request,dd):
    if 'hid' in request.session:
        data=tbl_psychologistappointment.objects.get(id=dd)
        data.status=1
        data.save()
        return redirect("Hospital:newpsychologistappointment")
    else:
        return redirect("Guest:login")

def rejectpsychologist(request,dd):
    if 'hid' in request.session:
        data=tbl_psychologistappointment.objects.get(id=dd)
        data.status=2
        data.save()
        return redirect("Hospital:newpsychologistappointment")
    else:
        return redirect("Guest:login")

def feedback(request):
    if 'hid' in request.session:
        hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
        data=tbl_feedback.objects.filter(hospital=hospitaldata)
        if request.method=="POST":
            tbl_feedback.objects.create(content=request.POST.get('txtcontent'),hospital=hospitaldata)
            return render(request,"Hospital/Feedback.html",{'data':data})
        else:
            return render(request,"Hospital/Feedback.html",{'data':data})
    else:
        return redirect("Guest:login")

def delfeedback(request,df):
    tbl_feedback.objects.get(id=df).delete()
    return redirect("Hospital:feedback")


def emergencydetails(request):
    if 'hid' in request.session:
        rescuedata=tbl_newhospital.objects.get(id=request.session["hid"])
        data=tbl_rescueinfo.objects.filter(hospital=rescuedata)
        return render(request,"Hospital/EmergencyDetails.html",{'data':data})
    else:
        return redirect("Guest:login") 


def emergencydetailsunknown(request):
    if 'hid' in request.session:
        rescuedata=tbl_newhospital.objects.get(id=request.session["hid"])
        data=tbl_rescueinfounknown.objects.filter(hospital=rescuedata)
        return render(request,"Hospital/UnknownEmergencyDetails.html",{'data':data})
    else:
        return redirect("Guest:login") 


def deledetails(request,did):
    tbl_emergencyrequest.objects.get(id=did).delete()
    return redirect("Hospital:emergencydetails")


def deleunknowndetails(request,did):
    tbl_unknownemergency.objects.get(id=did).delete()
    return redirect("hospital:emergencydetailsunknown")


def logout(request):
    del request.session["hid"]
    return redirect("Guest:login")

######## appointment reports ###########



def psychiatristreport(request,ar):
    
    if 'hid' in request.session:
        psychiatristdata=tbl_pyschiatrist.objects.get(id=ar)

        if request.method=="POST":
            
            if request.POST.get('txtft')!="" and request.POST.get('txttt')!="":
                data=tbl_psychiatristappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),booking_to_date__lt=request.POST.get('txttt'),token__availability__psychiatrist=psychiatristdata)
                return render(request,"Hospital/AppointmentReport.html",{'data':data})
            elif request.POST.get('txtft')!="":
                data=tbl_psychiatristappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),token__availability__psychiatrist=psychiatristdata)
                return render(request,"Hospital/AppointmentReport.html",{'data':data})
            else:
                data=tbl_psychiatristappointment.objects.filter(booking_to_date__lt=request.POST.get('txttt'),token__availability__psychiatrist=psychiatristdata)
                return render(request,"Hospital/AppointmentReport.html",{'data':data})
        else:
            return render(request,"Hospital/AppointmentReport.html")
    else:
        return redirect("Guest:login")
    


def psychologistreport(request,ar):
    
    if 'hid' in request.session:

        psychologistdata=tbl_pyschologist.objects.get(id=ar)

        if request.method=="POST":
            
            if request.POST.get('txtft')!="" and request.POST.get('txttt')!="":
                data1=tbl_psychologistappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),booking_to_date__lt=request.POST.get('txttt'),token__availability__psychologist=psychologistdata)
                return render(request,"Hospital/AppointmentReport.html",{'data1':data1})
            elif request.POST.get('txtft')!="":
                data1=tbl_psychologistappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),token__availability__psychologist=psychologistdata)
                return render(request,"Hospital/AppointmentReport.html",{'data1':data1})
            else:
                data1=tbl_psychologistappointment.objects.filter(booking_to_date__lt=request.POST.get('txttt'),token__availability__psychologist=psychologistdata)
                return render(request,"Hospital/AppointmentReport.html",{'data1':data1})
        else:
            return render(request,"Hospital/AppointmentReport.html")
    else:
        return redirect("Guest:login")

########### Main reports #######################################################################


def doctorsreport(request):
    if 'hid' in request.session:
        
        hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
        if request.method=="POST":
            
            if request.POST.get('txtft')!="" and request.POST.get('txttt')!="":
                data=tbl_psychologistappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),booking_to_date__lt=request.POST.get('txttt'),token__availability__psychologist__hospital=hospitaldata)
                data1=tbl_psychiatristappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),booking_to_date__lt=request.POST.get('txttt'),token__availability__psychiatrist__hospital=hospitaldata)
                return render(request,"Hospital/DoctorsReport.html",{'data':data,'data1':data1})
            elif request.POST.get('txtft')!="":
                data=tbl_psychologistappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),token__availability__psychologist__hospital=hospitaldata)
                data1=tbl_psychiatristappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),token__availability__psychiatrist__hospital=hospitaldata)
                return render(request,"Hospital/DoctorsReport.html",{'data':data,'data1':data1})
            else:
                data=tbl_psychologistappointment.objects.filter(booking_to_date__lt=request.POST.get('txttt'),token__availability__psychologist__hospital=hospitaldata)
                data1=tbl_psychiatristappointment.objects.filter(booking_to_date__lt=request.POST.get('txttt'),token__availability__psychiatrist__hospital=hospitaldata)
                return render(request,"Hospital/DoctorsReport.html",{'data':data,'data1':data1})
        else:
            return render(request,"Hospital/DoctorsReport.html")
    else:
        return redirect("Guest:login")
    return render(request,"Hospital/DoctorsReport.html")


############################ payment report #################################

def paymentreport(request):
    if 'hid' in request.session:
        totals=[]
        counts=[]
        totals1=[]
        counts1=[]
        hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
        pcdata=tbl_pyschiatrist.objects.filter(hospital=hospitaldata)
        pldata=tbl_pyschologist.objects.filter(hospital=hospitaldata)
        if request.method=="POST":
            
            if request.POST.get('txtft')!="" and request.POST.get('txttt')!="":
                
                datacount=tbl_psychologistappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),booking_to_date__lt=request.POST.get('txttt'),token__availability__psychologist__in=pldata).count()
                
                data1count=tbl_psychiatristappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),booking_to_date__lt=request.POST.get('txttt'),token__availability__psychiatrist__in=pcdata).count()
                counts.append(datacount)
                tot=150*datacount
                totals.append(tot)
                counts1.append(data1count)
                tot1=150*data1count
                totals1.append(tot1)
                data=zip(pcdata,counts1,totals1)
                data1=zip(pldata,counts,totals)           
                return render(request,"Hospital/PaymentReport.html",{'data':data,'data1':data1})
            elif request.POST.get('txtft')!="":
                
                datacount=tbl_psychologistappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),token__availability__psychologist__in=pldata).count()
                data1count=tbl_psychiatristappointment.objects.filter(booking_to_date__gt=request.POST.get('txtft'),token__availability__psychiatrist__in=pcdata).count()
                counts.append(datacount)
                tot=150*datacount
                totals.append(tot)
                counts1.append(data1count)
                tot1=150*data1count
                totals1.append(tot1)
                data=zip(pcdata,counts1,totals1)
                data1=zip(pldata,counts,totals) 
                return render(request,"Hospital/PaymentReport.html",{'data':data,'data1':data1})
            else:
                
                datacount=tbl_psychologistappointment.objects.filter(booking_to_date__lt=request.POST.get('txttt'),token__availability__psychologist__hospital=hospitaldata).count()
                data1count=tbl_psychiatristappointment.objects.filter(booking_to_date__lt=request.POST.get('txttt'),token__availability__psychiatrist__hospital=hospitaldata).count()
                counts.append(datacount)
                tot=150*datacount
                totals.append(tot)
                counts1.append(data1count)
                tot1=150*data1count
                totals1.append(tot1)
                data=zip(pcdata,counts1,totals1)
                data1=zip(pldata,counts,totals)  
                return render(request,"Hospital/PaymentReport.html",{'data':data,'data1':data1})
        else:
            return render(request,"Hospital/PaymentReport.html")
    else:
        return redirect("Guest:login")
    return render(request,"Hospital/PaymentReport.html")



def patienthistory(request):
    if 'hid' in request.session:
        hospitaldata=tbl_newhospital.objects.get(id=request.session["hid"])
        data=tbl_psychologistappointment.objects.filter(token__availability__psychologist__hospital=hospitaldata)
        data1=tbl_psychiatristappointment.objects.filter(token__availability__psychiatrist__hospital=hospitaldata)
        return render(request,"Hospital/PatientHistory.html",{'data':data,'data1':data1})
            
        
    else:
        return redirect("Guest:login")