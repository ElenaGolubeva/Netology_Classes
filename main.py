class Student:
    items = []

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.items.append(self)

    def rate_lec(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        sum_ = 0
        k = 0
        if len(self.grades) == 0:
            return 0
        for i in self.grades:
            sum_ += sum(self.grades.get(i))/len(self.grades[i])
            k += 1
        return sum_/k

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {'%.1f'%(self.average_grade())} \nКурсы в процессе изучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_courses}"

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Not a Student")
            return
        return self.average_grade() > other.average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
    items = []

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        self.items.append(self)

    def average_grade(self):
        sum_ = 0
        k = 0
        if len(self.grades) == 0:
            return 0
        for i in self.grades:
            sum_ += sum(self.grades.get(i)) / len(self.grades[i])
            k +=1
        return sum_ / k

    def __str__(self):
        return f'Имя: {self.name}  \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecture):
            print("Not a Lecture")
            return
        return self.average_grade() > other.average_grade()


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
        return f'Имя: {self.name} \nФамилия: {self.surname}'


def average_student(items_mass, name_course):
    sum_ = 0
    k = 0
    for i in items_mass:
        if name_course in i.grades:
            sum_ += sum(i.grades[name_course])/len(i.grades[name_course])
            k += 1

    if k == 0:
        rez = "Оценок у студентов по данному курсу нет"
    else:
        rez = sum_ / k
    return f'Средняя оценка по курсу {name_course}: {rez}'


def average_lecture(items_mass, name_course):
    sum_ = 0
    k = 0
    for i in items_mass:
        if name_course in i.grades:
            sum_ += sum(i.grades[name_course])/len(i.grades[name_course])
            k += 1
    if k == 0:
        rez = "Оценок по лекциям данного курса нет"
    else:
        rez = sum_/k
    return f'Средняя оценка за курс лекций по {name_course}: {rez}'

# Создание и наполнение экземпляров класса Student


student_1 = Student('Sam', 'Potter', 'm')
student_2 = Student('Sony', 'Baker', 'w')
student_1.courses_in_progress += ["Python", "Git", "Game Developer"]
student_1.finished_courses += ["Java"]
student_2.courses_in_progress += ["Python", "Game Developer"]
student_2.finished_courses += ["Java", "Git"]


# Создание и наполнение класса Reviewer


reviewer_1 = Reviewer("Ron", "Davies")
reviewer_2 = Reviewer("Mary", "Gilbert")

reviewer_1.courses_attached += ["Python", "Game Developer"]
reviewer_2.courses_attached += ["Python", "Game Developer"]

reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_2.rate_hw(student_1, "Python", 10)
reviewer_1.rate_hw(student_1, "Python", 7)

reviewer_1.rate_hw(student_2, "Game Developer", 9)
reviewer_2.rate_hw(student_2, "Game Developer", 8)
reviewer_1.rate_hw(student_2, "Python", 9)

# Создание и наполнение класса Lecture


lecture_1 = Lecture("Polly", "Smith")
lecture_2 = Lecture("John", "Calvert")

lecture_1.courses_attached += ["Python"]
lecture_1.courses_attached += ["Java"]

lecture_2.courses_attached += ["Python"]
lecture_2.courses_attached += ["Game Developer"]

student_2.rate_lec(lecture_2, 'Python', 8)
student_1.rate_lec(lecture_1, 'Python', 6)
student_1.rate_lec(lecture_1, 'Java', 6)
student_2.rate_lec(lecture_2, "Game Developer", 7)


print(student_1, end='\n\n')
print(student_2, end='\n\n')
print(f"Сравнение студентов {student_1 > student_2}", end='\n\n')

print(reviewer_1, end='\n\n')
print(reviewer_2, end='\n\n')

print(lecture_1, end='\n\n')
print(lecture_2, end='\n\n')
print(f"Сравнение лекторов {lecture_1 < lecture_2}", end='\n\n')


#Вызов функций

print(average_student(Student.items, 'Python'))
print(average_lecture(Lecture.items, 'Game Developer'))
# Вызов функции с курсами которых нет

print(average_student(Student.items, 'ython'))
print(average_lecture(Lecture.items, "Pyhon"))


