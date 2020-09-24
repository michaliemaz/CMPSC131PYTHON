# Author: Michalie Mazurkivich mpm6778@psu.edu

def getGradePoint(letterGrade):
  if letterGrade == 'A':
    gradePointNum = 4.0
  elif letterGrade == 'A-':
    gradePointNum = 3.67
  elif letterGrade == 'B+':
    gradePointNum = 3.33
  elif letterGrade == 'B':
    gradePointNum = 3.0
  elif letterGrade == 'B-':
    gradePointNum = 2.67
  elif letterGrade == 'C+':
    gradePointNum = 2.33
  elif letterGrade == 'C':
    gradePointNum = 2.0
  elif letterGrade == 'D':
    gradePointNum = 1.0
  else:
    gradePointNum = 0.0
  gradePointNum = float(gradePointNum)
  return(gradePointNum)
  return 0.0

def calcGPA(gradepoint1, credit1, gradepoint2, credit2, gradepoint3, credit3):
  GPA = (gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3)
  return(GPA)

def run():
  n=1
  while (n<=3):
    letterGrade = input(f"Enter your course {n} letter grade: ")
    credit = input(f"Enter your course {n} credit: ")
    gradepoint = getGradePoint(letterGrade)
    print (f"Grade point for course {n} is: {gradepoint}")
    credit = float(credit)
    if (n==1):
      gradepoint1 = gradepoint
      credit1 = credit
    elif (n==2):
      gradepoint2 = gradepoint
      credit2 = credit
    elif (n==3):
      gradepoint3 = gradepoint
      credit3 = credit
    n = n+1

  GPA = calcGPA (gradepoint1, credit1, gradepoint2, credit2, gradepoint3, credit3)
  print (f"Your GPA is: {GPA}")
  return

if __name__ == "__main__":
  run()