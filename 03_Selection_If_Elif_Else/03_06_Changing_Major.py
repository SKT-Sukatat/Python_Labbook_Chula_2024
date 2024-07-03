student_1, gpax_1, cp_1, cal1_1, cal2_1 = input().split()
student_2, gpax_2, cp_2, cal1_2, cal2_2 = input().split()

if cp_1 == 'A' and cal1_1 <= 'C' and cal2_1 <= 'C':
    result_1 = True
else:
    result_1 = False

if cp_2 == 'A' and cal1_2 <= 'C' and cal2_2 <= 'C':
    result_2 = True
else:
    result_2 = False

if (result_1 == result_2) and (result_1 == True):
    if gpax_1 > gpax_2:
        result_1, result_2 = True, False
    elif gpax_1 < gpax_2:
        result_1, result_2 = False, True
    elif gpax_1 == gpax_2:
        if cal1_1 < cal1_2:
            result_1, result_2 = True, False
        elif cal1_1 > cal1_2:
            result_1, result_2 = False, True
        elif cal1_1 == cal1_2:
            if cal2_1 < cal2_2:
                result_1, result_2 = True, False
            elif cal2_1 > cal2_2:
                result_1, result_2 = False, True
            elif cal2_1 == cal2_2:
                result_1, result_2 = True, True

if result_1 == True and result_2 == False:
    print(student_1)
elif result_1 == False and result_2 == True:
    print(student_2)
elif result_1 == True and result_2 == True:
    print("Both")
else:
    print("None")