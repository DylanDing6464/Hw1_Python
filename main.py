c1LetterGrade = input("Enter your course 1 letter grade: ")
c1CourseCredit = input("Enter your course 1 credit: ")
if(c1LetterGrade == "A"):
  c1GradePoint = 4.0
elif(c1LetterGrade == "A-"):
  c1GradePoint = 3.67
elif(c1LetterGrade == "B+"):
	c1GradePoint = 3.33
elif(c1LetterGrade == "B"):
	c1GradePoint = 3.0
elif(c1LetterGrade == "B-"):
	c1GradePoint = 2.67
elif(c1LetterGrade == "C+"):
	c1GradePoint = 2.33
elif(c1LetterGrade == "C"):
	c1GradePoint = 2.0
elif(c1LetterGrade == "D"):
	c1GradePoint = 1.0
else:
	c1GradePoint = 0.0
print (f"Grade point for course 1 is: {c1GradePoint}")

c2LetterGrade = input("Enter your course 2 letter grade: ")
c2CourseCredit = input("Enter your course 2 credit: ")
if(c2LetterGrade == "A"):
	c2GradePoint = 4.0
elif(c2LetterGrade == "A-"):
	c2GradePoint = 3.67
elif(c2LetterGrade == "B+"):
	c2GradePoint = 3.33
elif(c2LetterGrade == "B"):
	c2GradePoint = 3.0
elif(c2LetterGrade == "B-"):
	c2GradePoint = 2.67
elif(c2LetterGrade == "C+"):
	c2GradePoint = 2.33
elif(c2LetterGrade == "C"):
	c2GradePoint = 2.0
elif(c2LetterGrade == "D"):
	c2GradePoint = 1.0
else:
	c2GradePoint = 0.0
print (f"Grade point for course 1 is: {c2GradePoint}")
c3LetterGrade = input("Enter your course 3 letter grade: ")
c3CourseCredit = input("Enter your course 3 credit: ")

if(c3LetterGrade == "A"):
	c3GradePoint = 4.0
elif(c3LetterGrade == "A-"):
	c3GradePoint = 3.67
elif(c3LetterGrade == "B+"):
	c3GradePoint = 3.33
elif(c3LetterGrade == "B"):
	c3GradePoint = 3.0
elif(c3LetterGrade == "B-"):
	c3GradePoint = 2.67
elif(c3LetterGrade == "C+"):
	c3GradePoint = 2.33
elif(c3LetterGrade == "C"):
	c3GradePoint = 2.0
elif(c3LetterGrade == "D"):
	c3GradePoint = 1.0
else:
	c3GradePoint = 0.0
print (f"Grade point for course 1 is: {c3GradePoint}")

c1CourseCredit = float(c1CourseCredit)
c2CourseCredit = float(c2CourseCredit)
c3CourseCredit = float(c3CourseCredit)


gpa = (c1GradePoint * c1CourseCredit + c2GradePoint * c2CourseCredit + c3GradePoint * c3CourseCredit) / (c1CourseCredit + c2CourseCredit + c3CourseCredit) 

print (f"Your GPA is {gpa}")
