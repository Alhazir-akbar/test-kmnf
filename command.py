from django.contrib.auth.models import User
from course.models import Course, UserCourse


users = [
    ('Andi', 'andi@andi.com', '12345'),
    ('Budi', 'budi@budi.com', '67890'),
    ('Caca', 'caca@caca.com', 'abcde'),
    ('Deni', 'deni@deni.com', 'fghij'),
    ('Euis', 'euis@euis.com', 'klmno'),
    ('Fafa', 'fafa@fafa.com', 'pqrst'),
]
for username, email, password in users:
    User.objects.create_user(username=username, email=email, password=password)
    
    
courses = [
    ('C++', 'Ari', 'Dr.'),
    ('C#', 'Ari', 'Dr.'),
    ('C#', 'Ari', 'Dr.'),
    ('CSS', 'Cania', 'S.Kom'),
    ('HTML', 'Cania', 'S.Kom'),
    ('Javascript', 'Cania', 'S.Kom'),
    ('Python', 'Barry', 'S.T.'),
    ('Micropython', 'Barry', 'S.T.'),
    ('Java', 'Darren', 'M.T.'),
    ('Ruby', 'Darren', 'M.T.'),
]
for course_name, mentor_name, title in courses:
    Course.objects.create(course=course_name, mentor=mentor_name, title=title)
    
    
user_course_relationships = [
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (3, 7),
    (3, 8),
    (3, 9),
    (4, 1),
    (4, 3),
    (4, 5),
    (5, 2),
    (5, 4),
    (5, 6),
    (6, 7),
    (6, 8),
    (6, 9),
]
for user_id, course_id in user_course_relationships:
    user = User.objects.get(id=user_id)
    course = Course.objects.get(id=course_id)
    UserCourse.objects.create(user=user, course=course)




###
new_password = '1'  
users = User.objects.all()
for user in users:
    user.set_password(new_password)
    user.save()
