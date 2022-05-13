from ast import Add
from django.urls import path
from .views import (HomeView, ProfileView, AnalyticView, NotificationView, EnrolledTutorialView, 
                    CourseDetailView, AddEnrolledCourseView, EditProfileView, EditProfileSkillsView,)
    

urlpatterns = [
    path('dashboard/',HomeView.as_view(), name='home'),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('analytic/',AnalyticView.as_view(), name='analytic'),
    path('notifications/',NotificationView.as_view(), name='notifications'),
    path('tutorials/',EnrolledTutorialView.as_view(), name='tutorial'),
    path('tutorial/<int:pk>/',CourseDetailView.as_view(), name='tutorial-detail'),
    path('tutorial/<int:pk>/added/',AddEnrolledCourseView.as_view(), name='add-enrolled'),
    path('profile/edit/',EditProfileView.as_view(), name='edit-profile'),
    path('profile/edit-skills',EditProfileSkillsView.as_view(), name='edit-profile-skill'),
]