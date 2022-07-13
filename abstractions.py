"""examples of abstraction
Importing logging module
Importing ineuron class from util2 module"""
import logging
from utils.util2 import ineuron
logging.basicConfig(filename="abs.log",level=logging.DEBUG, format='%(levelname)s,%(asctime)s,%(name)s, %(message)s')
logging.info("examples to show abstraction concept")
"""Example 1 showing the abstract class imported from another module"""
class blog(ineuron):
    try:
        def names(self):
            print("the blog name of ineurons")
    except Exception as e:
        logging.exception(e)

class bloggers(blog):
    try:
        def names(self):
            print("the blogger who wrote this blog is shweta jain")
    except Exception as e:
        logging.exception(e)

obj1 = bloggers(" FSDS", "Geetanjali Singh", " krish naik ")
logging.info("object of bloggers class is created")
obj1.names()
print(obj1.syllabus())
logging.info("obj1.syllabus() will print the method of the abstract class")

"""Example 2 of abstraction"""
try:
    class candidates:
        logging.info("Example 2 of abstraction")
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

"""Example 3 of abstraction"""
try:
    logging.info("example-3")
    class ineuron:
        __students="data science"

        def students(self):
            print("print the class od students", ineuron.__students)
except Exception as e:
    logging.info(e)
i=ineuron()
i.students()
print(i._ineuron__students)

"""Example 4 of abstraction"""
from utils.util2 import ineuron_class
logging.info("importing ineuron_class class from util2 module")
class tests(ineuron_class):
    logging.info("tests class will inherit abstract class ineuron_class")
    try:
        def test(self):
            print("start test of new syllabus")
            logging.info("abstract class information is overridden")
    except Exception as e:
        logging.exception(e)
obj2=tests()
logging.info("object of tests class is created")
obj2.test()

"""Example 5 of abstraction"""
class new_syllabus(ineuron_class):
    try:
        def new_syllabus(self):
            print("new syllabus")
    except Exception as e:
        logging.exception(e)
class tests1(new_syllabus):
    try:
        def test(self):
            super().test()
            logging.info("super method is called to access the super class method in case of overriding")
            print("start test of new syllabus")
    except Exception as e:
        logging.exception(e)
obj2=tests1()
obj2.fees()
obj2.test()
logging.info("this function will be called from the tests class, but by using the super method abstract class method will be called")
obj2.new_syllabus()



