from django.shortcuts import render, redirect
from django.views import View
from .models import Tutorial, EnrolledTutorial, TutorialMedia
from user.models import MainUser, Skill
from django.contrib import messages
from django.contrib.auth.models import User

class HomeView(View):
    def get(self, request):
        tutorials = Tutorial.objects.all()
        mainuser = MainUser.objects.get(user=request.user)
        return render(request, 'home.html',{'tutorials':tutorials, 'mainuser':mainuser})

class CourseDetailView(View):
    def get(self, request,pk):
        tutorial = Tutorial.objects.get(id=pk)
        mainuser = MainUser.objects.get(user=request.user)
        if tutorial.user != mainuser:
            tutorial.tutorial_views += 1
            tutorial.save()
        else:
            pass
        return render(request, 'course-details.html',{'tutorial':tutorial})
    
class AddEnrolledCourseView(View):
    def get(self, request, pk):
        mainuser = MainUser.objects.get(user=request.user)
        tutorial = Tutorial.objects.get(id=pk)
        if not Tutorial.id == tutorial:
            enroll = EnrolledTutorial.objects.create(
                user=mainuser,
                tutorial=tutorial
            )
        else:
            messages.error(request, "You are already enrolled this course")
        return redirect('home')

class ProfileView(View):
    def get(self, request):
        mainuser = MainUser.objects.get(user=request.user)
        skills = Skill.objects.get(user=mainuser)
        courses = Tutorial.objects.filter(user=mainuser)
        return render(request, 'pages-profile.html',{'mainuser':mainuser, 'courses':courses, 'skills':skills})

class AnalyticView(View):
    def get(self, request):
        tutorial = Tutorial.objects.filter(user=MainUser.objects.get(user=request.user))
        
        labels = []
        data = []
        tutorial_views = Tutorial.objects.order_by('-tutorial_views')[:3]
        for person in tutorial_views:
            labels.append(person.tutorial_name)
            data.append(person.tutorial_views)
        return render(request, 'index.html', {'mainuser':tutorial, 'labels':labels, 'data':data, 'user2':tutorial_views})

class NotificationView(View):
    def get(self, request):
        mainuser = MainUser.objects.get(user=request.user)
        return render(request, 'notifications.html',{'mainuser':mainuser})

class EnrolledTutorialView(View):
    def get(self, request):
        mainuser = MainUser.objects.get(user=request.user)
        enrolled = EnrolledTutorial.objects.filter(user=mainuser)
        return render(request, 'ui-cards.html',{'mainuser':mainuser,'enrolled':enrolled})

class EditProfileView(View):
    def get(self, request):
        mainuser = MainUser.objects.get(user=request.user)
        user = User.objects.get(username=mainuser)
        skill = Skill.objects.get(user=mainuser)
        return render(request, 'ui-forms.html',{'mainuser':mainuser, 'skill':skill})

    def post(self, request):
        mainuser = MainUser.objects.get(user=request.user)
        user = User.objects.get(username=mainuser)
        if request.POST['f-name']:
            mainuser.first_name = request.POST['f-name']
        if request.POST['l-name']:
            mainuser.last_name = request.POST['l-name']
        if request.POST['username']:
            user.username = request.POST['username']
        if request.POST['birth-address']:
            mainuser.birth_address = request.POST['birth-address']
        if request.POST['live-address']:
            mainuser.live_address = request.POST['live-address']
        if request.POST['work']:
            mainuser.work = request.POST['work']
        if request.POST['about']:
            mainuser.about = request.POST['about']
        if request.POST.get('photo'):
            mainuser.photo = request.POST.get('photo')
        mainuser.save()
        return redirect('home')

class EditProfileSkillsView(View):
    def get(self, request):
        return render(request, 'ui-forms.html')
    
    def post(self, request):
        mainuser = MainUser.objects.get(user=request.user)
        skill = Skill.objects.get(user=mainuser)
        skill.skills = request.POST['skills']
        skill.save()
        return redirect('home')

class EnterCourse(View):
    def get(self, request, pk):
        tutorial_media = TutorialMedia.objects.filter(tutorial=pk)
        return render(request, 'course-media-files.html',{'tutorial_media':tutorial_media})