from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .models import TenetDetails,ReportDetails
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.



def adminhome(request):
    return render(request, 'adminhome.html')




def tenantdetails(request):
    tenants = TenetDetails.objects.all()
    return render(request,'tenantdetails.html',{'tenants': tenants})




def logout(request):
    request.session.flush()
    return redirect('login')


def login(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username =='balasekar' and password == 'bala9942':
            return render(request,'adminhome.html')
        try:
            user=TenetDetails.objects.get(username=username)
            
        except TenetDetails.DoesNotExist:
            messages.error(request,'user not found')
            return redirect('signup')
        if check_password(password,user.password):
            request.session['username']=user.username
            request.session['name']=user.name
            messages.success(request,'login succesfull')
            return redirect('home')
        else:
            messages.error(request,'password doesnot match')
            return redirect('signup')
    return render(request,'login.html')




def home(request):
    if 'username' not in request.session:
        messages.error(request, 'Please login first!')
        return redirect('login')

    tenant = TenetDetails.objects.get(username=request.session['username'])

    resolved_reports = ReportDetails.objects.filter(
        tenant=tenant,
        status='Resolved'
    ).order_by('-id')

    return render(request,'home.html',{'resolved_reports': resolved_reports})

def contact(request):
    return render(request,'contact.html')



def about(request):
    return render(request,'about.html')



def report(request):
    if 'username' not in request.session:
        messages.error(request, 'Please login first!')
        return redirect('login')

    try:
        tenant = TenetDetails.objects.get(username=request.session['username'])

    except TenetDetails.DoesNotExist:
        messages.error(request, 'Tenant not found!')
        return redirect('login')

    if request.method == 'POST':
        about = request.POST.get('about')
        description = request.POST.get('description')

        ReportDetails.objects.create(
            tenant=tenant,
            about=about,
            description=description,
            status='Pending'
        )

        messages.success(request,'Your report has been submitted successfully!')
        return redirect('home')

    return render(request, 'report.html')





def reportdetails(request):
    reports = ReportDetails.objects.all().order_by('-id')
    return render(request,'reportdetails.html',{'reports': reports})

    


def signup(request):
    if request.method== "POST":
        name=request.POST.get('name')
        age=request.POST.get('age')
        city=request.POST.get('city')
        phone=request.POST.get('phone')
        username=request.POST.get('username')
        password=request.POST.get('password')
        payment=request.POST.get('payment')
        aadhaar_number=request.POST.get('aadhaar_number')
        room_no=request.POST.get('room_no')

        if TenetDetails.objects.filter(username=username).exists():
            message.error(request,'already exixted username!!!')
            return redirect('login')
        
        TenetDetails.objects.create(
            name=name,
            age=age,
            city=city,
            username=username,
            password=make_password(password),
            phone=phone,
            payment=payment,
            aadhaar_number=aadhaar_number,
            room_no=room_no
        )
        return redirect ('login')
    return render(request,'signup.html')






def update_report_status(request, id):
    if request.method == "POST":
        try:
            report = ReportDetails.objects.get(id=id)
        except ReportDetails.DoesNotExist:
            messages.error(request,'Report not found!')
            return redirect('reportdetails')

        status = request.POST.get('status')
        if status in ['Pending', 'Resolved']:
            report.status = status
            report.save()
            messages.success(request,'Report status updated successfully!')
    return redirect('reportdetails')

