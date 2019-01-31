from django import forms
from .models import Client


class ClientCreateForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(ClientCreateForm, self).clean()
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super(ClientCreateForm, self).__init__(*args, **kwargs)
        self.fields['client_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['street_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['suburb'].widget.attrs.update({'class' : 'form-control'})
        self.fields['postcode'].widget.attrs.update({'class' : 'form-control'})
        self.fields['state'].widget.attrs.update({'class' : 'form-control'})
        self.fields['contact_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['phone'].widget.attrs.update({'class' : 'form-control'})


    #      client_name = models.CharField(max_length=255, unique=True)
    # street_name = models.CharField(max_length=255)
    # suburb = models.CharField(max_length=255)
    # postcode = models.CharField(max_length=10)
    # state = models.CharField(max_length=255)
    # contact_name = models.CharField(max_length=255)
    # email = models.EmailField(max_length=255)
    # phone = models.CharField(max_length=20)

    class Meta:
        model = Client

        fields = '__all__'


class ClientUpdateForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(ClientUpdateForm, self).clean()
        return cleaned_data
    

    def __init__(self, *args, **kwargs):
        super(ClientCreateForm, self).__init__(*args, **kwargs)
        self.fields['client_name'].widget.attrs.update({'class' : 'form-control'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control'})
        self.fields['phone'].widget.attrs.update({'class' : 'form-control'})

    class Meta:
        model = Client
        fields = '__all__'


