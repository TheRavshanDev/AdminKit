from django.shortcuts import render
from django.views import View
from .models import Tutorial, EnrolledTutorial
from user.models import MainUser, Skill, IT

class HomeView(View):
    def get(self, request):
        tutorials = Tutorial.objects.all()
        mainuser = MainUser.objects.get(user=request.user)
        return render(request, 'home.html',{'tutorials':tutorials, 'mainuser':mainuser})

# class CourseDetailView(View):
#     def get(self, request):
#         return render(request, '')

class ProfileView(View):
    def get(self, request):
        mainuser = MainUser.objects.get(user=request.user)
        skills = Skill.objects.get(user=mainuser)
        courses = Tutorial.objects.filter(user=mainuser)
        return render(request, 'pages-profile.html',{'mainuser':mainuser, 'courses':courses, 'skills':skills})

class AnalyticView(View):
    def get(self, request):
        return render(request, 'index.html')

class NotificationView(View):
    def get(self, request):
        return render(request, 'notifications.html')

class EnrolledTutorialView(View):
    def get(self, request):
        mainuser = MainUser.objects.get(user=request.user)
        enrolled = EnrolledTutorial.objects.filter(user=mainuser)
        return render(request, 'ui-cards.html',{'mainuser':mainuser,'enrolled':enrolled})