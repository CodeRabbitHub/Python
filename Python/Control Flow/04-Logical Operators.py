# and - or -  not

high_income = True
good_credit = False
student = True

if high_income and good_credit:
    print("Eligible")
elif (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligible")
