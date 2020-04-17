from django.shortcuts import render, redirect

from .forms import ResumeForm
from .models import Resume

def resume(request):
    if request.method == "POST":
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = Resume(first_name = form.cleaned_data['first_name'], last_name =  form.cleaned_data['last_name'],mobile = form.cleaned_data['mobile'], mail = form.cleaned_data['mail'],linkedin = form.cleaned_data['linkedin'],github = form.cleaned_data['github'],facebook = form.cleaned_data['facebook'],hobies = form.cleaned_data['hobies'],skills = form.cleaned_data['skills'],present_company = form.cleaned_data['present_company'],present_role = form.cleaned_data['present_role'],previous_role = form.cleaned_data['previous_role'],previous_company = form.cleaned_data['previous_company'],your_intro = form.cleaned_data['your_intro'],present_work = form.cleaned_data['present_work'],previous_work = form.cleaned_data['previous_work'])
            resume.save()
            form.save()
            return redirect('/cv/final')
    else:
        form = ResumeForm()
    
    context = {'form' : form}
    return render(request, 'cv/resume.html', context)

def final(request):
    resume= Resume.objects.all()
    l= len(resume)
    resume = resume[l-1]
    skills= resume.skills.split(',')
    present = resume.present_start + '-' + resume.present_end
    previous = resume.previous_start + '-' + resume.previous_end
    context = {'resume': resume, 'skills': skills, 'present': present, 'previous': previous}
    return render(request, 'final.html', context)
