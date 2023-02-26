# Name:                     Task 7: Course Registration
# Author:                   Yunfeng Lin (Ylin8832)
# Date Created:             February 25, 2023
# Date Last Modified:       February 26, 2023

print("\n{0:-^64s}".format("Welcome to course registering system".upper()))


# Create a dictionary called aList.
aList = {
    "firstName":" ",
    "lastName":" ",
    "studentNumber":" "
}
# pass the input data from the user to 
aList["firstName"] = input("\nEnter your first name: ")
aList["lastName"] = input("Enter your last name: ")
aList["studentNumber"] = input("Enter your student number: ")

# Creat a dictionary called forCourses.
fourCourses = {
    "E124": "English",
    "P457": "Programing",
    "N579": "Network",
    "C678": "Computer"
}
# display available course IDs and coresponding course names to the user.
print("\n{0:-^48}".format("Your available couses are"))
for key, value in fourCourses.items():
    print(key, value)

# Prompt user to select courses that they would like to register.
# and store the input data in to the variable called disiredCourse.
disiredCourse = input("\nEnter the course ID you would like to register(with ',' in between course IDs): ")
courseList = (disiredCourse.replace(" ", "")).split(",")

# Desplay user information (Student name and ID) and selected courses for the final confirmation.
print("\n{0:*^64s}".format("Please confirm your registeration info below"))
print("\nStudent information:\n{} {},{}".format(aList["firstName"], aList["lastName"], aList["studentNumber"]))
print("\nRegistered courses: ")
for n in courseList:
    print(n, fourCourses[n])
