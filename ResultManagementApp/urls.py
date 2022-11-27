from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('', views.login, name="login"),
    path('student', views.student, name="student"),
    path('staff', views.admin, name="staff"),
    path('upload/(?P<reg_no>)/(?P<action>)', views.upload_results, name='upload_results'),
    path('delete_exam_entry/(?P<reg_no>)', views.delete_exam_entry, name='delete_exam_entry'),
    path('unit_details/(?P<action>)', views.unit_details, name='unit_details'),
    path('manage_results', views.manage_results, name='manage_results')
]
