from django.shortcuts import render,redirect
from Admin.models import tbl_rescueteam,tbl_place
from User.models import *
from Hospital.models import *
from Rescueteam.models import *
from Guest.models import *
# Create your views here.
def homepage(request):
    if 'rid' in request.session:
        return render(request,"Rescueteam/Homepage.html")
    else:
        return redirect("Guest:login")

def myprofile(request):
    if 'rid' in request.session:
        rescuedata=tbl_rescueteam.objects.get(id=request.session["rid"])
        return render(request,"Rescueteam/Myprofile.html",{'data':rescuedata})
    else:
        return redirect("Guest:login")

def editprofile(request):
    rescuedata=tbl_rescueteam.objects.get(id=request.session["rid"])
    if request.method=='POST':
        rescuedata.name=request.POST.get('txtname')
        rescuedata.contact=request.POST.get('txtcontact')
        rescuedata.email=request.POST.get('txtemail')
        rescuedata.address=request.POST.get('txtaddress')
        rescuedata.save()
        return redirect("Rescueteam:myprofile")
    else:
        return render(request,"Rescueteam/Editprofile.html",{'data':rescuedata})

def changepassword(request):
    if request.method=='POST':
        rescuecount=tbl_rescueteam.objects.filter(id=request.session["rid"],password=request.POST.get('txtcurrent')).count()
        if rescuecount>0:
            if request.POST.get('txtnew')==request.POST.get('txtconfirm'):
                rescuedata=tbl_rescueteam.objects.get(id=request.session["rid"])
                rescuedata.password=request.POST.get('txtnew')
                rescuedata.save()
                return redirect("Rescueteam:homepage")
            else:
                return render(request,"Rescueteam/Changepassword.html")
        else:
            return render(request,"Rescueteam/Changepassword.html")
    else:        
        return render(request,"Rescueteam/Changepassword.html")


def emergencyrequest(request):
    if 'rid' in request.session:
        placedata=tbl_place.objects.get(id=request.session["pid"])
        data=tbl_emergencyrequest.objects.filter(user__place=placedata,status=0)
        return render(request,"Rescueteam/Emergencyrequest.html",{'data':data})
    else:
        return redirect("Guest:login")

def aemergencyrequest(request):
    if 'rid' in request.session:
        placedata=tbl_place.objects.get(id=request.session["pid"])
        data=tbl_emergencyrequest.objects.filter(user__place=placedata,status=1)
        return render(request,"Rescueteam/AcceptEmergencyrequest.html",{'data':data})
    else:
        return redirect("Guest:login")

def remergencyrequest(request):
    if 'rid' in request.session:
        placedata=tbl_place.objects.get(id=request.session["pid"])
        data=tbl_emergencyrequest.objects.filter(user__place=placedata,status=2)
        return render(request,"Rescueteam/RejectEmergencyrequest.html",{'data':data})
    else:
        return redirect("Guest:login")

def acceptrequest(request,dd):
    if 'rid' in request.session:
        data=tbl_emergencyrequest.objects.get(id=dd)
        data.status=1
        data.save()
        return redirect("Rescueteam:emergencyrequest")
    else:
        return redirect("Guest:login")


def rejectrequest(request,dd):
    if 'rid' in request.session:
        data=tbl_emergencyrequest.objects.get(id=dd)
        data.status=2
        data.save()
        return redirect("Rescueteam:emergencyrequest")
    else:
        return redirect("Guest:login")

def informhospital(request,hh):
    if 'rid' in request.session:
        request.session["emergency"]=hh
        requestdata=tbl_emergencyrequest.objects.get(id=hh)
        placedata=tbl_place.objects.get(id=request.session["pid"])
        data=tbl_newhospital.objects.filter(status=1,place=placedata)
        return render(request,"Rescueteam/InformHospital.html",{'data':data})
    else:
        return redirect("Guest:login")

