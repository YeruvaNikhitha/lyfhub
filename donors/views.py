from django.shortcuts import render, redirect
from .models import Donor

def home(request):
    return render(request,"home.html")


from .models import Donor

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


def emergency(request):
    donors = Donor.objects.filter(available=True)
    return render(request,"search_donors.html",{"donors":donors})


def admin_dashboard(request):

    total_donors = Donor.objects.count()

    available_donors = Donor.objects.filter(available=True).count()

    tirupati = Donor.objects.filter(area="Tirupati").count()

    renigunta = Donor.objects.filter(area="Renigunta").count()

    chandragiri = Donor.objects.filter(area="Chandragiri").count()

    context = {
        "total_donors": total_donors,
        "available_donors": available_donors,
        "tirupati": tirupati,
        "renigunta": renigunta,
        "chandragiri": chandragiri
    }

    return render(request, "admin_dashboard.html", context)