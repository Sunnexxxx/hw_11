from django.shortcuts import render, redirect
from .models import Student


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students_list.html', {'students': students})


def student_detail(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return redirect('students_list')

    return render(request, 'student_detail.html', {'student': student})


def edit_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return redirect('students_list')

    if request.method == 'POST':
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.age = request.POST.get('age')
        student.course = request.POST.get('course')
        student.instrument = request.POST.get('instrument')
        student.performance = request.POST.get('performance')
        student.payment_status = request.POST.get('payment_status') == 'on'
        student.image = request.FILES.get('image')
        student.save()
        return redirect('students_list')

    return render(request, 'edit_student.html', {'student': student})


def create_student(request):
    if request.method == 'POST':
        Student.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            age=request.POST.get('age'),
            course=request.POST.get('course'),
            instrument=request.POST.get('instrument'),
            performance=request.POST.get('performance'),
            payment_status=request.POST.get('payment_status') == 'on',
            image=request.FILES.get('image')
        )
        return redirect('students_list')

    return render(request, 'create_student.html')
