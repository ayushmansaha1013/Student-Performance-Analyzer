class Student:
    # Initialize student data
    def __init__(self, name, roll_no, marks, subjects):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.subjects = subjects

    # Calculate total marks
    def calculate_total(self):
        return sum(self.marks)

    # Calculate average marks
    def calculate_average(self):
        if self.marks:
            return sum(self.marks) / len(self.marks)
        return 0.0

    # Calculate grade
    def calculate_grade(self):
        average = self.calculate_average()

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

