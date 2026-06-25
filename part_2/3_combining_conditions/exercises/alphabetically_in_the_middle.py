char_1 = input("1st letter: ")
char_2 = input("2nd letter: ")
char_3 = input("3rd letter: ")

if (char_1 < char_2 and char_1 < char_3) and char_2 < char_3:
    print("The letter in the middle is", char_2)
elif (char_2 < char_1 and char_2 < char_3) and char_3 < char_1:
    print("The letter in the middle is", char_3)
elif (char_2 < char_1 and char_2 < char_3) and char_1 < char_3:
    print("The letter in the middle is", char_1)
elif (char_3 < char_1 and char_3 < char_2) and char_1 < char_2:
    print("The letter in the middle is", char_1)
elif (char_3 < char_1 and char_3 < char_2) and char_2 < char_1:
    print("The letter in the middle is", char_2)
elif (char_1 < char_2 and char_1 < char_3) and char_3 < char_2:
    print("The letter in the middle is", char_3)
