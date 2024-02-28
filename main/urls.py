from django.urls import path
from.views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('get-banner/', GetBanner.as_view()),
    path('get-aboutus/', GetAboutUs.as_view()),
    path('get-university/', GetUniversity.as_view()),
    path('get-faculties/', GetFaculties.as_view()),
    path('get-work/', GetWork.as_view()),
    path('get-contactus/', GetContactUs.as_view()),
    path('get-students/', GetStudents.as_view()),
    path('get-p_university/<int:pk>/', get_p_university),
    path('get-single/', GetSingle.as_view),
    path('get-assistent/', GetAssistent.as_view),
    path('get-U_cabinet/', GetU_Cabinet.as_view),
    path('search/', search, name='search'),
]