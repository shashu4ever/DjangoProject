from django.contrib import admin
from django.urls import path

from appname1.views import (
    getStudents,
    createStudent,
    updateStudent,
    deleteStudent
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('students/', getStudents),

    path('students/create/', createStudent),

    path('students/<int:stid>/update/', updateStudent),

    path('students/<int:stid>/delete/', deleteStudent),
]
