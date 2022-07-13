"""examples of encapsulation
Importing logging module"""
import logging
logging.basicConfig(filename="encap.log",level=logging.DEBUG, format='%(levelname)s,%(asctime)s,%(name)s, %(message)s')
logging.info("examples to show encapsulation")
"""Example 1 showing the encapsulation concept """
class ineuron_details:
    try:
        logging.info("Example 1")
        def __init__(self):
            self.__stud = "DS"

        def stud(self):
            print(self.__stud)

        def student_change(self, new):
            logging.info("this method works as a setter function")
            self.__stud = new
    except AttributeError as a:
        logging.exception(a)
i1=ineuron_details()
logging.info("object of ineuron_details class is called")
i1.__stud="big data"
logging.info("will not change the value of private variable")
i1.stud()
i1.student_change("my big data")
i1.stud()

"""Example 2 """
class ineuron_class:
    try:
        logging.info("Example 2 ")
        def __init__(self, name, project, duration):
            self.name = name
            self.project = project
            self.__duration = duration

        def batch(self):
            print(self.name, "is working on", self.project, "for", self.__duration, "months")
    except AttributeError as a:
        logging.exception(a)
obj1=ineuron_class("geet","dstl", 3)
obj1.batch()
logging.info("batch method will display the output")
print(obj1._ineuron_class__duration)

"""Example 3 using protected variable"""
try:
    logging.info("Example 3 using protected variable")
    class instructor:
        def __init__(self):
            self._nos_of_instructors = 2


    class total(instructor):
        def __init__(self):
            instructor.__init__(self)
            print("the original value is", self._nos_of_instructors)
            self._nos_of_instructors = 8
            print("the changed value is", self._nos_of_instructors)
except Exception as e:
    logging.exception(e)
obj2=total()
logging.info("object of total class is created")
obj2._nos_of_instructors
logging.info("protected variable can be called like this")

"""Example 4  """

try:
    logging.info("Example 4 ")
    class stars:
        def __init__(self):
            self.course = "Data science"
            self.__title = "star of the month"


    class placement(stars):
        def __init__(self):
            stars.__init__(self)
            print("the title of student got placed", self._stars__title)
except Exception as e:
    logging.exception(e)
obj3=placement()
logging.info("object of placement class is created")
print(obj3.course)
print(obj3._stars__title)
logging.info("thi sis the way to call a private variable")

"""Example 5 """
class blog:
    try:
        logging.info("Example 5")
        def __init__(self, name, age):
            self.name = name
            self.__age = age

        def reader(self):
            logging.info("this will act as a getter function")
            return self.__age

        def writer(self, newage):
            logging.info("this will act as a setter function")
            self.__age = newage
    except AttributeError as a:
        logging.exception(a)

obj5=blog("geet", "29")
print(obj5.name, obj5.reader())
obj5.writer(25)
print(obj5.name, obj5.reader())

"""Example 6 """
class course:
    try:
        logging.info("Example 6")
        def __init__(self, name, id, syllabus):
            self.name = name
            self.__id = id
            self.__syllabus = syllabus

        def show_data(self):
            print("students details for course are", self.name, self.__id, self.__syllabus)

        def get_new_data(self, new_syllabus):
            if new_syllabus != "old":
                print("please select new syllabus")
            else:
                self.new_syllabus = new_syllabus
    except Exception as e:
        logging.exception(e)
obj6=course("pawan", 10, "old")
obj6.show_data()
obj6.get_new_data("new")

"""Example 7 """
class course:
    try:
        logging.info("Example 7 ")
        def __init__(self, name, id, syllabus):
            self.name = name
            self.__id = id
            self.__syllabus = syllabus

        def show_data(self):
            print("students details for course are", self.name, self.__id, self.__syllabus)

        def get_new_data(self, new_syllabus):
            if new_syllabus == "old":
                print("please select new syllabus")
            else:
                self.name = "prateek"
                self.__syllabus = new_syllabus
    except AttributeError as e:
        logging.exception(e)
obj6=course("pawan", 10, "old")
obj6.show_data()
obj6.get_new_data("old")
obj6.get_new_data("new")
obj6.show_data()

"""Example 8 """
class internship:
    try:
        logging.info("Example 8")
        def __init__(self):
            self.__project = "big data"
            self.__deadline = "2023"

        def show(self):
            print(self.__project)
            logging.info(self.__project)
            print(self.__deadline)
            logging.info(self.__deadline)

        def modify(self, project1, deadline1):  ### setter function
            self.__project = project1
            self.__deadline = deadline1
    except Exception as e:
        logging.exception(e)
obj8=internship()
obj8.__project="cloud"
obj8.__deadline="2022"
obj8.show()
obj8.modify("hadoop", 2024)
obj8.show()

