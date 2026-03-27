score = float(input("Enter the sctudent score: "))
if (100 >= score >= 80):
    print("Grade A")
elif 79 >= score >= 70:
    print("Grade B")
elif 69 >= score >= 60:
    print("Grade C")
elif 59 >= score >= 50:
    print("Grade D")
elif 49 >= score >= 40:
    print("Grade E")
else:
    print("Grade F")
