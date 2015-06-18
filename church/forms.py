from django import forms
from church.models import *
from django.contrib.auth.models import User
#class CommentForm(forms.ModelForm):
	#name=forms.CharField(max_length=42,help_text="Name")
	#email=forms.EmailField(max_length=75,help_text="Email")
	#text =forms.CharField(max_length=200)
	##class Meta:
		#model = SermonComment
		#exclude = ['sermon',]
		
class CommentForm(forms.ModelForm):
    class Meta:
        model = SermonComment
        exclude = ['sermon',]
        
