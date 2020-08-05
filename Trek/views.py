from django.http import HttpResponse, HttpRequest

from django.shortcuts import render

from datetime import datetime

# from .forms import Trek_form

from .models import Trek
from .models import Details
from django import forms

# from Hikeventure import settings




# Create your views here.

def Home(request,*args, **kwargs): 
    if request.method == "POST":
        Name      = request.POST.get('firstName')
        Last_Name = request.POST.get('lastName')
        Adventure = request.POST.get('Adventure')
        Email     = request.POST.get('Email')
        Mob_No    = request.POST.get('MobNo')
        message   = request.POST.get('message')
        
        details      = Details(Name=Name, Last_Name=Last_Name, Adventure=Adventure,
                          Email=Email, Mob_No=Mob_No, 
                          message=message
                          )
        details.save() 
    return  render(request, "trek_v2/Index.html")

def Treks(request,*args, **kwargs):  
    return  render(request, "trek_v2/Treks.html", {})

def Road_Trip(request,*args, **kwargs):  
    return  render(request, "trek_v2/road_trip.html", {})

def River_Rafting(request,*args, **kwargs):  
    return  render(request, "trek_v2/river_rafting.html", {})

def Contact(request,*args, **kwargs):  
    return  render(request, "trek_v2/contact.html", {})

def About(request,*args, **kwargs):  
    return  render(request, "trek_v2/About.html", {})





def test(a):
    b = a*5
    return b
    
def Book(request,*args, **kwargs): 
    user_input= {
    "UPIID": "BHIM UPI",
    "Gpay" : "G-PAY",
    }
    if request.method == "POST":
        Name = request.POST.get('firstName')
        Last_Name = request.POST.get('lastName')
        Adventure = request.POST.get('Adventure')
        Trek_Date = request.POST.get('TrekDate')
        Email     = request.POST.get('Email')
        Mob_No    = request.POST.get('MobNo')
        Country   = request.POST.get('Country')
        State     = request.POST.get('State')
        Zip       = request.POST.get('Zip')
        paymentMethod = request.POST.get('paymentMethod')
        Pay_ID    = request.POST.get('Pay-ID')
        kk = test(5)
        

        # Trek_Date = datetime.strptime((request.POST.get('TrekDate')), '%Y-%m-%d')
        trek      = Trek(Name=Name, Last_Name=Last_Name, Adventure=Adventure,
                         Trek_Date=Trek_Date,
                         Email=Email, Mob_No=Mob_No, Country=Country,
                         State=State, Zip=Zip, 
                         paymentMethod=paymentMethod,Pay_ID=Pay_ID,
                         kk=kk,
                         Book_Date=datetime.today()
                         )
        trek.save() 

    return  render(request, "trek_v2/Book.html", user_input)






def form_data(request,*args, **kwargs):  
    return  render(request, "trek/form.html", {})
    
def Home_view(request,*args, **kwargs):  
    return  render(request, "trek/default.html", {})
    
# def trek_form_view(request,*args, **kwargs): 
#     form = Trek_form(request.POST or None)
#     if request.method == "POST":
#         form = Trek_form(request.POST)
#         if form.is_valid():
#             form.save()
#             form = Trek_form()
#     context = {
#         'form': form
#         }
#     return  render(request, "trek/form.html", context)


  
def test_view(request):
        
    context  = {
        "var1": 2*2,
        "var2": 3*3,
        "m" :  [1,2,3,5,6,7]
        }
    for i in range(len(context["m"])):
        context["m"][i] = i*2
        print(i)
        
    return render(request, "trek/test.html" ,context)




