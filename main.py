# li = [1, 2, 3]
# programming_dictionary = {
#   "Bug": "An error in a program that prevents the program from running as expected.", 
#   "Function": "A piece of code that you can easily call over and over again.",
#   "Loop": "The act of doing something over and over again"  
# }

# pd = programming_dictionary
# pdf = {
#   li[0]: "first item corr to li[0]"
# }
# pdf[li[1]] = "second item corr to li[1]"
# pd["Argument"] = "Data sent to a function from a calling function"
# mylist1 = []
# mylist2 = []
# for key in pd:
#   print(key)
#   mylist1.append(key)
#   mylist2.append(pd[key])

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
def decide_grade(score):
# This is the scoring criteria:
# Scores 91 - 100: Grade = "Outstanding"
# Scores 81 - 90: Grade = "Exceeds Expectations"
# Scores 71 - 80: Grade = "Acceptable"
# Scores 70 or lower: Grade = "Fail"
  if score <= 70:
    return("Fail")
  elif score <= 80:
    return("Acceptable")
  elif score <= 90:
    return("Exceeds Expectations")
  else:
    return("Outstanding")
  return(grade)
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  student_grades[key] = decide_grade(student_scores[key])

# 🚨 Don't change the code below 👇
print(student_grades)