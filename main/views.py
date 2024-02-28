from django.shortcuts import render, redirect
from django.db.models import Q 
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import response
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, \
     RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView, \
     RetrieveDestroyAPIView 
from.serializer import *



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                error_message = "Invalid username or password. Please try again."
                return render(request, {'error_message': error_message})
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, {'error_message': error_message})
    else:
        form = AuthenticationForm()
        return render(request, {'form': form})



class GetBanner(ListAPIView):
    queryset = Banner.objects.last()
    serializer_class = BannerSerializer



class GetAboutUs(ListAPIView):
    queryset = AboutUs.objects.last()
    serializer_class = AboutUsSerializer



class GetUniversity(ListAPIView):
    queryset = University.objects.all().order_by('-rating')[:9]
    serializer_class = UniversitySerializer



class GetFaculties(ListAPIView):
    queryset = Faculties.objects.all().order_by('-rating')[:9]
    serializer_class = FacultiesSerializer



class GetWork(ListAPIView):
    queryset = Work.objects.last()
    serializer_class = WorkSerializer



class GetContactUs(CreateAPIView):
    queryset = ContactUs.objects.last()
    serializer_class = ContactUsSerializer



class GetStudents(CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer



@api_view(['GET'])
def get_p_university(request, pk):
    puniversity = P_University.objects.all()
    serialized_data = P_UniversitySerializer(puniversity, many=True).data
    return Response(serialized_data)



class GetSingle(CreateAPIView):
    queryset = Single.objects.all()
    serializer_class = SingleSerializer



class GetAssistent(CreateAPIView):
    queryset = Assistent.objects.last()
    serializer_class = AssistentSerializer



class GetU_Cabinet(CreateAPIView):
    queryset = U_Cabinet.objects.last()
    serializer_class = U_CabinetSerializer



def search(request):
    query = request.GET.get('q', '')
    universities = University.objects.filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(rating__icontains=query) | Q(price__icontains=query))
    return render(request,{'universities': universities})



