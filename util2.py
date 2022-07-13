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

class ineuron_class:
    """Example 2 showing inheritance with when same function name is used for multiple classes"""
    #logging.info("created an ineuron_class parent class")
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
        raise Exception(e)
        #logging.exception(e)
