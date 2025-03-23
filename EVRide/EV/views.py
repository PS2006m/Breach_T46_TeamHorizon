from django.shortcuts import render,redirect
import random
from django.contrib import messages
# Create your views here.
from .models import Stations,Vehicle,Rides,Customer
from django.conf import settings
from django.core.mail import send_mail

def login(request):
    return render(request,'login_Signup.html')

class Vars:
    email,name,number,password,otp="","","","",""

class Locs:
    pickup,end="",""
    
class Veh:
    vehicle_Id=""

def signup(request):
    Vars.email=request.POST['c_email']
    Vars.name=request.POST['c_name']
    Vars.number=request.POST['c_cnum']
    Vars.password=request.POST['pass']
    confirm_password=request.POST['c_pass']
    msg=""
    if Vars.password==confirm_password:
        user_email = Vars.email  # Get the logged-in user's email
        random_otp=random.randint(100000,999999)
        subject = "Your OTP for Login"
        message = f"Hi {Vars.name}, Your OTP is {str(random_otp)}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)
        request.session['otp']=random_otp
        return redirect('otp')
    else:
        msg="Password and Confirm Password does not match"
        return render(request,'login_Signup.html',{"msg":msg})

def otp(request):
    try:
        if request.method == "POST":
            otp = request.POST.get('otp', '')
            otp = int(otp)

            stored_otp = request.session.get('otp')
            if stored_otp and stored_otp == otp:
                Customer.objects.create(
                    customer_name=Vars.name,
                    customer_password=Vars.password,
                    customer_number=Vars.number,
                    customer_email=Vars.email
                )
                del request.session['otp']  # Clear OTP after verification
                return redirect('login')  # Redirect to login page
            else:
                return render(request, 'otp.html', {'msg': "Invalid OTP"})
    except Exception as e:
        print(e)  # Consider logging this instead
        return render(request, 'otp.html', {'msg': str(e)})

    return render(request, 'otp.html')

    

def signin(request):
    if request.method=="POST":
        try:
            user=Customer.objects.get(customer_email=request.POST['email'])
            if user.customer_password==request.POST['password']:
                print("Good")
                request.session['email']=user.customer_email
                return redirect('home')
            else:
                msg="Wrong Password"
                return render(request,'login_Signup.html',{"msg":msg})
        except Exception as e:
            print(e)
            msg="Signup First"
            return render(request,'login_Signup.html',{'msg':msg})

def home(request):
    if request.method=="POST":
        request.session['pickup']=request.POST['pickup']
        request.session['end']=request.POST['end']
        return redirect('vehicle')
    station=Stations.objects.all()
    customer=Customer.objects.get(customer_email=request.session['email'])
    name=customer.customer_name.split(" ")
    master=False
    if 'sm' in name:
        master=True
    pen=False
    if customer.customer_penalty!=0:
        pen=True
    return render(request,'home.html',{'station':station,'customer':customer.customer_penalty,'pen':pen,'master':master})

def vehicle(request):
    print(request.session['pickup'])
    station=Stations.objects.get(station_id=request.session['pickup'])
    vehicles=Vehicle.objects.all()
    vehiclesstation=[]
    stationveh=station.station_vehicles.split(",")
    print(stationveh)
    for i in vehicles:
        if str(i.vehicle_id) in stationveh:
            vehiclesstation.append(i)
    print(vehiclesstation)
    return render(request,'vehicle.html',{'vehiclesstation':vehiclesstation})

def rv(string,id):
    sp=string.split(",")
    new=""
    for i in sp:
        if str(id)==i:
            continue
        new+=","+i
    return new

def av(string,id):
    return string+","+str(id)

def book(request):
    vehicleId=int(request.POST['id'])
    request.session['vehicle_Id']=vehicleId
    station1=request.session['pickup']
    station2=request.session['end']
    customer=Customer.objects.get(customer_email=request.session['email'])
    r=Rides.objects.create(customer_id=customer.customer_id,vehicle_id=vehicleId,pickup_station_id=
                         request.session['pickup'],drop_station_id=request.session['end'])
    request.session['ride_id'] = r.ride_id
    loc1=Stations.objects.get(station_id=request.session['pickup'])
    loc2=Stations.objects.get(station_id=request.session['end'])
    loc1.station_vehicles=rv(loc1.station_vehicles,vehicleId)
    loc1.save()
    point1=loc1.station_location.split(",")
    point2=loc2.station_location.split(",")
    lat11=point1[0]
    long11=point1[1]
    lat22=point2[0]
    long22=point2[1]
    return render(request,'route.html',{'lat1':lat11,'long1':long11,'lat2':lat22,'long2':long22,
                                        'station1':station1,'station2':station2})
    
def reached(request):
    st=Stations.objects.get(station_id=request.session['end'])
    st.station_vehicles=av(st.station_vehicles,request.session['vehicle_Id'])
    st.save()
    ride=Rides.objects.get(ride_id=request.session['ride_id'])
    ride.distance=request.GET.get('distance')
    total_distance = request.GET.get('distance')
    vehicle=Vehicle.objects.get(vehicle_id=request.session['vehicle_Id'])
    priceperkm=vehicle.vehicle_pricePerKm
    totalprice=float(total_distance)*int(priceperkm)
    ride.total_cost=totalprice
    ride.save()
    print(totalprice)
    return render(request,'bill.html',{'msg':"Total Price is "+str(totalprice)})

def adminui(request):
    # total_distance_till_now = sum([x for x  in Rides.distance])
    # total_revenue = sum([x  for x in Rides.total_cost])
    return render(request,'admin.html')

def sm(request):
  post_che=False
  if request.method=="POST":
      vehicle=Vehicle.objects.get(vehicle_id=request.POST['vehicleNo'])
      damages=request.POST['vehicleCost']
    #   ride=Rides.objects.get(ride_id=request.session['ride_id'])
    #   ride.total_cost+=damages
    #   ride.save()
      customer=Customer.objects.get(customer_email=request.session['email'])
      customer.customer_penalty+=float(damages)
      customer.save()
      return redirect('home')
  return render(request,"sm.html")

def user_route(request):
    pass

def route_trace(request):
    pass

def end_ride(request):
    pass
