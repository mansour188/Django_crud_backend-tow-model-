from  django import forms
from listings.models import Band,Listing
class ContactUseForms (forms.Form):
    name=forms.CharField(max_length=100,required=False)
    email=forms.EmailField()
    msg=forms.CharField(max_length=100)
class BandForm (forms.ModelForm):
    class Meta:
        model=Band
        fields= '__all__'

class ListingForm(forms.ModelForm):
    class Meta:
        model=Listing
        fields='__all__'

