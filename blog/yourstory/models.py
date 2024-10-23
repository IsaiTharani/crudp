from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=10)
    email=models.EmailField()
    def __str__(self):
        return self.name
class TextFile(models.Model):
    person=models.ForeignKey(Person,on_delete=models.CASCADE,related_name="text_files")
    file=models.FileField(upload_to='text/')

    def __str__(self):
        return f' Text file for {self.person.name}'