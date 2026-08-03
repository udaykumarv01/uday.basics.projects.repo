name = input("enter the name of student : ")
first_subject = int(input("enter your kannada marks : "))
second_subject = int(input("enter your english marks : "))
third_subject = int(input("enter your physics marks : "))
fourth_subject = int(input("enter your chemistry marks : "))
fifth_subject = int(input("enter your mathematics marks : "))
sixth_subject = int(input("enter your biology or computerscience marks : "))
sum_of_subject_marks = first_subject + second_subject + third_subject + fourth_subject + fifth_subject + sixth_subject
print("sum of subject marks", sum_of_subject_marks)
percentage = sum_of_subject_marks / 600 * 100
print(percentage)

if percentage >= 95:
    print(f"{name} is passed with greater distinction and congratulations to your")
elif percentage >= 85:
    print(f"{name} is passed with distinction and congratulations to your")
elif percentage >= 60:
    print(f"{name} is passed with first class and congratulations to your")
elif percentage >= 35:
    print(f"{name} is passed with second class and congratulations to your")
else:
    print(f"{name} is failed")

# This code calculates the total marks and percentage of a puc science student based on their six subjects
# It also then determines the class student passing based on percentage.