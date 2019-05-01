from django.urls import path
from . import views
from chambray.decorators import check_recaptcha


urlpatterns = [
    path('', check_recaptcha(views.ContactCreateView.as_view()), name='create'),
    path(r'thankyou/<str:sender>/', views.ThankyouView.as_view(), name='thankyou')
]