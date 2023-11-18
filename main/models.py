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

    GRADES_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    course = models.CharField(max_length=255, choices=COURSES_CHOICES)
    instrument = models.CharField(max_length=255, choices=INSTRUMENT_CHOICES)
    performance = models.CharField(max_length=255, choices=GRADES_CHOICES)
    payment_status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='student_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
