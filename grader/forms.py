from django.forms import ModelForm
from grader.models import *



class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['f','name']
