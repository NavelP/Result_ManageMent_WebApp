from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib import messages


# definition for login


def login(request):
    if request.method == 'POST':
        reg_no_login = request.POST['reg_no']
        password_login = request.POST['password']

        if Student.objects.filter(reg_no=reg_no_login, password=password_login).exists():
            return redirect('student')
        else:
            return redirect('login')

    context = {
        'title': "Login In"
    }

    return render(request, 'ResultManagementApp/user/sign_up_login.html', context)


# definition for sign up


def signup(request):
    # getting data from the form
    if request.method == 'POST':
        reg_no_signup = request.POST['reg_no']
        password_signup = request.POST['password']

        # course = request.POST['course']

        if reg_no_signup != " " and password_signup != " ":
            new_user = Student(reg_no=reg_no_signup, password=password_signup)
            new_user.save()

            messages.success(request, "Account created Successfully!")
            return redirect('login')

        else:
            messages.success(request, "Failed to create Account")

    context = {
        'title': "Sign Up"
    }

    return render(request, 'ResultManagementApp/user/sign_up_login.html', context)


# definition for the admin panel


def admin(request):
    context = {
        'title': "Staff"
    }
    return redirect('upload_results', reg_no='#', action='#')


# global variables that need to be accessed by more than one function definition
entry_to_update = ""
student_results_data = {}
student_unit_details = {'faculty': "", 'school': "", 'department': "",
                        'course': "", 'year': "", 'term': "", 'unit_name': ""}


# definition for uploading the results


def upload_results(request, reg_no, action):
    global entry_to_update
    global student_results_data

    # setting the page title

    title = ''

    if action == '#':
        title = 'Upload Results'
    elif action == 'manage':
        title = 'manage'
    elif action == 'view':
        title = 'view'

    add_faculty_form = AddFaculty(request.POST or None)
    add_exam_entry_form = AddExamEntry(request.POST or None)

    faculties = Faculty.objects.filter()
    schools = ""
    departments = ""
    courses = ""
    years = ""
    terms = ""
    units = ""
    # fetching the list of schools that belong to the selected faculty

    if student_unit_details['faculty'] != '':
        schools = School.objects.filter(faculty__name=student_unit_details['faculty'])

    #   fetching the list of departments in that school

    if student_unit_details['school'] != '':
        departments = Department.objects.filter(school__name=student_unit_details['school'])

    # fetching the list of courses in that department

    if student_unit_details['department'] != '':
        courses = Course.objects.filter(department__name=student_unit_details['department'])

    # fetching the list of courses in that department

    if student_unit_details['course'] != '':
        years = {'Year 1': "Year 1", 'Year 2': "Year 2", 'Year 3': "Year 3", 'Year 4': "Year 4", 'Year5': "Year 5"}

    # fetching the list of courses in that department

    if student_unit_details['year'] != '':
        terms = {'Term 1': "Term 1", 'Term 2': "Term 2", 'Term 3': "Term 3", 'Term 4': "Term 4"}

    # fetching the list of units in the selected term and year of study

    if student_unit_details['term'] != '':
        units = Unit.objects.filter(course__name=student_unit_details['course'], year=student_unit_details['year'],
                                    term=student_unit_details['term'])

    # fetch table results
    all_results = ExamEntry.objects.filter()

    # fetching the values of the selected table row
    if reg_no != '#':
        reg_no = reg_no.replace('_', '/')
        entry_to_update = all_results.get(reg_no=reg_no)

        student_results_data = {
            'Reg no': entry_to_update.reg_no,
            'Unit': entry_to_update.unit,
            'Cat one': entry_to_update.cat_one,
            'Cat two': entry_to_update.cat_two,
            'Main exam': entry_to_update.main_exam,
            'Grade': entry_to_update.grade
        }

    else:
        student_results_data = {}

    # submit new exam entry
    if request.method == 'POST':
        if ExamEntry.objects.filter(reg_no=request.POST['Reg no']).exists() and reg_no == "#":
            pass
        else:
            reg_no_form = request.POST['Reg no']
            unit = student_unit_details['unit_name']
            cat_one = request.POST['Cat one']
            cat_two = request.POST['Cat two']
            main_exam = request.POST['Main exam']
            grade = request.POST['Grade']

            # in the case where the field is being updated
            if reg_no != "#":
                entry_to_update.reg_no = reg_no_form
                entry_to_update.unit = unit
                entry_to_update.cat_one = cat_one
                entry_to_update.cat_two = cat_two
                entry_to_update.main_exam = main_exam
                entry_to_update.grade = grade
                entry_to_update.save()
            else:
                new_exam_entry = ExamEntry(reg_no=reg_no_form, unit=unit, cat_one=cat_one, cat_two=cat_two,
                                           main_exam=main_exam,
                                           grade=grade)
                new_exam_entry.save()

    context = {
        'add_faculty_form': add_faculty_form,
        'title': title,
        'page_description': "This page deals with the uploading of students' results of all schools from all the "
                            "faculties ",

        'faculties': faculties,
        'exam_entry_form': add_exam_entry_form,
        'results_in_the_inputted_unit': all_results,
        'student_to_update_data': student_results_data,
        'student_unit_details': student_unit_details,
        'schools': schools,
        'departments': departments,
        'courses': courses,
        'years': years,
        'terms': terms,
        'units': units,
        'action': action
    }

    return render(request, 'ResultManagementApp/admin/record_management_base.html', context)


# definition to delete an exam entry


def delete_exam_entry(request, reg_no):
    if reg_no != ' ':
        reg_no = reg_no.replace('_', '/')
        ExamEntry.objects.filter(reg_no=reg_no).delete()

    return redirect('upload_results', reg_no='#', action='#')


# definition for the student page

def student(request):
    context = {
        'title': "Student"
    }
    return render(request, 'ResultManagementApp/user/student_base.html', context)


# definition for choosing unit details


def unit_details(request, action):
    global student_unit_details

    if request.method == 'POST':
        selected_faculty = request.POST.get('faculty', '')
        selected_school = request.POST.get('school', '')
        selected_department = request.POST.get('department', '')
        selected_course = request.POST.get('course', '')
        selected_year = request.POST.get('year', '')
        selected_term = request.POST.get('term', '')
        selected_unit = request.POST.get('unit', '')

        # setting the value of the selected faculty

        if selected_faculty != "":
            student_unit_details.update({'faculty': selected_faculty})

        # setting the value of the selected school

        if selected_school != "":
            student_unit_details.update({'school': selected_school})

        # setting the value of the selected department

        if selected_department != "":
            student_unit_details.update({'department': selected_department})

        # setting the value of the selected course

        if selected_course != "":
            student_unit_details.update({'course': selected_course})

        # setting the value of the selected year

        if selected_year != "":
            student_unit_details.update({'year': selected_year})

        # setting the value of the selected term

        if selected_term != "":
            student_unit_details.update({'term': selected_term})

        # setting the value of the selected unit

        if selected_unit != "":
            student_unit_details.update({'unit_name': selected_unit})

    return redirect('upload_results', reg_no='#', action=action)


# definition of  the view to manage the results


def manage_results(request):
    context = {
        'title': "manage results"
    }
    return render(request, 'ResultManagementApp/admin/manage_results.html', context)
