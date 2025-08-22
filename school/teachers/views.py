# teachers/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm # استيراد النموذج الذي أنشأناه

# الصفحة الرئيسية للمعلمين
def teacher_index(request):
    return render(request, "teachers/index.html")

# إنشاء معلم جديد
def create_teacher(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save() # حفظ بيانات النموذج مباشرة في قاعدة البيانات
            return redirect("teacher_list")
    else:
        form = TeacherForm() # نموذج فارغ لطلب GET
    return render(request, "teachers/create_teacher.html", {"form": form})

# عرض كل المعلمين
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers/teacher_list.html", {"teachers": teachers})

# عرض تفاصيل معلم واحد
def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, "teachers/teacher_detail.html", {"teacher": teacher})

# تعديل معلم
def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher) # تمرير instance للتعديل
        if form.is_valid():
            form.save()
            return redirect("teacher_detail", pk=teacher.pk) # إعادة التوجيه لصفحة التفاصيل
    else:
        form = TeacherForm(instance=teacher) # نموذج مملوء ببيانات المعلم الحالي لطلب GET
    return render(request, "teachers/edit_teacher.html", {"form": form, "teacher": teacher})

# حذف معلم
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        teacher.delete()
        return redirect("teacher_list")
    return render(request, "teachers/delete_teacher.html", {"teacher": teacher})