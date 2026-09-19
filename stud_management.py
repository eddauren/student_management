import json
class Student:
    def __init__(self,name,age,course,grades):
        self.name=name
        self.age=age
        self.course=course
        self.grades=grades
    @classmethod
    def from_dict(cls,data):
        return cls(data['Name'],data['Age'],data['Course'],data['Grades'])

    def __str__(self):
        return (f'{self.name} | Age: {self.age} | Course: {self.course} | Average: {self.avg_grades():.2f}')
    def birthday(self):
        self.age+=1
    def add_grade(self,grade):
        self.grades.append(grade)
    def next_course(self):
        avg=self.avg_grades()
        if avg>=60:
            self.course+=1
            print(self.name,' succesfully moved to the next course')
        else:
            print(self.name,' can not move to the next course')
    def avg_grades(self):
        if not self.grades:
            return 0
        return sum(self.grades)/len(self.grades)
    def to_dict(self):
        return {'Name':self.name,'Age':self.age,'Course':self.course,'Grades':self.grades}
        
students=[]
with open('student.json','r') as f:
    data=json.load(f)
for i in data:
    students.append(Student.from_dict(i))
while True:
    action=int(input('\n1-info\n2-highest avg score\n3-everyone to the new course\n4-new grade\n5-exit\n6-json\n'))
    if action==1:
        for i in students:
            print(i)
    elif action==2:
        max_avg_stud=students[0]
        for i in students: 
            if i.avg_grades()>max_avg_stud.avg_grades():
                max_avg_stud=i
        print(max_avg_stud.name,' has highest avg score: ',max_avg_stud.avg_grades())
    elif action==3:
        for i in students:
            i.next_course()
    elif action==4:
        name,grade=input('Enter students name and new grade:').split()
        if int(grade)<0 or int(grade)>100:
            print('invalid grade')
            continue
        for i in students:
            if i.name.lower().strip()==name.lower().strip():
                i.add_grade(int(grade))
                break
        else:
            print(name,' is not found')
        
    elif action==5:
        break
    elif action==6:
        data=[]
        for student in students:
            data.append(student.to_dict())
        with open('student.json','w') as f:
            json.dump(data,f,indent=4)

    else:
        print('invalid option')