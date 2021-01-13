from django.shortcuts import render


def dashboard(request):
    context = {'title' : 'Home'}
    return render(request,'dashboard/dashboard.html')

def create_student(request):
    
    context = {'title' : "Create Student"}
    return render(request, 'dashboard/create_student.html')

def create_teacher(request):
    context = {'title' : "Create Teacher"}
    return render(request, 'dashboard/create_teacher.html')