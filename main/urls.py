from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import students_list, edit_student, create_student, student_detail

urlpatterns = [
    path('', students_list, name='students_list'),
    path('student_detail/<int:student_id>/', student_detail, name='student_detail'),
    path('edit_student/<int:student_id>/', edit_student, name='edit_student'),
    path('create_student/', create_student, name='create_student'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

