from django.shortcuts import render
from .models import User, Subject, Contest, Contest_Participant, Student, School
from .forms import *
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'home.html')

def ban_to_chuc(request):
    return render(request, 'banToChuc/ban_to_chuc.html')

def account_management(request):
    all_users = User.objects.all()

    return render(request, 'sys_admin/account_management.html', {
        'all_users':all_users
    })

def add_account(request):
    all_participants = User.objects.all()


    return render(request, 'sys_admin/add_account.html', {
        'all_participants':all_participants
    })

def create_account(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = CreateAccount(request.POST)
        if form.is_valid():
            _username = form.cleaned_data['username']
            _account_type = form.cleaned_data['account_type']
            _password = form.cleaned_data['password']

            user = User(username = _username)
            if(_account_type == 'BanToChuc'):
                user.is_BanToChuc = True
            else:
                user.is_DonViDuThi = True
        
            user.set_password(_password)
            user.save()

            print("Account: " + user.username + " was created")
        else:
            
            return render(request, 'sys_admin/add_account.html', {'form':form})
    
    all_users = User.objects.all()

    return render(request, 'sys_admin/account_management.html', {
        'all_users':all_users
    })

def edit_account(request, user_username):
    pass
#     if request.method == 'POST':
#         if 
# 


### participant management ###
def participants_management(request):
    all_participants = User.objects.filter(is_DonViDuThi=True)

    return render(request, 'organizer/participants_management.html', {
        'all_participants':all_participants
    })

def add_participant(request):
    return render(request, 'organizer/add_participant.html')

def create_participant(request):
    if(request.method == 'POST'):
        form = CreateParticipant(request.POST)
        if form.is_valid():
            _participant_name = form.cleaned_data['participant_name']
            _email = form.cleaned_data['email']
            _phone_number = form.cleaned_data['phone_number']

            _username = form.cleaned_data['username']
            _password = form.cleaned_data['password']

            participant = User(name = _participant_name, email = _email, phone_number = _phone_number, username = _username)
            
            participant.set_password(_password)
            #set is_DonViDuThi
            participant.is_DonViDuThi = True
            participant.save()
            print("Paticipant " + participant.name + " was created.")
        else:
            print("Not success")
            return render(request, 'organizer/add_participant.html', {'form':form})

    all_participants = User.objects.filter(is_DonViDuThi=True)
    return render(request, 'organizer/participants_management.html', {
        'all_participants':all_participants
    })

def del_participant(request, my_id):
    User.objects.get(id=my_id).delete()

    all_participants = User.objects.filter(is_DonViDuThi=True)

    return render(request, 'organizer/participants_management.html', {
        'all_participants':all_participants
    }) 

def edit_participant(request, my_id):
    participant = User.objects.get(id = my_id)
    return render(request, 'organizer/edit_participant.html', {
        'participant':participant
    })

def update_participant(request, my_id):
    if request.method == 'POST':
        form = EditInfoParticipant(request.POST)
        if form.is_valid():
            _participant_name = form.cleaned_data['participant_name']
            _email = form.cleaned_data['email']
            _phone_number = form.cleaned_data['phone_number']

            

            User.objects.filter(id=my_id).update(name = _participant_name, email = _email, phone_number = _phone_number)


            print("Paticipant " + _participant_name + " was updated.")
        else:
            print("Not success")
            return render(request, 'organizer/edit_participant.html', {'form':form})

    all_participants = User.objects.filter(is_DonViDuThi=True)
    return render(request, 'organizer/participants_management.html', {
        'all_participants':all_participants
    })

 
 ### subject management ###
def subject_management(request):
    all_subjects = Subject.objects.all()

    return render(request, 'subject/subject_management.html', {
        'all_subjects' : all_subjects
    })

def add_subject(request):
    return render(request, 'subject/add_subject.html')

def create_subject(request):
    if request.method == 'POST':
        form = CreateSubject(request.POST)
        if form.is_valid():
            _subject_name = form.cleaned_data['subject_name']

            subject = Subject(name = _subject_name)
            subject.save()
            print("Subject " + subject.name + " was created")
        else:
            return render(request, 'subject/add_subject.html', {
                'form':form
            })
    all_subjects = Subject.objects.all()
    return render(request, 'subject/subject_management.html', {
        'all_subjects': all_subjects
    })

def del_subject(request, my_id):
    Subject.objects.get(id=my_id).delete()

    all_subjects = Subject.objects.all()

    return render(request, 'subject/subject_management.html', {
        'all_subjects':all
    })

def edit_subject(request, my_id):
    subject = Subject.objects.get(id=my_id)

    return render(request, 'subject/edit_subject.html', {
        'subject':subject
    })

def update_subject(request, my_id):
    if request.method == 'POST':
        form = CreateSubject(request.POST)
        if form.is_valid():
            subject_name = form.cleaned_data['subject_name']

            Subject.objects.filter(id=my_id).update(name = subject_name)
            print("Subject " + subject_name + " was updated.")
        else:
            print("Not success")
            return render(request, 'subject/edit_subject.html', {
                'form':form})

    all_subjects = Subject.objects.all()
    return render(request, 'subject/subject_management.html', {
        'all_subjects':all_subjects
    })



### contest management ###
def contest_management(request):
    all_contests = Contest.objects.all()

    return render(request, 'contest/contest_management.html', {
        'all_contests': all_contests
    })

def add_contest(request):
    all_subjects = Subject.objects.all()

    return render(request, 'contest/add_contest.html', {
        'all_subjects': all_subjects
    })

def create_contest(request):
    if request.method == 'POST':
        form = CreateContest(request.POST)
        if form.is_valid():
            _contest_name = form.cleaned_data['contest_name']
            _day_start = form.cleaned_data['day_start']
            _day_end = form.cleaned_data['day_end']
            _subjects = request.POST.getlist('subject')

            contest = Contest(name = _contest_name, day_start = _day_start, day_end = _day_end)
            contest.save()
            
            for subject in _subjects:
                contest.subjects.add(Subject.objects.get(name=subject))
                
            contest.save()


            print(contest.name)
        else:
            return render(request, 'contest/add_contest.html', {
                'form':form
            })
    
    all_contests = Contest.objects.all()
    return render(request, 'contest/contest_management.html', {
        'all_contests': all_contests
    })

def del_contest(request, my_id):
    Contest.objects.get(id=my_id).delete()

    all_contest = Contest.objects.all()

    return render(request, 'contest/contest_management.html', {
        'all_contests': all_contest
    })

def edit_contest(request, my_id):
    contest = Contest.objects.get(id=my_id)

    subjects_in_contest = contest.subjects.all()
    print(subjects_in_contest)

    all_subjects = Subject.objects.all()
    print(all_subjects)

    return render(request, 'contest/edit_contest.html', {
        'contest':contest,
        'subjects_in_contest':subjects_in_contest,
        'all_subjects': all_subjects,
    })

def update_contest(request, my_id):
    if request.method == 'POST':
        form = CreateContest(request.POST)
        if form.is_valid():
            _contest_name = form.cleaned_data['contest_name']
            _day_start = form.cleaned_data['day_start']
            _day_end = form.cleaned_data['day_end']
            _subjects = request.POST.getlist('subject')

            print( _subjects)

            Contest.objects.filter(id=my_id).update(name = _contest_name, day_start = _day_start, day_end = _day_end)
            
            contest = Contest.objects.get(id=my_id)
            contest.subjects.clear()
            for subject in _subjects:
                contest.subjects.add(Subject.objects.get(name=subject))

            contest.save()
            print(contest.subjects)
        else:
            return render(request, 'contest/add_contest.html', {
                'form':form
            })
    
    all_contests = Contest.objects.all()
    return render(request, 'contest/contest_management.html', {
        'all_contests': all_contests
    })

def read_contest(request, my_id):
    contest = Contest.objects.get(id=my_id)

    subjects_in_contest = contest.subjects.all()
    print(subjects_in_contest)

    all_subjects = Subject.objects.all()
    print(all_subjects)

    return render(request, 'contest/read_contest.html', {
        'contest':contest,
        'subjects_in_contest':subjects_in_contest,
        'all_subjects': all_subjects,
    })

def all_request(request):
    all_contest_participant = Contest_Participant.objects.all()

    # all_contest = all_contest_participant.contest.all()
    # all_participant = all_contest_participant.participant.all()


    return render(request, 'organizer/all_request.html',{
        'all_contest_participant': all_contest_participant
    })

def detail_request_from_participant(request, cp_id):
    cp = Contest_Participant.objects.get(id=cp_id)
    
    subjects_in_cp = cp.subjects.all()
    subjects_in_c = Contest.objects.get(id=cp.contest.id).subjects.all()

    return render(request, 'organizer/detail_request_from_participant.html',{
        'cp': cp,
        'subjects_in_cp': subjects_in_cp,
        'subjects_in_c' : subjects_in_c
    })

def accept_request(request, cp_id):
    Contest_Participant.objects.filter(id = cp_id).update(status='accepted')
    

    all_contest_participant = Contest_Participant.objects.all()


    return render(request, 'organizer/all_request.html',{
        'all_contest_participant': all_contest_participant
    })

def reject_request(request, cp_id):
    Contest_Participant.objects.filter(id = cp_id).update(status='rejected')
    

    all_contest_participant = Contest_Participant.objects.all()


    return render(request, 'organizer/all_request.html',{
        'all_contest_participant': all_contest_participant
    })

        ## list student ##
def all_request_accepted(request):
    all_contest_participant = Contest_Participant.objects.filter(status='accepted') # all participent was accepted

    return render(request, 'organizer/all_request_accepted.html',{
        'all_contest_participant': all_contest_participant
    })

def detail_list_student(request, participant_id):
    all_students = Student.objects.filter(participant = User.objects.get(id=participant_id))

    participant = User.objects.get(id=participant_id)
    return render(request, 'organizer/detail_list_student.html', {
        'all_students': all_students,
        'participant':participant
    })

def accept_student_request(request, participant_id, student_id):
    Student.objects.filter(id=student_id).update(status= 'accepted')

    all_students = Student.objects.filter(participant = User.objects.get(id=participant_id))

    participant = User.objects.get(id=participant_id)
    return render(request, 'organizer/detail_list_student.html', {
        'all_students': all_students,
        'participant':participant
    })

def reject_student_request(request, participant_id, student_id):
    Student.objects.filter(id=student_id).update(status= 'rejected')

    all_students = Student.objects.filter(participant = User.objects.get(id=participant_id))

    participant = User.objects.get(id=participant_id)
    return render(request, 'organizer/detail_list_student.html', {
        'all_students': all_students,
        'participant':participant
    })


### Participant working ### 

def request_join(request):
    all_contests = Contest.objects.all()
    return render(request, 'participant/request_join.html', {
        'all_contests':all_contests
    })


def detail_request(request, contest_id):
    contest = Contest.objects.get(id = contest_id)
    subjects = contest.subjects.all()

    return render(request, 'participant/send_request_join.html', {
        'contest':contest,
        'subjects':subjects
    })

def send_request(request, contest_id):

    _subjects = request.POST.getlist('subject')


    contest_participant = Contest_Participant()
    contest_participant.save()

    contest_participant.contest = Contest.objects.get(id = contest_id)
    contest_participant.participant = User.objects.get(id = request.user.id)

    for subject in _subjects:
        contest_participant.subjects.add(Subject.objects.get(name=subject))

    contest_participant.save()

    #contest_participant.save()
    print("Dang ki tham gia thi thanh cong")
    return render(request, 'home.html')

### student working space ###

def all_students(request):
    all_students = Student.objects.filter(participant = request.user.id)

    

    return render(request, 'participant/send_list_student.html', {
        'all_students':all_students
    })

def add_student(request):
    all_schools = School.objects.filter(participant = request.user.id)
    cp = Contest_Participant.objects.get(participant= request.user.id)
    subject_in_c = cp.subjects.all()
    return render(request, 'participant/add_student.html',{
        'all_schools':all_schools,
        'subjects_in_c':subject_in_c
    })    

def create_student(request):
    if request.method == 'POST':
        form = CreateStudent(request.POST)
        if form.is_valid():
            _name = form.cleaned_data['name']
            _birthday = form.cleaned_data['birthday']
            _gender = form.cleaned_data['gender']
            _identity_number = form.cleaned_data['identity_number']
            _phone_number = form.cleaned_data['phone_number']

            _school_id = request.POST['school']
            _subject_id = request.POST['subject']

            

            student = Student(name = _name, birthday = _birthday, gender = _gender, identity_number = _identity_number, phone_numer = _phone_number)

            student.school = School.objects.get(id=_school_id)
            student.subject = Subject.objects.get(id=_subject_id)

            student.participant = User.objects.get(id = request.user.id)

            student.save()        
            
            print(student)
            
        else:
            return render(request, 'participant/add_student.html', {
                'form':form
            })
    
    all_students = Student.objects.filter(participant = request.user.id)

    return render(request, 'participant/send_list_student.html', {
        'all_students':all_students
    })

def edit_student(request, student_id):
    student = Student.objects.get(id = student_id)

    return render(request, 'participant/edit_student.html', {
        'student': student
    })

def update_student(request, student_id):
    if request.method == 'POST':
        form = CreateStudent(request.POST)
        if form.is_valid():
            _name = form.cleaned_data['name']
            _birthday = form.cleaned_data['birthday']
            _gender = form.cleaned_data['gender']
            _school = form.cleaned_data['school']
            _phone_number = form.cleaned_data['phone_number']
            _subject = form.cleaned_data['subject']
            
            Student.objects.filter(id=student_id).update(name = _name, birthday = _birthday, gender = _gender, school = _school, phone_numer = _phone_number, subject_test = _subject)
            
        else:
            return render(request, 'participant/add_student.html', {
                'form':form
            })
    
    all_students = Student.objects.filter(participant = request.user.id)

    return render(request, 'participant/send_list_student.html', {
        'all_students':all_students
    })  

def del_student(request, student_id):
    Student.objects.get(id = student_id).delete()

    all_students = Student.objects.filter(participant = request.user.id)

    return render(request, 'participant/send_list_student.html', {
        'all_students':all_students
    })



#### School working space #####

def school_management(request):
    all_schools = School.objects.filter(participant_id = request.user.id)

    return render(request, 'school/school_management.html', {
        'all_schools':all_schools
    })

def add_school(request):
    return render(request, 'school/add_school.html')

def create_school(request):
    if request.method == 'POST':
        form = CreateSchool(request.POST)
        if form.is_valid():
            _name = form.cleaned_data['name']
            _address = form.cleaned_data['address']
            _website = form.cleaned_data['website']
            _email = form.cleaned_data['email']
            _phone_number = form.cleaned_data['phone_number']

            school = School(name = _name, address = _address, website = _website, email = _email, phone_number = _phone_number, participant = request.user)
            school.save()

            print("School: " + school.name + " was created")
        else:
            return render(request, 'school/add_school.html', {'form':form})
    
    all_schools = School.objects.filter(participant_id = request.user.id)

    return render(request, 'school/school_management.html', {
        'all_schools':all_schools
    })    

def edit_school(request, school_id):
    school = School.objects.get(id = school_id)
    return render(request, 'school/edit_school.html', {
        'school':school
    })

def update_school(request, school_id):
    if request.method == 'POST':
        form = CreateSchool(request.POST)   
        if form.is_valid():
            _name = form.cleaned_data['name']
            _address = form.cleaned_data['address']
            _website = form.cleaned_data['website']
            _email = form.cleaned_data['email']
            _phone_number = form.cleaned_data['phone_number']

            School.objects.filter(id=school_id).update(name = _name, address = _address, website = _website, email = _email, phone_number = _phone_number)

        else:
            return render(request, 'school/edit_school.html', {'form':form})
    
    all_schools = School.objects.filter(participant_id = request.user.id)

    return render(request, 'school/school_management.html', {
        'all_schools':all_schools
    })  

def del_school(request, school_id):
    School.objects.get(id = school_id).delete()

    all_schools = School.objects.filter(participant_id = request.user.id)

    return render(request, 'school/school_management.html', {
        'all_schools':all_schools
    }) 

      









