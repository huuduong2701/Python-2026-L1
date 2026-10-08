import numpy as np

class Student:
    def __init__(self, s_id, name, dob):
        self.id = s_id
        self.name = name
        self.dob = dob
        self.marks = {}
        self.gpa = 0.0

    def calculate_gpa(self, courses):
        marks_list = []
        credits_list = []
        for c in courses:
            if c.id in self.marks:
                marks_list.append(self.marks[c.id])
                credits_list.append(c.credits)
        
        if credits_list and sum(credits_list) > 0:
            arr_marks = np.array(marks_list)
            arr_credits = np.array(credits_list)
            self.gpa = float(np.sum(arr_marks * arr_credits) / np.sum(arr_credits))
        else:
            self.gpa = 0.0
        return self.gpa