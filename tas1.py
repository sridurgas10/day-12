class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def calculate_total(self):
        return sum(self.marks.values())
    def viewgrade(self):
        total=self.calculate_total()
        grade=total/len(self.marks)

        if grade>=90:
             return 'A'
        elif grade>=80:
             return 'B'
        elif grade>=70:
             return 'C'
        elif grade>=60:
             return 'D'
        else:
            return 'F'      
    def display_report_cards(self):
        print("-----REPORT CARD-----")
        print(f"the student name is :{self.name}")
        print(f"student roll no : {self.roll_number}")
        print("marks")
        for subject ,marks in self.marks.items():
            print(f" {subject}:{marks}")
        print(f"total marks : {self.calculate_total()}")   
        print(f"grade is : {self.viewgrade()}") 
        print("-----------------------")
student=Student("sri",5,{"tamil":80,"english":90,"maths":89,"science":96,"social":100})
student.display_report_cards()