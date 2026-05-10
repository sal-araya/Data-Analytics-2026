# show_major.py

student_name = "Saliem"
student_major = "CSCI"

# Determine major name and office
if student_major == "BIOL":
    major_name = "Biology"
    office = "Science Bldg, Room 410"

elif student_major == "CSCI":
    major_name = "Computer Science"
    office = "Matthew Hall, Room 344"

elif student_major == "ENG":
    major_name = "English"
    office = "Kevin Hall, Room 201"

elif student_major == "HIST":
    major_name = "History"
    office = "Kevin Hall, Room 204"

elif student_major == "MKT":
    major_name = "Marketing"
    office = "Westly Hall, Room 310"

else:
    major_name = "<unknown>"
    office = ""

# Display results
print(f"Student Name: {student_name}")
print(f"Major Code: {student_major}")
print(f"Major Name: {major_name}")
print(f"Department Office: {office}")