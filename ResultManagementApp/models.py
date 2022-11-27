from django.db import models


# class to define a faculty


class Faculty(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


# class to define a school


class School(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class to define a department


class Department(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# definition for a single course


class Course(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# definition for a single unit


class Unit(models.Model):
    TERMS = (
        ("Term 1", "Term 1"),
        ("Term 2", "Term 2"),
        ("Term 3", "Term 3"),
        ("Term 4", "Term 4")
    )

    YEARS = (
        ("Year 1", "Year 1"),
        ("Year 2", "Year 2"),
        ("Year 3", "Year 3"),
        ("Year 4", "Year 4"),
        ("Year 5", "Year 5"),
        ("Year 6", "Year 6"),
    )
    name = models.CharField(max_length=100, blank=False, null=False)
    course = models.ManyToManyField(Course)
    term = models.CharField(choices=TERMS, max_length=30, blank=False, null=False)
    year = models.CharField(choices=YEARS, max_length=30, blank=False, null=False)

    def __str__(self):
        return self.name


# class definition for a single result input


class ExamEntry(models.Model):
    reg_no = models.CharField(max_length=100, blank=False, null=False)
    unit = models.CharField(max_length=100, blank=False, null=False)
    cat_one = models.IntegerField(null=True)
    cat_two = models.IntegerField(null=True)
    main_exam = models.IntegerField(null=True)
    grade = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.reg_no


# definition for the lecturer
class Lecturer(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    pf_number = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.pf_number


class Student(models.Model):
    reg_no = models.CharField(max_length=20, blank=False, null=False)
    password = models.CharField(max_length=15, blank=False, null=False)
    course = models.ForeignKey(Course, max_length=100, blank=True, null=True, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, max_length=100, blank=True, null=True, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, max_length=100, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.reg_no
