from django.shortcuts import render
from django.http import HttpResponse
from child.models import *
# Create your views here.


def home(request):
    """help"""
    branches = Branch.objects.all()
    
    context = {"branches":branches}
    return render(request, 'index.html', context)


def sem(request,pk):
    branch = Branch.objects.get(id=pk)
    semesters = branch.semesters.all()
    return render(request, 'semester.html',{"semesters":semesters})


def sub(request,pk):
    subjects = Semester.objects.get(id=pk).subjects.all()
    return render(request,'subject.html',{"subjects":subjects})

def lecture(request, pk):
    course = Course.objects.get(id=pk)
    return render(request,'lecture.html', {"course":course})


def video(request, pk):
    course = Course.objects.get(id=pk)
    return render(request,'lecture_video.html', {"course":course})

def course_pdf(request, pk):
    course = Course.objects.get(id=pk)
    return render(request,'pdf.html', {"course":course})


def quest(request, pk):
    course = Course.objects.get(id=pk)
    return render(request,'quest_pdf.html', {"course":course})