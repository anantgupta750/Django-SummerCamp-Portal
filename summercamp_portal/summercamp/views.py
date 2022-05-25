from django.shortcuts import redirect,render,HttpResponse
from .models import *
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

#HOME.HTML
def home(request):
    eventsobjset=Cityevents.objects.all()
    context={
        "eventkey":eventsobjset
    }
    return render(request,'summercamp/home.html',context)

def contactus(request):
    if request.method=="POST":
        #print(request.POST)
        cname=request.POST["txtname"]
        cemail=request.POST["txtemail"]
        cphone=request.POST["txtphonenumber"]
        cques=request.POST["txtques"]
        #print(cname,cemail,cphone,cquery) #only use to check instance names are correct
        contact_obj=Contactus(name=cname,email=cemail,phone=cphone,question=cques) #making object of the class
        contact_obj.save() #it is ORM 
        print("Contact added successfully")
        messages.success(request,"Thankyou For Cotancting SummerCamp") #to show message to users

    return render(request,'summercamp/contactus.html')

def feedback(request):
    if request.method=="POST":
        print(request.POST)

    return render(request,'summercamp/feedback.html')

def registration(request):
    if request.method=="POST":
        #print(request.POST)
        id=request.POST["txtid"]
        cpass=request.POST["txtpass"]
        cname=request.POST["txtcname"]
        oname=request.POST["txtoname"]
        email=request.POST["txtemail"]
        number=request.POST["txtphonenumber"]
        add=request.POST["txtaddress"]
        des=request.POST["txtdes"]
        res_obj=Organizer(summercamp_id=id,password=cpass,campname=cname,ownername=oname,campemailid=email,campmobileno=number,campaddress=add,description=des) #making object of the class
        res_obj.save() #it is ORM 
        print("Organizer added successfully")
        messages.success(request,"Registration Done Successfully")
    return render(request,'summercamp/registration.html')

def feedback(request):
    if request.method=="POST":
        name=request.POST["txtname"]
        email=request.POST["txtemail"]
        campname=request.POST["txtcampname"]
        feedback=request.POST["txtfeedback"]
        rating=request.POST["cmbrating"]
        fed_obj=Feedback(name=name,email=email,campname=campname,feedbacktext=feedback,ratings=rating)
        fed_obj.save()
        print("feedback submitted")

    return render(request,'summercamp/feedback.html')

def viewevents(request):
    eventobjset=Cityevents.objects.all()
    context={
        "eventdata":eventobjset
    }
    return render(request,'summercamp/viewevents.html',context)
    
def login(request):
    if request.method=="GET":
        return render(request,'summercamp/login.html')
    if request.method=="POST":
        print(request.POST)
        campid=request.POST["txtid"] 
        camppass=request.POST["txtpass"]
        print(campid,camppass) 
        camp_obj=Organizer.objects.filter(summercamp_id=campid,password=camppass)
        print(camp_obj)
        if len(camp_obj)>0:
            context={
                    "campdata":camp_obj
                }
            request.session["session_id"]=campid
            return render(request,'summercamp/organizer_home.html',context)
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("login")


#ORGANIZER_HOME.HTML
def organizer_home(request):
    campid=request.session["session_id"]
    print(campid)
    camp_obj=Organizer.objects.filter(summercamp_id=campid)
    for c in camp_obj:
        print(c.campname)
    context={"campdata":camp_obj}
    return render(request,'summercamp/organizer_home.html',context)

#ORGANIZER_EDITPROFILE.HTML
def organizer_editprofile(request):
    if request.method=="GET":
        campid=request.session["session_id"]
        camp_obj=Organizer.objects.get(summercamp_id=campid)
        print(camp_obj.campname)
        context={
                    "cdata":camp_obj
                }
        return render(request,'summercamp/organizer_editprofile.html',context)

    if request.method=="POST":
        print(request.POST)
        c_cname=request.POST["txtcname"]
        c_email=request.POST["txtemail"]
        c_number=request.POST["txtphonenumber"]
        c_add=request.POST["txtaddress"]
        campid=request.session["session_id"]
        camp_obj=Organizer.objects.filter(summercamp_id=campid)
        camp_obj.update(camp_name=c_cname,camp_email=c_email,camp_phone=c_number,camp_address=c_add)
        return redirect('organizer_home')

#ORGANIZER_LOGOUT.HTML
def logout(request):
    del request.session["session_id"]
    messages.success(request,"successfully logout")
    return redirect("login")

#ORGANIZER_PROGRAM_DETAILS.HTML
def program_details(request):
    if request.method=="POST":
        campid=request.session["session_id"]
        # organizer_obj=Organizer.objects.get(Summercamp_Id=campid)
        print(campid)
        pname=request.POST["txtpname"]
        duration=request.POST["txtduration"]
        fees=request.POST["txtfees"]
        sdate=request.POST["txtsdate"]
        edate=request.POST["txtedate"]
        description=request.POST["txtdes"]
        age=request.POST["txtage"]
        pd_obj=Program_details(summercamp_id=campid,programname=pname,duration=duration,fees=fees,startdate=sdate,enddate=edate,description=description,agegroup=age)
        pd_obj.save() #it is ORM 
        print("Organizer program Details added successfully")
        messages.success(request,"Programs Details Added Successfully")
    return render(request,'summercamp/program_details.html')


#JOB_DESCRIPTION.HTML
def job_description(request):
    if request.method=="POST":
        campid=request.session["session_id"]
        # organizer_obj=Organizer.objects.get(Summercamp_Id=campid)
        print(campid)
        job_id=request.POST["txtjid"]
        pname=request.POST["txtpname"]
        jseats=request.POST["txtseats"]
        ldate=request.POST["txtldate"]
        pdate=request.POST["txtpdate"]
        description=request.POST["txtdes"]
        job_obj=Job_description(summercamp_id=campid,jobid=job_id,postname=pname,noofseats=jseats,lastdateofapply=ldate,postdate=pdate,description=description)
        job_obj.save() #it is ORM 
        print("Job Details added successfully")
        messages.success(request,"job Details Added Successfully")
    
    return render(request,'summercamp/job_description.html')

#PROGRAM_VIEW.HTML
def viewprograms(request):
    programobjset=Program_details.objects.all()
    context={
        "programdata":programobjset
    }
    return render(request,'summercamp/viewprograms.html',context)

#JOB_VIEW.HTML
def viewjobs(request):
    jobobjset=Job_description.objects.all()
    context={
        "jobdata":jobobjset
    }
    return render(request,'summercamp/viewjobs.html',context)

