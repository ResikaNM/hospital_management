from django.shortcuts import render, redirect
from .forms import signupform,loginForm,BlogPostForm
from django.contrib.auth import authenticate,login
from .models import Patient,Doctor,customUser,BlogPost
from django.contrib.auth.decorators import login_required
# Create your views here.
def signupView(request):
    if request.method=='POST':
        form=signupform(request.POST,request.FILES)
        if form.is_valid():
            user=form.save()
            if form.cleaned_data['is_patient']:
                user.is_patient=True
                patient=Patient.objects.create(user=user)
            elif form.cleaned_data['is_doctor']:
                user.is_doctor=True
                doctor=Doctor.objects.create(user=user)
            user.save()
            login(request,user)
            return redirect('login')

    else:
        form=signupform()
    return render(request,'signup.html',{'form':form})

def loginView(request):
    if request.method=='POST':
        form=loginForm(request,data=request.POST)
        if form.is_valid():
           user=form.get_user()
           login(request,user)
           if user.is_patient:
            return redirect('Patient_Dashboard')
           elif user.is_doctor:
               return redirect('Doctor_Dashboard')

    else:
        form=loginForm()
    return render(request,'login.html',{'form':form})

@login_required()
def dashboard(request):
    user=request.user
    if user.is_patient:
        return render(request,'patient.html',{'user':user})
    elif user.is_doctor:
        return render(request,'doctor.html',{'user':user})
def blog_list(request):
    posts=BlogPost.objects.filter(is_draft=False)
    print("hiii")
    return render(request,'blog_list.html',{'posts':posts})

def blog_detail(request,pk):
    post=BlogPost.objects.get(pk=pk)
    return render(request,'blog_detail.html',{'post':post})

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})








