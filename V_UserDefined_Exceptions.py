try:
    print("Student Result : ")
    Hin = int(input("Enter the marks of Hindi : "))
    if Hin < 0 or Hin > 100:
        raise ValueError("Marks cannot be more than zero")

    Eng = int(input("Enter the marks of English : "))
    if Eng < 0 or Eng > 100:
        raise ValueError("Marks cannot be less than zero and more than Hundred ")

    Maths = int(input("Enter the marks of Mathematics : "))
    if Maths < 0 or Maths > 100:
        raise ValueError("Marks cannot be less than zero and more than Hundred ")

    Phy = int(input("Enter the marks of Physics : "))
    if 0< Phy > 100:
        raise ValueError("Marks cannot be less than zero and more than Hundred ")

    Che = int(input("Enter the marks of Chemistry : "))
    if 0 < Che > 100:
        raise ValueError("Marks cannot be less than zero and more than Hundred ")



    total_marks = Hin + Eng + Maths + Phy + Che
    print("Total marks obtained by Student ", total_marks)

    percentage = (total_marks * 100) / 500
    print("Student gets ", percentage, "% marks")

    if percentage < 33:
        print("Student is Fail")
    elif percentage >= 33 and percentage < 45:
        print("Student pass with third division")
    elif percentage >= 45 and percentage < 60:
        print("Student pass with second division")
    else:
        print("Student pass with First division")


except ValueError as error:
    print("You cannot enter invalid input --> This error is : ", error)

except Exception as e:  # for unknown error and this error is bramhastra
    print("This error is called : ", e)

finally:
    print("Thanks for the result.")







