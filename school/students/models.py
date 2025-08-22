from django.db import models



class Student(models.Model):
    f_name = models.CharField(max_length=100)          # الاسم الأول
    l_name = models.CharField(max_length=100)          # الاسم الأخير
    age = models.IntegerField(default=18)              # العمر الافتراضي 18
    gpa = models.FloatField(default=0.0)               # المعدل الافتراضي 0.0
    level = models.CharField(max_length=50, default="1")  # المستوى الافتراضي "1"
    status = models.CharField(max_length=50, default="نشط")  # الحالة الافتراضية "نشط"
    report = models.TextField(blank=True, default="")  # التقرير ممكن يكون فاضي

    def __str__(self):
        return f"{self.f_name} {self.l_name}"

