# students_management_system2
class students(models.Model):
    Id=models.CharField(max_length=10,unique=True)
    Name=models.CharField(max_length=100,blank=True)
    email=models.CharField(max_length=100,unique=True)