def inform(request,hid):
    if 'rid' in request.session:
        emergencydata=tbl_emergencyrequest.objects.get(id=request.session["emergency"])
        hospitaldata=tbl_newhospital.objects.get(id=hid)
        rescuedata=tbl_rescueteam.objects.get(id=request.session["rid"])
        tbl_rescueinfo.objects.create(rescue=rescuedata,hospital=hospitaldata,emergency=emergencydata)
        return redirect("Rescueteam:homepage")
    else:
        return redirect("Guest:login")

def emergencydetails(request):
    if 'rid' in request.session:
        rescuedata=tbl_rescueteam.objects.get(id=request.session["rid"])
        data=tbl_rescueinfo.objects.filter(rescue=rescuedata)
        return render(request,"Rescueteam/EmergencyDetails.html",{'data':data})
    else:
        return redirect("Guest:login") 



def deledetails(request,did):
    tbl_emergencyrequest.objects.get(id=did).delete()
    return redirect("Rescueteam:emergencydetails")


def deleunknowndetails(request,did):
    tbl_unknownemergency.objects.get(id=did).delete()
    return redirect("Rescueteam:emergencydetailsunknown")

################# unknown emergency ########


def unknownemergencyrequest(request):
    if 'rid' in request.session:
        placedata=tbl_place.objects.get(id=request.session["pid"])
        data=tbl_unknownemergency.objects.filter(place=placedata,status=0)
        return render(request,"Rescueteam/UnknownEmergencyRequest.html",{'data':data})
    else:
        return redirect("Guest:login")

def uaemergencyrequest(request):
    if 'rid' in request.session:
        placedata=tbl_place.objects.get(id=request.session["pid"])
        data=tbl_unknownemergency.objects.filter(place=placedata,status=1)
        return render(request,"Rescueteam/AcceptUnknownEmergency.html",{'data':data})
    else:
        return redirect("Guest:login")

def uremergencyrequest(request):
    if 'rid' in request.session:
        placedata=tbl_place.objects.get(id=request.session["pid"])
        data=tbl_unknownemergency.objects.filter(place=placedata,status=2)
        return render(request,"Rescueteam/RejectUnknownEmergency.html",{'data':data})
    else:
        return redirect("Guest:login")

def acceptunknownrequest(request,dd):
    if 'rid' in request.session:
        data=tbl_unknownemergency.objects.get(id=dd)
        data.status=1
        data.save()
        return redirect("Rescueteam:unknownemergencyrequest")
    else:
        return redirect("Guest:login")


def rejectunknownrequest(request,dd):
    if 'rid' in request.session:
        data=tbl_unknownemergency.objects.get(id=dd)
        data.status=2
        data.save()
        return redirect("Rescueteam:unknownemergencyrequest")
    else:
        return redirect("Guest:login")

def informhospitalunknown(request,hh):
    if 'rid' in request.session:
        request.session["emergency"]=hh
        requestdata=tbl_unknownemergency.objects.get(id=hh)
        placedata=tbl_place.objects.get(id=request.session["pid"])
        data=tbl_newhospital.objects.filter(status=1,place=placedata)
        return render(request,"Rescueteam/InformhospitalUnknown.html",{'data':data})
    else:
        return redirect("Guest:login")


def informunknown(request,hid):
    if 'rid' in request.session:
        emergencydata=tbl_unknownemergency.objects.get(id=request.session["emergency"])
        hospitaldata=tbl_newhospital.objects.get(id=hid)
        rescuedata=tbl_rescueteam.objects.get(id=request.session["rid"])
        tbl_rescueinfounknown.objects.create(rescue=rescuedata,hospital=hospitaldata,emergency=emergencydata)
        return redirect("Rescueteam:homepage")
    else:
        return redirect("Guest:login")


def emergencydetailsunknown(request):
    if 'rid' in request.session:
        rescuedata=tbl_rescueteam.objects.get(id=request.session["rid"])
        data=tbl_rescueinfounknown.objects.filter(rescue=rescuedata)
        return render(request,"Rescueteam/UnknownEmergencyDetails.html",{'data':data})
    else:
        return redirect("Guest:login") 

##########

def logout(request):
    del request.session["rid"]
    return redirect("Guest:login")