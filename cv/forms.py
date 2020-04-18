from django.forms import ModelForm
from .models import Resume


class ResumeForm(ModelForm):

    class Meta:
        model = Resume
        fields = ['your_image','first_name', 'last_name','permanent_address','mobile','your_intro','mail','linkedin','github','facebook','hobies','skills','highest_qualification','graduation_year','institute_name','graduation_achievements','present_company','present_role','present_start','present_end','present_work','previous_company','previous_role','previous_start','previous_end','previous_work']

 