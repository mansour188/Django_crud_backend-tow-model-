"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page1/',views.page1),
    path('bands/',views.Band_list, name="band_list"),
    path('bands/<int:id>/',views.get_band,name="band_ditail"),
    path('bands/<int:id>/update/',views.update_band,name='update_band'),
    path('bands/BandAdd/', views.BandAdd, name="band_create"),
    path('bands/<int:id>/delate/',views.delate_band,name="band_delate"),
    path("contact_us/",views.contact,name="contact"),
    path("listings/",views.Listing_,name="listing_list"),
    path("listings/ListngAdd", views.ListingAdd, name="listing_add"),
    path("listings/<int:id>/", views.GetListing, name="listing_ditail"),
    path("listings/<int:id>/update_listings/", views.update_listings, name="listing_update"),

]
