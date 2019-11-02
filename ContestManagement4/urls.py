"""ContestManagement4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path("accounts/", include('django.contrib.auth.urls')),
    
    path('bantochuc/', views.ban_to_chuc, name='bantochuc'),
    path('manager/', views.account_management, name='account_management'),
    path('manager/add_account/', views.add_account, name='add_account'),
    path('manager/create_account/', views.create_account, name="create_account"),
    #path('manager/edit/<char:user_username>', views.edit_account, name="edit_account"),


    path('organizer/', views.participants_management, name='participants_management'),
    path('organizer/add_participant/', views.add_participant, name='add_participant'),
    path('organizer/create_participent/', views.create_participant, name="create_participant"),
    path('organizer/del_participant/<int:my_id>/', views.del_participant, name='del_participant'),
    path('organizer/edit_participant/<int:my_id>/', views.edit_participant, name='edit_participant'),
    path('organizer/update_participant/<int:my_id>', views.update_participant, name="update_participant"),

    path('organizer/all_request/', views.all_request, name='all_request'),
    path('organizer/detail_request_from_participant.html/<int:cp_id>/', views.detail_request_from_participant, name='detail_request_from_participant'),
    path('organizer/accept_request/<int:cp_id>/', views.accept_request, name='accept_request'),
    path('organizer/reject_request/<int:cp_id>/', views.reject_request, name='reject_request'),

    path('organizer/all_request_accepted/', views.all_request_accepted, name='all_request_accepted'),
    path('organizer/detail_list_student/<int:participant_id>/', views.detail_list_student, name="detail_list_student"),
    path('organizer/detail_list_student/<int:participant_id>/accept/<int:student_id>', views.accept_student_request, name='accept_student_request'),
    path('organizer/detail_list_student/<int:participant_id>/reject/<int:student_id>', views.reject_student_request, name='reject_student_request'),


    path('subject/', views.subject_management, name='subject_management'),
    path('subject/add_subject/', views.add_subject, name='add_subject'),
    path('subject/create_subject/', views.create_subject, name='create_subject'),
    path('subject/del_subject/<int:my_id>/', views.del_subject, name="del_subject"),
    path('subject/edit_subject/<int:my_id>/', views.edit_subject, name='edit_subject'),
    path('subject/update_subject/<int:my_id>', views.update_subject, name='update_subject'),



    path('contest/', views.contest_management, name='contest_management'),
    path('contest/add_contest/', views.add_contest, name='add_contest'),
    path('contest/create_contest/', views.create_contest, name='create_contest'),
    path('contest/del_contest/<int:my_id>/', views.del_contest, name='del_contest'),
    path('contest/edit_contest/<int:my_id>/', views.edit_contest, name='edit_contest'),
    path('contest/update_contest/<int:my_id>/', views.update_contest, name='update_contest'),
    path('contest/read_contest/<int:my_id>/', views.read_contest, name='read_contest'),



    path('participant/request_join/', views.request_join, name='request_join'),
    path('participant/detail_request/<int:contest_id>', views.detail_request, name='detail_request'),
    path('participant/send_request/<int:contest_id>/', views.send_request, name='send_request'),

    path('participant/list_student_request/', views.all_students, name='list_student_request'),
    path('participant/add_student/', views.add_student, name='add_student'),
    path('participant/create_student/', views.create_student, name='create_student'),
    path('participant/edit_student/<int:student_id>/', views.edit_student, name='edit_student'),
    path('participant/update_student/<int:student_id>/', views.update_student, name='update_student'),
    path('participant/list_student_request/del_student/<int:student_id>/', views.del_student, name='del_student'),



    path('participant/school/shool_management/', views.school_management, name='school_management'),
    path('participant/school/add_school/', views.add_school, name='add_school'),
    path('participant/school/create_school/', views.create_school, name='create_school'),
    path('participant/school/edit_school/<int:school_id>/', views.edit_school, name='edit_school'),
    path('participant/school/update_school/<int:school_id>/', views.update_school, name='update_school'),
    path('participant/school/shool_management/del_school/<int:school_id>/', views.del_school, name='del_school'),


]
