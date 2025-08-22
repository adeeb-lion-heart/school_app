# students/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls), # لإلغاء التعليق إذا كنت تستخدم لوحة تحكم الأدمن
    path('', views.index, name="index"),
    path('add/', views.create_student, name="add"), # إضافة مهمة / طالب
    path('show/', views.student_list, name="showll"), # عرض المهام / الطلاب

    # هذه المسارات تتطلب مفتاحًا أساسيًا (pk) لتحديد الطالب
    path('edit/<int:pk>/', views.edit_student, name="edit_student"), # تعديل طالب معين
    path('showone/<int:pk>/', views.student_detail, name="showone"), # عرض تفاصيل طالب واحد
    path('delete/<int:pk>/', views.delete_student, name="delete_student"), # حذف طالب معين
]