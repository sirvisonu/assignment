student_marks= {'alice':23
                 ,'priya':56
                 ,'sima':96
                 ,'savita':34
                , 'pushpa':36
                                }
name=input("enter student name: ")
if name in student_marks:
    marks=student_marks[name]
    print(marks)
else:
    print('student is not fount')









