from django.db import models




class Banner(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # menu = models.



class AboutUs(models.Model):
    icon = models.ImageField()
    number = models.CharField(max_length=100)
    text = models.TextField()
    


class University(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    rating = models.CharField(max_length=100)
    quality = models.IntegerField()
    price = models.CharField(max_length=100)
    rating = models.IntegerField()
    


class Faculties(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField()
    rating = models.IntegerField()



class Work(models.Model):
    title = models.CharField(max_length=100)
    icon = models.ImageField()



class Students(models.Model):
    name = models.CharField(max_length=100)
    direction = models.CharField(max_length=100)
    description = models.TextField()



class ContactUs(models.Model):
    phone = models.CharField(max_length=100 ,unique=True)



class Personal(models.Model):
    photo = models.ImageField()
    students = models.ForeignKey(Students, on_delete=models.CASCADE)
    passport = models.URLField()
    degree = models.URLField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    faculties = models.ForeignKey(Faculties, on_delete=models.CASCADE)



class Single(models.Model):
    title = models.CharField(max_length=100)
    waiting = models.CharField(max_length=100)


class P_University(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    date = models.DateField()
    single = models.ForeignKey(Single, on_delete=models.CASCADE) 
    status = models.IntegerField(choices=(
        (1, 'Прием документов'),
        (2, 'прием закрыт'),
    ))



class Assistent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone = models.CharField(max_length=100, unique=True)
    email = models.EmailField()



class Statistics(models.Model):
    univ = models.ForeignKey(University , on_delete=models.CASCADE)
    students = models.IntegerField()
    invoices = models.IntegerField()
    accepted = models.IntegerField()
    naccepted = models.IntegerField()
    male = models.IntegerField()
    female = models.IntegerField()
    langs = models.CharField(max_length=25)
    faculties = models.ForeignKey(Faculties , on_delete=models.CASCADE)
    semesters = models.CharField(max_length=25)
    payment = models.BooleanField(default=False)



class Search(models.Model):
    student = models.ForeignKey(Students , on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculties , on_delete=models.CASCADE)
    gpa = models.IntegerField()
    ielts = models.IntegerField()
    accept = models.IntegerField(choices=(
        (1, 'Да'),
        (2, 'Нет')
    ))



class University_info(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)



class U_Cabinet(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=100)
    yearfoundation = models.IntegerField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    matto = models.CharField(max_length=100)
    bachelors = models.IntegerField()
    masters = models.IntegerField()
    teachers = models.IntegerField()
    startingsalary = models.CharField(max_length=100)
    description = models.TextField()
    # mapuniver = models.URLField()


