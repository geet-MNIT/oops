""" example 1 showing overriding concept"""
import logging
logging.basicConfig(filename="over.log",level=logging.DEBUG, format='%(levelname)s,%(asctime)s,%(name)s, %(message)s')
logging.info("example-1 showing overriding concept")
try:
    class ineuron:
        def student(self):
            print("print the details of all the students")
        def achievers(self):
            print("achievers")
        def hall_of_fame(self):
            print("print everyone")
    class hiring(ineuron):
        def student(self):
            print("these are the filters student list")
except Exception as e:
    logging.exception(e)
obj1 = hiring()
logging.info("object of hiring class is created")
obj1.student()
logging.info("object of student class is created")

""" example 2 """
try:
    logging.info("example 2 ")
    class jobs():
        def __init__(self):
            self.candidates_count = 84

        def get_value(self):
            return self.candidates_count

    class placed(jobs):
        def get_value(self):
            return self.candidates_count + 1
except Exception as e:
    logging.exception(e)
obj2=placed()
logging.info("object of placed class is created")
print(obj2.get_value())

""" example 3 with multiple init methods"""
try:
    logging.info("example 3 with multiple init methods")
    class course_reg:
        def __init__(self):
            self.value = "course registration will start from tomorrow"
        def print_msg(self):
            print(self.value)
    class fees_pay(course_reg):
        def __init__(self):
            self.value = "please pay the feel to register completely"
        def print_msg(self):
            print(self.value)
except Exception as e:
    logging.exception(e)
obj3=fees_pay()
logging.info("object of fees_pay class is created")
obj3.print_msg()

""" example 4 of overriding using multiple inheritance"""
try:
    logging.info("example 4 of overriding using multiple inheritance")
    class course_reg1:
        def __init__(self):
            self.value = "course registration will start from tomorrow"

        def print_msg(self):
            print(self.value)

    class fees_pay1:
        def __init__(self):
            self.value = "please pay the feel to register completely"

        def print_msg(self):
            print(self.value)

    class acknowleged(course_reg1, fees_pay1):
        def print_msg(self):
            print("thank you for registering with ineuron")
except Exception as e:
    logging.exception(e)
obj4=acknowleged()
logging.info("object of acknowleged class is created")
obj4.print_msg()

""" example 5 """
try:
    class syllabus:
        def details(self):
            print("select the course to get the syllabus")

    class list_of_couses(syllabus):
        def details(self):
            print("for which course you want the syllabus")

    class data_science(list_of_couses):
        def details(self):
            print("click for data science syllabus")

    class data_analytics(data_science):
        def details(self):
            print("click for data analytics syllabus")
except Exception as e:
    logging.exception(e)
obj5=data_science()
logging.info("object of data_science class is created")
obj5.details()
logging.info("object of details class is created")
