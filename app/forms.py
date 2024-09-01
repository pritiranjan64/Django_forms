from django import forms
from app.models import *


g=[['MALE','male'],('FEMALE','female')]
c=[('python','python'),('django','django'),('sql','sql')]
class SchoolForm(forms.Form):
    Sname=forms.CharField(max_length=100)
    Sage=forms.IntegerField(min_value=5)
    Semail=forms.EmailField()
    Surl=forms.URLField()
    Spassword=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':10,'rows':5}))
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #Scourse=forms.MultipleChoiceField(choices=c)
    Scourse=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)


class TopicForm(forms.Form):
    topic_name=forms.CharField(max_length=100)


class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100)
    url=forms.URLField()
    email=forms.EmailField()

class AccessRecordForm(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    date=forms.DateField()
    author=forms.CharField(max_length=100)
