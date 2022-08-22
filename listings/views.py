from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Personne
from listings.models import Band ,Listing
from listings.forms import ContactUseForms ,BandForm,ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect
def page1(request):
    personnes=Personne.objects.all()

    return render(request,'listings/page1.html',{"personnes":personnes})

def Band_list (request):
    bands =Band.objects.all()


    return render(request,'listings/band_list.html',{"bands":bands})

def get_band (request,id):
    bands=Band.objects.get(id=id)
    return render(request,'listings/get_band.html',{"bands":bands})
def contact(request):
    if request.method=='POST':
        form=ContactUseForms(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message de {form.cleaned_data["name"]}',
                message=form.cleaned_data["msg"],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@app/xyz'],

            )
            return redirect("contacts")
    else:
        form = ContactUseForms()
    return render(request,"listings/contact.html",{"form":form})


def BandAdd(request):
    if request.method =='POST':
        form=BandForm(request.POST)
        if form.is_valid():
            band=form.save()
            return redirect('band_ditail',band.id)
    else :
            form=BandForm()
    return render(request,"listings/Band_Add.html", {'form':form})


def Listing_(request):
    listings=Listing.objects.all()
    return render(request,"listings/listings.html",{"listings":listings})

def ListingAdd(request):
    if request.method=='POST':
        form=ListingForm(request.POST)
        if form.is_valid():
            listing=form.save()
            return redirect("listing_ditail",listing.id)
    else:
        form=ListingForm()
    return render(request,"listings/listingadd.html",{'form':form})

def GetListing (request,id):
    listing=Listing.objects.get(id=id)
    return render(request,"listings/listingditail.html",{"listing":listing})

def update_band(request,id):
    band=Band.objects.get(id=id)
    if request.method=="POST":
        form=BandForm(request.POST,instance=band)
        if form.is_valid():
            band=form.save()
            return redirect("band_ditail",band.id)
    else:
        form = BandForm(instance=band)

    return render(request,"listings/update_band.html",{"form":form})
def update_listings(request,id):
    listing=Listing.objects.get(id=id)
    if request.method=='POST':
        form=ListingForm(request.POST,instance=listing)
        if form.is_valid():
            listing=form.save()
            return redirect("listing_ditail",listing.id)

    else :
        form = ListingForm(instance=listing)
    return render(request,"listings/update_listings.html",{"form":form})
def delate_band(request,id):
    band=Band.objects.get(id=id)
    if request.method=='POST':
        band.delete()
        return redirect('band_list')
    return render(request,'listings/delate_band.html',{'band':band})



