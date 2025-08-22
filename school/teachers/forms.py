# teachers/forms.py
from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['f_name', 'l_name', 'age', 'subject', 'years_of_experience', 'is_active']
        
        # إضافة widgets لتطبيق فئات Bootstrap CSS وعناصر التحكم المخصصة
        widgets = {
            'f_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل الاسم الأول'}),
            'l_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل اسم العائلة'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل العمر'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل المادة التي يدرسها'}),
            'years_of_experience': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'أدخل سنوات الخبرة'}),
            'is_active': forms.Select(attrs={'class': 'form-select'}, choices=[(True, 'نعم، نشط'), (False, 'لا، غير نشط')]),
        }
        
        # إضافة labels مخصصة إذا كنت لا تريد استخدام verbose_name من النموذج
        labels = {
            'f_name': 'الاسم الأول للمعلم',
            'l_name': 'اسم العائلة للمعلم',
            # ... وهكذا لبقية الحقول إذا أردت تسميات مختلفة عن النموذج
        }