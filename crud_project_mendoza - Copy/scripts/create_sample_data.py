# Run this script after migrations to create sample students.
from students.models import Student

def run():
    sample = [
        {'student_id':'S2025001','first_name':'Juan','last_name':'Dela Cruz','course':'BSIT','year':2,'email':'juan@example.com'},
        {'student_id':'S2025002','first_name':'Maria','last_name':'Santos','course':'BSIT','year':1,'email':'maria@example.com'},
    ]
    for s in sample:
        Student.objects.create(**s)
    print('Sample data created.')
