"""examples of inheritance
Importing logging module"""
import logging
logging.basicConfig(filename="inher.log",level=logging.DEBUG, format='%(levelname)s,%(asctime)s,%(name)s, %(message)s')
logging.info("examples to show inheritance")
logging.info("example-1")
class ineuron:
    try:
        def __init__(self, courses, student, faculties):
            self.courses=courses
            self.student=student
            self.faculties=faculties
        def syllabus(self):
            print("the syllabus of the course is attached in the dashboard")
    except:
        raise ValueError("invalid value")
class blog(ineuron):
    try:
        def names(self):
            name = input("enter the name of a blogger")
            return name
    except Exception as e:
        logging.exception(e)
obj1 = blog(" FSDS", "Geetanjali Singh", " krish naik ")
logging.info("object of blog class is created")
print(obj1)
print(obj1.syllabus())

logging.info("Example 2 showing inheritance with when same function name is used for multiple classes")
class ineuron_class:
    """Example 2 showing inheritance with when same function name is used for multiple classes"""
    logging.info("created an ineuron_class parent class")
    try:
        def members(self):
            print("the total members are 502")
        def account(self):
            print("the detail of the account is sent to their mail-id")
        def fees(self):
            print("you will only be allowed to attend the class if fees is paid")
        def test(self):
            print(" the test will be conducted after the completion of all modules")
    except Exception as e:
        logging.exception(e)

class tests(ineuron_class):
    logging.info("tests child class using ineuron_class as parent class ")
    def test(self):
        print(" the test will be conducted after the completion of 1 module")

obj3=tests()
logging.info("object of tests class is created")
obj3.account()
print(obj3.test())
print(obj3.fees())

"""Example 3 showing multi-level inheritance"""
logging.info("Example 3 showing multi-level inheritance")
class bloggers(blog):
    pass

obj3=bloggers(" FSDA","Prateek Chauhan"," Sudhanshu Kumar")
logging.info("object of bloggers class is created")
print(obj3.names())
print(obj3.courses)
print(obj3.faculties)

"""Example 4 showing multiple inheritance"""
class internship(ineuron):
    try:
        def students(self):
            print("total students opted internship")
        def certification(self):
            print("students will get the certification once it is completed")
    except Exception as e:
        logging.exception(e)
class mock_interview(internship, ineuron):
    logging.info("mock_interview class is inheriting both internship and ineuron class ")
    pass
obj2=mock_interview(" FSDS","Geetanjali Singh"," krish naik ")
logging.info("object of mock_interview is created")
print(obj2.students())
print(obj2.syllabus())
print(obj2.certification())
print(obj2.student)

"""Example 5 showing multiple inheritance  with same function name"""
class salary_account:
    try:
        def salaries(self):
            print("this will store the salaries of all employees")
        def payslip(self):
            print("payslip can be retrieved anytime")
    except Exception as e:
        logging.exception(e)
class ineuron_account:
    def account_status(self):
        print("check for an active account")
class expenditures(ineuron_account, ineuron_class, salary_account):
    logging.info("class expenditures is inheriting ineuron_account, ineuron_class, salary_account) ")
    pass
obj3=expenditures()
logging.info("object of expenditures class is created")
print(obj3.account())
print(obj3.payslip())
print(obj3.salaries())
print(obj3.account_status())

"""example 6 showing the private, protected and public variables, when one class is inherited in another"""
try:
    class candidates:
        logging.info("example 6 showing the private, protected and public variables, when one class is inherited in another")
        _name="Geetanjali"
        __surname="Singh"
        yob=1992
        starting_month=6
        def _internship_period(self, finish_month):
            return finish_month-self.starting_month
        def __internship_period(self, finish_month):
            return finish_month-self.starting_month

    class intership_certificate(candidates):
        logging.info("intership_certificate class is inheriting candidates class)")
        _name="Prateek"
        __surname = "Chauhan"
        yob=1998
except Exception as e:
    logging.exception(e)
obj5=intership_certificate()
logging.info("object of intership_certificate class is created")
print(obj5._internship_period(11))
print(obj5._candidates__internship_period(12))
print(obj5.yob)
print(obj5._name)
print(obj5.starting_month)

""" example 7 using the super method in inheritance concept"""
try:
    logging.info("example 7 using the super method in inheritance concept")
    class internship1():
        def students(self):
            print("total students opted internship")

        def certification(self):
            print("students will get the certification once it is completed")

    class ineuron_head(internship1):
        def __init__(self, head_assigned):
            super().__init__()
            self.head_assigned = head_assigned
except Exception as e:
    logging.exception(e)
obj6=ineuron_head("Krish Naik")
logging.info("object of ineuron_head class is created")
print(obj6.head_assigned)
obj6.certification()

"""example 8 using multiple inheritance"""
try:
    logging.info("example 8 using multiple inheritance")
    class jobs:
        def __init__(self):
            self.job_title = "Data Scientist"
    class salary:
        def salary(self):
            print("list the salaries of all the candidates selected")
    class joining(jobs, salary):
        pass
except Exception as e:
    logging.exception(e)
obj7=joining()
logging.info("object of joining class is created")
print(obj7.job_title)
obj7.salary()

""" example 9 showing use of multiple init function in inheritance"""
try:
    logging.info("example 9 showing use of multiple init function in inheritance")
    class jobs:
        def __init__(self):
            self.job_title = "Data Scientist"
    class salary:
        def __init__(self):
            self.salary_amount = "22 LPA"
    class joining(jobs, salary):
        def __init__(self):
            jobs.__init__(self)
            salary.__init__(self)
            print("merged")
except Exception as e:
    logging.exception(e)
obj7 = joining()
print(obj7.salary_amount)

""" example 10 to show usage of modules """
logging.info("example 10 to show usage of modules")
from utils.util1 import candidate_next
logging.info("candidate_next class is imported from utils.util1 module")
obj8=candidate_next("geet","singh", "hey@gmail.com", 1992)
logging.info("object is created here and called")
print(obj8._name)
print(obj8._candidate_next__surname)






