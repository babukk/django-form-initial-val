
from django.shortcuts import render

from .forms import AddressForm, FinalForm, CITIES


def form1_view(request, *args, **kwargs):
    form = AddressForm()
    return render(request, "testform/form1.html", {'form': form,})


def form2_view(request, *args, **kwargs):
    city = request.POST.get("city", "")
    address = request.POST.get("address", "")
    email = request.POST.get("email", "")
    form = FinalForm(initial={'city': city, 'address': address, 'email': email,})
    return render(request, "testform/form2.html", {'form': form,})


def final_page(request, *args, **kwargs):
    city = request.POST.get("city", "")
    try:
        city = CITIES[int(city)][1]
    except IndexError as e:
        city = 'Москва'
    address = request.POST.get("address", "")
    email = request.POST.get("email", "")
    name = request.POST.get("name", "")
    return render(request, "testform/final_page.html",
        {'city': city, 'address': address, 'email': email, 'name': name}
    )
