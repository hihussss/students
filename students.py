class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_attached = []
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades1:
                lecturer.grades1[course] += [grade]
            else:
                lecturer.grades1[course] = [grade]
        else:
            return 'Ошибка'
    def mean_rate1(self):
        for lang,grad in self.grades.items():
            grad_i = [int(i) for i in grad]   
            mean = sum(grad_i)/len(grad_i)  
            return mean
            
    def __str__(self):
        res = (f"\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.mean_rate1():.1f}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершённые курсы: {self.finished_courses}")
        return res

    def __lt__(self,other):
        if not isinstance(other,Student): 
            print("Нет Лектора")
            return   
        elif self.mean_rate1() > other.mean_rate1():
            return (f"оценка {self.name} больше {other.name}")
        elif self.mean_rate1() < other.mean_rate1():
            return (f"оценка {self.name} меньше {other.name}") 
        else:
            return "Оценки равны" 
              
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
   
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades1 = {}
    
    def mean_rate(self):
        for lang,grad in self.grades1.items():
            grad_i = [int(i) for i in grad]   
            mean = sum(grad_i)/len(grad_i)  
        return mean 
    def __str__(self):
        res = (f"\nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.mean_rate():.1f}")
        return res
    def __lt__(self,other):
        if not isinstance(other,Lecturer): 
            print("Нет Лектора")
            return   
        elif self.mean_rate() > other.mean_rate():
            return (f"оценка {self.name} больше {other.name}")
        elif self.mean_rate() < other.mean_rate():
            return (f"оценка {self.name} меньше {other.name}") 
        else:
            return "Оценки равны"    
class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = (f"\nИмя: {self.name}\nФамилия: {self.surname}")
        return res

lt_mean = []
def calc_mean_allstudents(students,coursess):
    for i in students:
        for kurs,grade in i.grades.items():
            if kurs == coursess:
                for p in grade:
                    lt_mean.append(int(p))
            else:
                continue     
    calc_mean = sum(lt_mean)/len(lt_mean)   
    return f"Cредняя оценка за домашнее задание по всем студентам в рамках конкретного курса  {calc_mean:.1f}"     
l_mean = []
def calc_mean_alllectors(lectors,coursess):
    for i in lectors:
        for kurs,grade in i.grades1.items():
           if kurs == coursess:
                for p in grade:
                    l_mean.append(int(p))
           else:
                continue    
    calc_mean = sum(l_mean)/len(l_mean)   
    return f"Cредняя оценка за лекции по всем лекторам в рамках конкретного курса  {calc_mean:.1f}"         
    
lector1 = Lecturer('Morty', 'Lebovskiy')
lector1.courses_attached += ['Python'] 
lector1.courses_attached += ['Java']

lector2 = Lecturer('Zmey', 'Gorinich')
lector2.courses_attached += ['Python']
lector2.courses_attached += ['Java']

student1 = Student('Ruoy', 'Eman', 'men')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Java']
student1.finished_courses += ['Введение в программирование']

student2 = Student('Rick', 'Gonsales', 'men')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']
student2.finished_courses += ['Введение в программирование']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python']
reviewer1.courses_attached += ['Java']

reviewer2 = Reviewer('Mishon', 'Graims')
reviewer2.courses_attached += ['Python']
reviewer2.courses_attached += ['Java']

students = [student1,student2]
lectors = [lector1,lector2] 

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 10)

reviewer1.rate_hw(student1, 'Java', 9)
reviewer1.rate_hw(student1, 'Java', 9)
reviewer1.rate_hw(student1, 'Java', 6)

reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Python', 8)

reviewer2.rate_hw(student2, 'Java', 10)
reviewer2.rate_hw(student2, 'Java', 9)
reviewer2.rate_hw(student2, 'Java', 8)

student2.rate_lect(lector1, 'Python', 10)
student2.rate_lect(lector1, 'Python', 9)
student2.rate_lect(lector1, 'Python', 10) 

student1.rate_lect(lector2, 'Python', 10)
student1.rate_lect(lector2, 'Python', 10)
student1.rate_lect(lector2, 'Python', 10) 

print(student1.grades)
print(student2.grades)
print(student1.__lt__(student2))
print(lector1.__lt__(lector2))
print(student1)
print(student2)
print(lector1)
print(lector2)
print(reviewer1)
print(reviewer2)

print(calc_mean_allstudents(students,"Java"))
print(calc_mean_alllectors(lectors,"Python"))