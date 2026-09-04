from django.db import models
from django.utils import timezone

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    hod_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
       return self.code + '-' +  self.name
    def students_count(self):
        return self.students.filter(is_activate=True).count()
    


class Course(models.Model):
    name=models.CharField(max_length=100)
    code=models.CharField(max_length=100,unique=True)
    department=models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='Courses',
    )
    semester=models.SmallIntegerField(default=1)
    credits=models.SmallIntegerField(default=1) 
    class Meta:
        ordering = ['semester','name']
        def __str__(self):
            return self.code + '-' + self.name 
class Student(models.Model):
    GENDER_CHOICES=[
        ('M','Male'),
        ('F','Female'),
        ('O','Other'),
    ]
    roll_no=models.CharField(max_length=20, unique=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100, unique=True)

    #blank=True -> the FORM allow it to be empty
    #null=True -> the DATABASE allow itto be empty
    phone=models.CharField(max_length=15, blank=True)
    date_of_birth=models.DateField(null=True, blank=True)

    gender= models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    #PROJECT = you cannot delete a department that still has students.
    department=models.ForeignKey(
        Department,
        on_delete=models.PROTECT,
        related_name='students',
    )
    year_of_study=models.PositiveSmallIntegerField(default=1)
    address=models.TextField(blank=True)
    photo=models.ImageField(upload_to='student_photos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    admitted_on=models.DateField(default=timezone.now)
    #Django fills this in automatically when the row iscreated.
    created_at= models.DateTimeField(auto_now_add=True) 
    class Meta:
        ordering= ['roll_no']     
    def __str__(self):
        return self.roll_no + '-' + self.full_name()
    def full_name(self):
        return self.first_name + ' ' + self.last_name        