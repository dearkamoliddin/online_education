from django.urls import path

from app.views import HomePageView, AboutView, ContactView

app_name = 'app'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
]
