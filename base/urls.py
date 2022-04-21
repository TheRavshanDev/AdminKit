from django.urls import path
from .views import HomeView, ProfileView, AnalyticView, NotificationView, EnrolledTutorialView

urlpatterns = [
    path('dashboard/',HomeView.as_view(), name='home'),
    path('profile/',ProfileView.as_view(), name='profile'),
    path('analytic/',AnalyticView.as_view(), name='analytic'),
    path('notifications/',NotificationView.as_view(), name='notifications'),
    path('tutorials/',EnrolledTutorialView.as_view(), name='tutorial'),
]