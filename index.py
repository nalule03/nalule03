# Define variables for marks in each subject
database = float(input("Enter Database marks: "))
computing =  float(input("Enter Computing marks: "))
administration = float(input("Enter administration marks: "))
mathematics = float(input("Enter mathematics marks: "))
programming = float(input("Enter Programming marks: "))
leadership = float(input("Enter leadership marks: "))


# Calculate total marks
total_marks =  database + computing + administration + mathematics + programming  + leadership

# Calculate average marks
average_marks = total_marks / 6

# Check if the student has passed or failed
passing_marks = 40
if average_marks >= passing_marks:
    result = "Passed"
else:
    result = "Failed"

# Display total marks, average marks, and result
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Result:", result)

# Provide feedback if student has failed
if result == "Failed":
    print("Areas for improvement: Study harder in all subjects.")