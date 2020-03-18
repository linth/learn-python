"""
Goal: learn about documenting python code: a complete guide.

Keyword:
    - documenting code
    - commenting
    - tagging

References:
    - https://realpython.com/documenting-python-code/
"""


class Student:
    """
    The class is about Student class.

    Attributes
    ---
    id: str
        a student id.
    name: str
        a student name.
    """

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        """
        show the student class's id and name.
        :return:
        """
        return f'ID: {self.id}, Name: {self.name}'

    def get_student_name_by_id(self, id):
        """Function name: get_student_name_by_id()
        search a specific student' name by student's id.
        :param id: student's id.
        :return: student's name.
        """
        if self.id == id:
            return self.name
        else:
            return {'message': 'not found.'}

    def get_id_by_student_name(self, name):
        """Function name: get_id_by_student_name()
        get a specific student's id by student's name.
        :param name: student's name.
        :return: student's id.
        """
        if self.name == name:
            return self.id
        else:
            return {'message': 'not found.'}


if __name__ == '__main__':
    # help(Student)             # function help() that prints out the objects docstring to the console
    # print(dir(Student))       # show all functions and attributes.
    print(Student.__doc__)      # show the description of this class.
    print(Student.get_student_name_by_id.__doc__)   # show the description of this function.
