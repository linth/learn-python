# 通過範例可以知道使用dict or list可以用來存取資料
class SimpleGradeBook(object):
    """ simple grade book class. """
    def __init__(self):
        self._grades = dict()

    def add_student(self, name):
        self._grades[name] = []

    def report_grade(self, name, score):
        self._grades[name].append(score)

    def average_grade(self, name):
        grades = self._grades[name]
        return sum(grades) / len(grades)


# TODO: if you want to add course.
class WithSubjectGreadBook(object):
    """ extend the SimpleGradeBook class. """
    def __init__(self):
        self._grades = dict()

    def add_student(self, name):
        self._grades[name] = dict()

    def report_grade(self, name, subject, score):
        subject_course = self._grades[name]
        grade_list = subject_course.setdefault(subject, [])
        grade_list.append(score)

    def average_grade(self, name):
        subject_course = self._grades[name]
        total, count = 0, 0
        for grades in subject_course.values():
            total += sum(grades)
            count += len(grades)
        return total / count


# 發現到隨著資料增加，程式碼複雜度隨之增加。應該可以使用階層架構類別處理 (a hierarchy of classes)
import collections
Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject(object):
    """ the subject class. """
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student(object):
    """ the student class. """
    def __init__(self, name):
        self._subjects = dict()

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject()
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class GradeBook(object):
    """ the grade book class. """
    def __init__(self):
        self._students = dict()

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student(name)
        return self._students[name]


if __name__ == '__main__':
    s = SimpleGradeBook()
    s.add_student('george')
    s.report_grade('george', 90)
    s.report_grade('george', 60)
    print(s.average_grade('george'))

    w = WithSubjectGreadBook()
    w.add_student('may')
    w.report_grade('may', 'english', 70)
    w.report_grade('may', 'english', 100)
    print(w.average_grade('may'))

    # TODO: need to think and read again.
    b = GradeBook()
    info = b.student('peter')
    math = info.subject('Math')
    math.report_grade(80, 0.10)
    print(info.average_grade())
