from django.shortcuts import render, redirect
from .models import Donor,EmergencyRequest

def home(request):
    return render(request,"home.html")


def profile(request, donor_id):

    donor = Donor.objects.get(id=donor_id)

    return render(request,"profile.html",{"donor":donor})

def register(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        blood_group = request.POST.get("blood_group")
        area = request.POST.get("area")
        available = request.POST.get("available") == "on"

        Donor.objects.create(
            name=name,
            email=email,
            phone=phone,
            blood_group=blood_group,
            area=area,
            available=available
        )

    return render(request,"register.html")


def search_donors(request):

    donors=Donor.objects.all()
    blood = request.GET.get("blood_group")
    area = request.GET.get("area")

    if blood:
        donors = donors.filter(blood_group=blood, available=True)
    if area:
        donors = donors.filter(area=area)
    return render(request,"search_donors.html",{"donors":donors})


from .models import Donor, EmergencyRequest

def emergency_request(request):

    donors = []

    if request.method == "POST":

        blood = request.POST.get("blood_group")
        area = request.POST.get("area")

        donors = Donor.objects.filter(
            blood_group=blood,
            area=area,
            available=True
        )

    return render(request,"emergency.html",{"donors":donors})


def dashboard(request):

    total = Donor.objects.count()

    available = Donor.objects.filter(available=True).count()

    a_pos = Donor.objects.filter(blood_group="A+").count()
    b_pos = Donor.objects.filter(blood_group="B+").count()
    o_pos = Donor.objects.filter(blood_group="O+").count()

    context = {
        "total": total,
        "available": available,
        "a_pos": a_pos,
        "b_pos": b_pos,
        "o_pos": o_pos
    }

    return render(request,"dashboard.html",context)

def toggle_availability(request, donor_id):

    donor = Donor.objects.get(id=donor_id)

    donor.available = not donor.available
    donor.save()

    return redirect("profile",donor_id=donor.id)