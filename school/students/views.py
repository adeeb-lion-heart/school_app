# students/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

# الصفحة الرئيسية
def index(request):
    return render(request, "index.html")

# إنشاء طالب جديد
def create_student(request):
    if request.method == "POST":
        f_name = request.POST.get("f_name")
        l_name = request.POST.get("l_name")
        age = request.POST.get("age")
        gpa = request.POST.get("gpa")
        level = request.POST.get("level")
        # يجب تحويل قيمة status إلى Boolean (True/False)
        # إذا كانت "True" من الـ POST، تكون True، وإلا فـ False
        status = request.POST.get("status") == "True"
        report = request.POST.get("report")

        Student.objects.create(
            f_name=f_name, l_name=l_name, age=age, gpa=gpa,
            level=level, status=status, report=report
        )
        return redirect("showll") # إعادة التوجيه إلى قائمة الطلاب

    return render(request, "create_student.html")

# عرض كل الطلاب
def student_list(request):
    students = Student.objects.all()
    # يمكنك تمرير عدد الطلاب إذا أردت استخدامه في القالب بشكل مباشر (أو استخدم students.count في القالب)
    # students_count = students.count()
    return render(request, "student_list.html", {"students": students})

# عرض تفاصيل طالب واحد
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "student_detail.html", {"student": student})

# تعديل طالب موجود
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.f_name = request.POST.get("f_name")
        student.l_name = request.POST.get("l_name")
        student.age = request.POST.get("age")
        student.gpa = request.POST.get("gpa")
        student.level = request.POST.get("level")
        # تحويل قيمة status إلى Boolean
        student.status = request.POST.get("status") == "True"
        student.report = request.POST.get("report")
        student.save()
        return redirect("showll") # إعادة التوجيه إلى قائمة الطلاب بعد التعديل

    return render(request, "edit_student.html", {"student": student})

# حذف طالب
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("showll") # إعادة التوجيه إلى قائمة الطلاب بعد الحذف
    # إذا كانت طريقة الطلب GET، اعرض صفحة التأكيد
    return render(request, "delete_student.html", {"student": student})