# -*- coding: utf-8 -*-
"""
Alyssa Wheeler
3/19/24
GPA class
"""
#import Course class
from Course import Course

class GPA(Course):
    def __init__ (self,abbreviation, number, name, number_credits, semester, lettergrade):
        #inherit month,day,year from Date class
        super().__init__(abbreviation, number, name, number_credits)
        self.semester = semester
        self.lettergrade = lettergrade
            
    #get numeric grade from lettergrade
    def getQualityPoints(lettergrade, number_credits):
        if lettergrade == "A":
            numeric = 4.00
        if lettergrade == "A-":
            numeric = 3.67
        if lettergrade == "B+":
            numeric = 3.33
        if lettergrade == "B":
            numeric = 3.00
        if lettergrade == "B-":
            numeric = 2.67
        if lettergrade == "C+":
            numeric = 2.33
        if lettergrade == "C":
            numeric = 2.00
        if lettergrade == "C-":
            numeric = 1.67
        if lettergrade == "D+":
            numeric = 1.33
        if lettergrade == "D":
            numeric = 1.00
        if lettergrade == "D-":
            numeric = 0.67
        if lettergrade == "F":
            numeric = 0.00
        
        #return numberic grade * number of credits to get quality points
        return float(number_credits * numeric)
    
    def numericGPA(lettergrade):
        if lettergrade == "A":
            return 4.00
        if lettergrade == "A-":
            return 3.67
        if lettergrade == "B+":
            return 3.33
        if lettergrade == "B":
            return 3.00
        if lettergrade == "B-":
            return 2.67
        if lettergrade == "C+":
            return 2.33
        if lettergrade == "C":
            return 2.00
        if lettergrade == "C-":
            return 1.67
        if lettergrade == "D+":
            return 1.33
        if lettergrade == "D":
            return 1.00
        if lettergrade == "D-":
            return 0.67
        if lettergrade == "F":
            return 0.00
            
#return printed out variables
    def __str__(self):
        return "Department abbreviation: " + str(self.abbreviation) + "course #: " + str(self.number) + "course name:" + str(self.name) + "# of credits" + str(self.number_credits)
        return "Semester: " + str(self.semester) + "lettergrade: " + str(self.lettergrade)