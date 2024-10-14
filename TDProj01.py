# -*- coding: utf-8 -*-
"""
Alyssa Wheeler
3/19/24
Add student info to CSV file
"""

import csv
from GPA import GPA

if __name__ == "__main__":
    #prompt if adding new student or not
    NewStudent = input("Is this a new student (Y/y): ")
    if NewStudent == "Y" or NewStudent == "y":
        while True:
            try:
                #prompt for Student ID and first and last name
                StudentID = input("Enter Student's ID number: ")
                StudentFirst = input("Enter Student's first name: ")
                StudentLast = input("Enter Student's last name: ")
                
                #open and create csv file to write
                with open ("{}-{}-{}.csv".format(StudentID,StudentFirst,StudentLast), "w+") as file:
                    myFile = csv.writer(file, lineterminator = '\n')
                    
                    #header row
                    myFile.writerow(["Department", "Course Number", "Course Name", "Credits", "Semester", "Grade", "Quality Points", "GPA"])
                    while True: 
                        try: 
                            #get input for GPA attributes
                            Student = GPA((input("Enter course abbreviation: ")),(input("Enter course number: ")),(input("Enter course name: ")),(int(input("Enter the number of course credits: "))),(input("Enter the semester (ex:20/FA): ")),(input("Enter the letter grade: ")))
                            
                            #get Quality Points
                            grade = GPA.getQualityPoints(Student.lettergrade, Student.number_credits)
                            
                            #get overal GPA
                            Overall_GPA = float(GPA.numericGPA(Student.lettergrade))
                            
                            #write rows to file
                            myFile.writerow([Student.abbreviation, Student. number, Student.name, Student.number_credits, Student.semester, Student.lettergrade, grade, Overall_GPA])
                            
                            #prompt if want to add another course to student
                            prompt_addmore = input("Add more courses? (Y/y): ")
                            if prompt_addmore == "y":
                                continue
                            if prompt_addmore == "Y":
                                continue
                            else:
                                break
                            
                            #add overall_GPA
                            myFile.writerow(["Overall GPA:" + sum(Overall_GPA)])
                            
                        except ValueError:
                            print("Error")
                        print
                        
                    file.close()
                        
                    #open file to read
                    with open("{}-{}-{}.csv".format(StudentID,StudentFirst,StudentLast)) as file:
                        reader = csv.reader(file)
                        for row in reader:
                            
                            #print rows to console
                            print(row)
                            
                        file.close()
                        
                #prompt to continue or not
                    prompt_user = input("Continue? (Y/y): ")
                    if prompt_user == "y":
                        continue
                    if prompt_user == "Y":
                        continue
                    else:
                        break
                
            except ValueError:
                print("Error")
                
    #if not adding new student, prompt to ask which student want to look at
    else:
        StudentID = input("Enter Student's ID number: ")
        StudentFirst = input("Enter Student's first name: ")
        StudentLast = input("Enter Student's last name: ")

        #open in read and print to console
        with open("{}-{}-{}.csv".format(StudentID,StudentFirst,StudentLast)) as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                
            file.close()

"""
Is this a new student (Y/y): y
Enter Student's ID number: 222
Enter Student's first name: Jane
Enter Student's last name: Day
Enter course abbreviation: DS
Enter course number: 510
Enter course name: Computer Science Fundamentals
Enter the number of course credits: 4
Enter the semester (ex:20/FA): 20/FA
Enter the letter grade: A
Add more courses? (Y/y): Y
Enter course abbreviation: MA
Enter course number: 117
Enter course name: Discrete Structures
Enter the number of course credits: 4
Enter the semester (ex:20/FA): 19/FA
Enter the letter grade: B
Add more courses? (Y/y): n
['Department', 'Course Number', 'Course Name', 'Credits', 'Semester', 'Grade', 'Quality Points', 'GPA']
['DS', '510', 'Computer Science Fundamentals', '4', '20/FA', 'A', '16.0', '4.0']
['MA', '117', 'Discrete Structures', '4', '19/FA', 'B', '12.0', '3.0']
Continue? (Y/y): n

Is this a new student (Y/y): n
Enter Student's ID number: 222
Enter Student's first name: Jane
Enter Student's last name: Day
['Department', 'Course Number', 'Course Name', 'Credits', 'Semester', 'Grade', 'Quality Points', 'GPA']
['DS', '510', 'Computer Science Fundamentals', '4', '20/FA', 'A', '16.0', '4.0']
['MA', '117', 'Discrete Structures', '4', '19/FA', 'B', '12.0', '3.0']

Is this a new student (Y/y): y
Enter Student's ID number: 111
Enter Student's first name: John
Enter Student's last name: Doe
Enter course abbreviation: CS
Enter course number: 104
Enter course name: Quantitative Methods
Enter the number of course credits: 3
Enter the semester (ex:20/FA): 20/SP
Enter the letter grade: C+
Add more courses? (Y/y): n
['Department', 'Course Number', 'Course Name', 'Credits', 'Semester', 'Grade', 'Quality Points', 'GPA']
['CS', '104', 'Quantitative Methods', '3', '20/SP', 'C+', '6.99', '2.33']
"""
            
            