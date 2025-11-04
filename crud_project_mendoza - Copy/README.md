# Students CRUD - Django skeleton

Project created for a midterm exam.

- Author: Mendoza, Jeff Mclaine BSIT 2-4
- Project: crud_project
- App: students
- Uses Django generic class-based views for CRUD:
  - ListView, DetailView, CreateView, UpdateView, DeleteView

How to run (basic):
1. Create a virtualenv, install Django:
   ```
   python -m venv venv
   source venv/bin/activate    # or venv\Scripts\activate on Windows
   pip install django
   ```
2. From project root:
   ```
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver
   ```
3. Open http://127.0.0.1:8000/ to view the students list.

Notes:
- This is a minimal skeleton intended for learning and grading.
- Add `SECRET_KEY` rotation and DEBUG=False for production.
