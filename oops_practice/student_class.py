class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

        self.subjects = set()

    def add_subject(self, subject):
        self.subjects.add(subject)


    def remove_subject(self, subject):
        try:
            self.subjects.remove(subject)
        except KeyError:
            print(f"Subject '{subject}' not found in the list of subjects.")



# Create a new student object
student1 = Student("Priya", "S12345")

# Try to add some subjects
student1.add_subject("Math")
student1.add_subject("Physics")
student1.add_subject("Math") # This should not add a duplicate

# Try to remove subjects
student1.remove_subject("History") # This subject doesn't exist
student1.remove_subject("Physics")

# You can check the final list of subjects
print(f"Final subjects for {student1.name}: {student1.subjects}")


"""
below code when list used insted of sets


class Student:
    
    # Represents a student with a name, ID, and a list of enrolled subjects.

    def __init__(self, name, student_id):
        
        # Initializes a new Student object.
        
        self.name = name
        self.student_id = student_id
        self.subjects = [] # Start with an empty list of subjects

    def add_subject(self, new_subject):
        
        # Adds a subject to the student's list if it's not already there.
        
        if new_subject not in self.subjects:
            self.subjects.append(new_subject)
            print(f"{self.name} has been enrolled in {new_subject}.")
        else:
            # This part is optional, but good for feedback
            print(f"{self.name} is already enrolled in {new_subject}.")

    def remove_subject(self, subject_to_remove):
        
        # Removes a subject from the student's list if it exists.
    
        if subject_to_remove in self.subjects:
            self.subjects.remove(subject_to_remove)
            print(f"{self.name} has been unenrolled from {subject_to_remove}.")
        else:
            # This part is also optional, but helpful
            print(f"Cannot unenroll. {self.name} is not enrolled in {subject_to_remove}.")

"""