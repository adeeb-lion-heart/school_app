# teachers/models.py
from django.db import models

class Teacher(models.Model):
    f_name = models.CharField(max_length=100, verbose_name="الاسم الأول")
    l_name = models.CharField(max_length=100, verbose_name="اسم العائلة")
    age = models.IntegerField(verbose_name="العمر")
    subject = models.CharField(max_length=100, verbose_name="المادة التي يدرسها")
    years_of_experience = models.IntegerField(verbose_name="سنوات الخبرة")
    is_active = models.BooleanField(default=True, verbose_name="نشط حاليًا")

    def __str__(self):
        return f"{self.f_name} {self.l_name} ({self.subject})"

    class Meta:
        verbose_name = "معلم"
        verbose_name_plural = "معلمون"
        ordering = ['l_name', 'f_name'] # ترتيب افتراضي