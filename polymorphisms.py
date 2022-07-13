"""examples of polymorphism
Importing logging module"""
import logging
logging.basicConfig(filename="poly.log",level=logging.DEBUG, format='%(levelname)s,%(asctime)s,%(name)s, %(message)s')
logging.info("examples to show polymorphism")

"""example 1"""
try:
    logging.info("example 1")
    class ineuron:
        def students(self):
            print("print students details")

    class class_type:
        def students(self):
            print("print the class type of students")

    def ineuron_ex(a):
        logging.info("creating a bridge function")
        a.students()
        logging.info("calling the same function from this method")
except Exception as e:
    logging.exception(e)
obj1= ineuron()
logging.info("creating an object of ineuron class")
obj2= class_type()
logging.info("creating an object of class_type class")
ineuron_ex(obj1)
ineuron_ex(obj2)

""" example 2 of polymorphism using an inbuilt function """
logging.info("example 2 of polymorphism using an inbuilt function ")
print(len("geeks"))
logging.info("len() is a string function")
print(len([10,20,50,60]))
logging.info("It is used here for list type ")

""" example 3 of polymorphism """

class ineuron:
    logging.info("example 3 of polymorphism")
    try:
        def students(self):
            print("total number of students present")

        def batches(self):
            print("total batches")

        def classes(self):
            print("total number of classes to be held")
    except Exception as e:
        logging.exception(e)

class metadata:
    try:
        def students(self):
            print("total number of employees present")

        def batches(self):
            print("total group for 1 project")

        def classes(self):
            print("training period")
    except Exception as e:
        logging.exception(e)
obj3=ineuron()
logging.info("creating an object of ineuron class")
obj4=metadata()
logging.info("creating an object of metadata class")
for i in (obj3,obj4):
    i.students()
    i.batches()
    i.classes()

""" example 4 of polymorphism using functions """
try:
    logging.info("example 4 of polymorphism using functions")
    class ineuron_details:
        def names(self):
            print(" faculty detail ")

        def students(self):
            print("")

    class student_details(ineuron_details):
        def names(self):
            print("the names of the students are given")

        def joining_date(self):
            print("the joining date of students is given")

    class faculty_details(ineuron_details):
        def names(self):
            print("the names of the faculties are given")

        def joining_date(self):
            print("the joining date of faculties is given")
except Exception as e:
    logging.exception(e)
obj5=ineuron_details()
obj6=student_details()
obj7=faculty_details()
def bridge1(value):
    logging.info("creating a bridge function")
    value.names()
def bridge2(value):
    logging.info("creating another bridge function")
    value.joining_date()
bridge1(obj5)
bridge1(obj6)
bridge1(obj7)
bridge2(obj6)
bridge2(obj7)

""" example 5 of polymorphism with inheritance """

class ineuron_details1:
    logging.info('example 5 of polymorphism with inheritance')
    try:
        def names(self):
            print(" faculty detail ")

        def students(self):
            print("")
    except Exception as e:
        logging.exception(e)
class student_details1(ineuron_details1):
    try:
        def names(self):
            print("the names of the students are given")

        def joining_date(self):
            print("the joining date of students is given")
    except Exception as e:
        logging.exception(e)
class faculty_details1(ineuron_details1):
    try:
        def names(self):
            print("the names of the faculties are given")

        def joining_date(self):
            print("the joining date of faculties is given")
    except Exception as e:
        logging.exception(e)
obj5=ineuron_details()
obj6=student_details()
obj7=faculty_details()
obj5.names()
obj5.students()
obj6.names()
obj6.joining_date()
obj7.names()
obj7.joining_date()

""" example 6 of polymorphism  """
try:
    class achievements:
        logging.info("example 6 of polymorphism")

        def achievers(self):
            print("2022 achievers detail is displayed on the dashboard")


    class prize(achievements):
        def achievers(self):
            print("prize will be distributed to the achievers")


    def achieve(name):
        logging.info("creating a bridge function")
        name.achievers()
except Exception as e:
    logging.exception(e)

obj8= achievements()
obj9= prize()
achieve(obj8)
achieve(obj9)
