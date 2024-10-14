# -*- coding: utf-8 -*-
"""
Alyssa Wheeler
3/19/24
Course attributes
"""

class Course:
    def __init__ (self,abbreviation, number, name, number_credits):
        self.abbreviation = abbreviation
        self.number = number
        self.name = name
        self.number_credits = number_credits
        
    #return printed out variables
        def __str__(self):
            return "Department abbreviation: " + str(self.abbreviation) + "course #: " + str(self.number) + "course name:" + str(self.name) + "# of credits" + str(self.number_credits)
