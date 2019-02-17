from django import forms 

class NumWordForm(forms.Form):
    number = forms.IntegerField(label="Enter a Number: ",initial=0,
                min_value=0, max_value=1000000, widget=forms.NumberInput(attrs={"placeholder": "Enter a number"}))
    class Meta:  
        fields = "__all__"  