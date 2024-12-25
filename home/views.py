from django.shortcuts import render,redirect
from .forms import UserRegistrationForm
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
# Create your views here.

def index(request):
    feedbacks=CustomerFeddback.objects.all()
    return render(request,'surveys.html',{"feedbacks":feedbacks})
# @login_required
def Customer_feedback(request,id):
    feedback=CustomerFeddback.objects.get(id=id)
    if request.method =='POST':
        for question in feedback.question.all():
            response_text=request.POST.get(f"response_{question.id}")
            selected_option_ids=request.POST.getlist(f"options_{question.id}")
            
            print(response_text)
            print(selected_option_ids)
            response=CustomerResponse.objects.create(
                feedback=feedback,
                question=question,
                response_text=response_text if question.question_type in ["Text","BigText"] else None
            )
            if selected_option_ids:
                selected_options=Options.objects.filter(id__in=selected_option_ids)
                response.selected_options.set(selected_options)

        return redirect('thank-you')
    
       
    return render(request,'survey.html',{"questions":feedback.question.all()})
    
def thank_you(request):
    return render(request,'thank_you.html')

def register(request):
    if request.method =="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('index')
    else:
        form=UserRegistrationForm()
    return render(request,'registration/register.html',{'form':form})
def about(request):
    return render(request,'about.html')