

class Person:
    def __init__(self, name, surname, age) -> None:
        self.__name = name
        self.__surname = surname
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property.setter
    def name(self, name):
        if name is None or len(name) < 3 or not name.isalpha():
            raise ValueError("Wrong name provided!")
        self.__name = name

    @property
    def surname(self):
        return self.__surname

    @property.setter
    def surname(self, surname):
        if surname is None or len(surname) < 3 or not surname.isalpha():
            raise ValueError("Wrong surname provided!")
        self.__surname = surname

    @property
    def age(self):
        return self.__age

    @property.setter
    def age(self, age):
        if age < 0 or age > 130:
            raise ValueError("Wrong age provided!")

    def __str__(self) -> str:
        return f'Name: ${self.name} Surname: ${self.surname} Age: ${self.age}'


class Student (Person):

    def __init__(self, name, surname, age, field_of_study) -> None:
        super().__init__(name, surname, age)
        self.__field_of_study = field_of_study
        self.__student_book = {"Subject": []}

    def addMark(self, lecture, mark):
        if not lecture.isalpha() or mark.isalpha():
            raise ValueError("Wronga data provided !")
        self.__student_book[lecture].append(mark)

    def __str__(self) -> str:
        return super().__str__() + f' Field of study ${self.__field_of_study}'


class Employee (Person):

    def __init__(self, name, surname, age, job_tittle) -> None:
        super().__init__(name, surname, age)
        self.__job_title = job_tittle
        self.__skills = set()

    def addSkill(self, skill):
        self.__skills.add(skill)

    def __str__(self) -> str:
        return super().__str__() + f"Job title ${self.__job_title}"
