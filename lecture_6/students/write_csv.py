import csv

name = input("Name: ")
house = input("House: ")

with open("students_write.csv", "a", newline="") as file:
    writer = csv.DictWriter(
        file, fieldnames=["name", "house"]
    )  # fieldnames is a list of column names
    writer.writerow({"name": name, "house": house})
