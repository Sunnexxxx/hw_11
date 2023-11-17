from django.db import models


class Student(models.Model):
    COURSES_CHOICES = [
        ('1', '1-й курс'),
        ('2', '2-й курс'),
        ('3', '3-й курс'),
    ]

    INSTRUMENT_CHOICES = [
        ('piano', 'Пианино'),
        ('guitar', 'Гитара'),
        ('violin', 'Скрипка'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=2, choices=COURSES_CHOICES)
    instrument = models.CharField(max_length=10, choices=INSTRUMENT_CHOICES)
    performance = models.IntegerField(default=1, help_text='От 1 до 12')
    payment_status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
