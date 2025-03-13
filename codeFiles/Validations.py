import re
class Valid:

    def checkTestName(self):

        while True:

            name = input("Enter the test name: ")
            abbr = input("Enter the abbreviation of the test name, for example -> LDL : ")

            full_name = name + " " + abbr
            checkName=name.lower().strip()
            checkAbbr=abbr.lower().strip()
            flag1=0
            flag2=0
            flag3=0
            flag4=0
            flag5=0


            if all(word.isalpha() for word in full_name.split()):

                with open("medicalTest",'r') as duplicateCheck:
                    for test in duplicateCheck:
                        Tname=test.split(";")[0].split(":")[1].split("(")[0].lower().strip()
                        Tabbr=test.split(";")[0].split(":")[1].split("(")[1].replace(")","").lower().strip()
                        if flag1 & flag2:
                            break

                        if checkName == Tname or Tabbr == checkAbbr:
                            print("you are trying to set a name or an abbreviation that is already exists in our medical tests!")
                            print()
                            with open("medicalTest",'r') as tests:
                                for t in tests:
                                    Tname = t.split(";")[0].split(":")[1].split("(")[0].lower().strip()
                                    Tabbr = t.split(";")[0].split(":")[1].split("(")[1].replace(")", "").lower().strip()

                                    if checkName == Tname and Tabbr == checkAbbr:
                                        print(t.split(";")[0].split(":")[1] + " <----------------- duplicated test detected")
                                        flag3=1



                                    elif checkName == Tname :
                                        print(t.split(";")[0].split(":")[1] + " <----------------- duplicated name detected")
                                        flag1=1
                                        flag4=1
                                    elif Tabbr == checkAbbr:


                                        print(t.split(";")[0].split(":")[1] + " <----------------- duplicated abbreviation detected")
                                        flag2=1
                                        flag5=1

                                    else:
                                        print(t.split(";")[0].split(":")[1] )

                                    if flag1 & flag2:
                                        break



                            print()
                            print("make sure you don't use one of the above names or abbreviations ")

                if flag3 or flag4 or flag5:
                    flag3 = 0
                    flag4 = 0
                    flag5 = 0
                    continue
                else:
                    break



            else:
                print()
                print("invalid test name, make sure it does not contain any numeric digits or special characters")
                print()


        full_name = name + " (" + abbr + ")"
        return full_name

    def checkRange(self):



        while True:

            print("your range can have a lower limit, upper limit, or both")
            print("for example < 30 , > 72 , < 100 > 14")
            print("do you want to enter the upper or the lower limit")
            print("1- lower limit")
            print("2- upper limit")
            option = int(input())

            if option == 1:
                lower = input("Enter the lower limit as a number without > : ")

                if not lower.isdigit():
                    print()

                    print("the limit cannot contain any non numeric value, make sure you only enter digits")
                    print()

                    continue
                else:
                    lower = int(lower)
                print()

                print("is there an upper limit in the range to enter?")
                decision = input("yes or no? : ")

                if decision.lower() == "yes":
                    upper = input("Enter the upper limit as a number without < : ")

                    if not upper.isdigit():
                        print()

                        print("the limit cannot contain any non numeric value, make sure you only enter digits")
                        print()

                        continue
                    else:
                        upper = int(upper)

                    if upper > lower:
                        return str(upper) + " " + str(lower)
                    else:
                        print()
                        print("the lower limit cannot be greater than or equal to the upper limit")
                        print()

                else:
                    return "L"+str(lower) # the L is added to identify it as an lower limit, so it can be assigned correctly in the main

            elif option == 2:
                upper = input("Enter the upper limit as a number without < : ")

                if not upper.isdigit():
                    print()
                    print("the limit cannot contain any non numeric value, make sure you only enter digits")
                    print()
                    continue
                else:
                    upper = int(upper)

                print("is there a lower limit in the range to enter?")
                decision = input("yes or no? : ")

                if decision.lower() == "yes":
                    lower = input("Enter the lower limit as a number without > : ")

                    if not lower.isdigit():
                        print()
                        print("the limit cannot contain any non numeric value, make sure you only enter digits")
                        print()
                        continue
                    else:
                        lower = int(lower)

                    if upper > lower:
                        return str(upper) + " " + str(lower)

                    else:
                        print("the lower limit cannot be greater than or equal to the upper limit")


                else:
                    return "U"+str(upper) # the U is added to identify it as an upper limit, so it can be assigned correctly in the main


            else:
                print()
                print("invalid option")
                print()


    def unitCheck(self):

        while True:

            unit = input("Enter the unit in the following format -> string/string or string string, for example mg/ml or mm Hg : ")

            parameters = r'[ /]'

            unit_parts = re.split(parameters,unit)

            if len(unit_parts) != 2:
                print()
                print("invalid unit, follow the given format")
                print()

            else:

                if unit_parts[0].isalpha() and unit_parts[1].isalpha():
                    if unit_parts[0] != unit_parts[1]:
                        return unit
                    else:
                        print()
                        print("the numerator and the denominator cannot be the same")
                        print()

                else:
                    print()
                    print("invalid unit, make sure no digits entered")
                    print()


    def TurnAroundCheck(self):

        while True:

            lengthFlag=0
            digitsFlag=0
            hoursFlag=0
            minutesFlag=0

            turnaround = input("Enter the turnaround time in the following format -> DD-hh-mm : ")

            parts = turnaround.split("-")

            if len(parts) != 3:
                print()
                print("invalid turnaround time, follow the given format")
                print()
                continue

            for i in range(3):
                if len(parts[i]) != 2:
                    print()
                    print("invalid entry,make sure that each part contains exactly two digits")
                    print()
                    lengthFlag = 1
                    break
                if not parts[i].isdigit():
                    print()
                    print("invalid entry, make sure not to use any non-numeric values or special characters")
                    print()
                    digitsFlag = 1
                    break

                if i == 1 and int(parts[i]) > 23:
                    print()
                    print("invalid hours numbers, the maximum number of hours is 23")
                    print()
                    hoursFlag = 1
                    break
                if i == 2 and int(parts[i]) > 59:
                    print()
                    print("invalid minutes numbers, the maximum number of minutes is 59")
                    print()
                    minutesFlag = 1
                    break

            if lengthFlag or digitsFlag or hoursFlag or minutesFlag:
                print("invalid input")
                continue
            else :
                return turnaround



    def combinationCheck(self): # to check the validty of the entered combination from the user in the filter part

        while True:
            print( "From the following menu, choose an option or a combination of options to filter the data based on them")
            print()
            print("1- patient ID")
            print("2- Test Name")
            print("3- Abnormal tests")
            print("4- Test added to the system within a specific period (start and end dates)")
            print("5- Test status")
            print("6- Test turnaround time within a period (minimum and maximum turnaround time")
            print()
            print("if you want to choose a combination, separate the options with commas as follow -> 1,5,3")
            combination = input("option/s: ")

            combination1 = combination.replace(" ","")
            combination2 = combination1.replace(",","")

            if all(option.isdigit() and int(option) < 7 for option in combination2):
               return combination1.replace(",","")
            else:
                print("stick to the given format, and only choose numbers from 1 to 6")
                continue




    def IDCheck(self):


        while True:
            print("Enter the patient ID")
            print("make sure it is a 7 digits number")
            ID = input("ID: ")

            if ID.isdigit() and len(ID) == 7:
                with open("medicalRecord", 'r') as data:
                    for record in data:
                        if ID in record:
                            return ID

                    print(f"The id {ID} does not exist in our records")
                    continue


            else:
                print("Invalid ID, make sure it is a 7 digits number")


    def PeriodCheck(self):

        while True:
            print()
            print("use the following format while entering the date -> YYYY-MM-DD")

            start_date = input("Enter the start date of the period: ")

            if len(start_date.split("-")) != 3:
                print("there is a missing or an extra part in the date, stick to the given format")
                continue

            year1 = start_date.split("-")[0]
            month1 = start_date.split("-")[1]
            day1 = start_date.split("-")[2]

            if year1.isdigit() and int(len(year1)) == 4:
                pass
            else:
                print("stick to the given format, invalid start year ")
                continue

            if month1.isdigit() and int(len(month1)) == 2 and int(month1) <= 12 and int(month1) > 0:
                pass
            else:
                print("stick to the given format, invalid month ")
                continue

            if day1.isdigit() and int(len(day1)) == 2 :
                pass
            else:
                print("stick to the given format, invalid day")
                continue


            end_date = input("Enter the end date of the period: ")
            if len(end_date.split("-")) != 3:
                print("there is a missing or an extra part in the date, stick to the given format")
                continue


            year2 = end_date.split("-")[0]
            month2 = end_date.split("-")[1]
            day2 = end_date.split("-")[2]


            if year2.isdigit() and int(len(year2)) == 4:
                pass
            else:
                print("stick to the given format, invalid end year ")
                continue



            if month2.isdigit() and int(len(month2)) == 2 and int(month2) <= 12 and int(month2) > 0:
                pass
            else:
                print("stick to the given format, invalid month ")
                continue


            if day2.isdigit() and int(len(day2)) == 2 :
                pass
            else:
                print("stick to the given format, invalid day")
                continue


            date1 = start_date.replace("-","")
            date2 = end_date.replace("-","")

            if date1 > date2 or date1 == date2:
                print("the start date must be before the end date")
                continue

            else:
                return start_date + " " + end_date








