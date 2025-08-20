class Student:
    def __init__(self, name, house, patronus):
        self.name = name
        self.house = house
        self.patronus = patronus

    # this will be called when we print the object
    def __str__(Self):
        return "a student"

    def charm(self):
        match self.patronus:
            case "Stag":
                return " S "
            case "Otter":
                return " O "
            case "Jack Russell terrier":
                return " J "
            case _:
                return "/"

    @property
    def house(self):
        return self.house

    @house.setter
    def house(self, house):
        if house not in ["A", "B", "C", "D"]:
            raise ValueError("Invalid house")
        self.house = house

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Name required")
        self.name = name


def main():
    student = get_student()
    print(student)  # this will call the __str__ method automatically
    print(f"{student.name} from {student.house} used the charm {student.charm()}")


def get_student():
    name = input("Enter student name: ")
    house = input("Enter student house: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main()
