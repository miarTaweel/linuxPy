from datetime import datetime
import pytz
class RecordInsertion:

    ID=""
    name=""
    date_time=""
    value=""
    unit=""
    status=""


    def insert(self):

        newRecord=""

        while True:

            self.ID =self.validID()
            self.name = self.validName()
            print(self.name)
            self.date_time= self.validDateTime()
            self.value = self.validValue()

            with open("medicalTest",'r') as data:
                for record in data:
                    if self.name in record:
                        self.unit = record.split(";")[2].split(":")[1].split(",")[0]

            self.status = self.validStatus(self.name,self.date_time)

            newRecord = self.ID+": "+self.name+", "+self.date_time+", "+str(self.value)+", "+self.unit.strip()+", "+self.status

            print()

            with open("medicalRecord", 'a') as output:
                output.write('\n'+newRecord)

            break

        print(f"The new record: {newRecord} ,is inserted successfully" )


    def validID(self):

         while True:
             print("Enter the patient ID")
             print("make sure it is a 7 digits number")
             ID = input("ID: ")

             if ID.isdigit() and len(ID) == 7:

                return ID


             else:
                 print("Invalid ID, make sure it is a 7 digits number")

    def validName(self):

        TestsNames = []
        test_name = ""

        while True:

            with open("medicalTest", 'r') as tests:
                for test in tests:
                    name = test.split(";")[0].split(":")[1]
                    TestsNames.append(name)

            print("Choose one of the tests below: ")
            index = 1
            for j in TestsNames:
                print(str(index) + "- " + str(j))
                index = index + 1
            option = input("option: ")
            if option.isdigit() and int(option) >= 1 and int(option) <= len(TestsNames):
                test_name = TestsNames.pop(int(option) - 1)
                break
            else:
                TestsNames = []
                test_name = ""
                print("make sure you are choosing one of the listed options!")

        return str(test_name).split("(")[1].replace(")", "")

    def validDateTime(self):

        while True:
            print()
            print("use the following format while entering the date -> YYYY-MM-DD")

            date = input("Enter the  date of the test: ")
            if len(date.split("-")) != 3:
                print("there is a missing or an extra part in the date, stick to the given format")
                continue
            year = date.split("-")[0]
            month = date.split("-")[1]
            day = date.split("-")[2]



            if year.isdigit() and int(len(year)) == 4:
                pass
            else:
                print("stick to the given format, invalid year ")
                continue

            if month.isdigit() and int(len(month)) == 2 and int(month) <= 12 and int(month) > 0:
                pass
            else:
                print("stick to the given format, invalid month ")
                continue

            if day.isdigit() and int(len(day)) == 2 and int(day) <= 31:
                pass
            else:
                print("stick to the given format, invalid day")
                continue

            today = datetime.now().date()
            input_date = datetime.strptime(date, "%Y-%m-%d").date()

            if input_date > today:
                print("This date hasn't come yet , Please enter a valid date")
                continue
            else:
                pass

            break




        while True:

            print()
            print("use the following format while entering the time -> HH:MM")

            time = input("Enter the time of the test: ")
            if len(time.split(":")) != 2:
                print("there is a missing or an extra part in the date, stick to the given format")
                continue
            hour = time.split(":")[0]
            minutes = time.split(":")[1]

            if hour.isdigit() and int(len(hour)) <= 23 and int(len(hour)) >= 00 and len(hour) == 2:
                pass
            else:
                print("invalid hour")
                continue

            if minutes.isdigit() and int(len(minutes)) <= 59 and int(len(minutes)) >= 00 and len(minutes) == 2:
                pass
            else:
                print("invalid minutes")
                continue

            fullDate = date + " " + time
            palestine = pytz.timezone('Asia/Gaza')
            now = datetime.now(palestine)
            input_date = palestine.localize(datetime.strptime(fullDate, "%Y-%m-%d %H:%M"))

            if input_date > now :
                print("This time hasn't come yet , Please enter a valid time")
                continue
            else:
                pass

            break

        return date+ " " + time

    def validValue(self):

        while True:
            value= input("enter the value of the test: ")

            if self.is_positive_integer_or_float(value):
                value = float(value)
                return value


            else:
                print("invalid value, make sure it either an int or float, with no non-numeric characters")

    def is_positive_integer_or_float(self,s):
        try:
            # Convert the string to a float
            num = float(s)
            # Check if the number is positive and not negative
            if num > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def is_leap_year(self,year):
        if (int(year) % 4 == 0):
            if (int(year) % 100 == 0):
                if (int(year) % 400 == 0):
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False



    def validStatus(self,name,date_time):

        while True:

            turnaround=""

            print("Choose the test's status")
            print("1- Pending")
            print("2- Completed")
            print("3- Reviewed")
            option = input("option: ")

            if int(option) == 1:
                status = "pending"
                return status
            elif int(option) == 2:
                status = "completed, "

                with open("medicalTest",'r') as data:
                    for test in data:
                        if name in test:
                            turnaround= test.split(";")[2].split(":")[1].split(",")[1]
                            turnaround_days = turnaround.split("-")[0]
                            turnaround_hours = turnaround.split("-")[1]
                            turnaround_minutes = turnaround.split("-")[2]


                date = date_time.split()[0]
                time = date_time.split()[1]

                date_year = date.split("-")[0]
                date_month = date.split("-")[1]
                date_day = date.split("-")[2]

                time_hours = time.split(":")[0]
                time_minutes = time.split(":")[1]


                new_hours= int(time_hours) + int(turnaround_hours)
                new_minutes = int(turnaround_minutes) + int(time_minutes)
                new_day = int(date_day) + int(turnaround_days)
                new_month = int(date_month)
                new_year = int(date_year)

                ThirtyOneDays=[1,3,5,7,8,10,12]
                ThirtyDays = [4, 6, 9, 11]
                TwentyEightdays =[2]

                if int(new_minutes) > 59:

                    minuteCheck1 = int(new_minutes) % 59 # to check if we exceeded the minutes limit, so we can add 1 to the hours part
                    minuteCheck2 = int(new_minutes) / 59

                    new_minutes = minuteCheck1
                    new_hours = int(new_hours) + int(minuteCheck2)



                if int(new_hours) > 23 :

                    hourCheck1 = int(new_hours)%23#23:59
                    hourCheck2 = int(new_hours) / 23

                    new_hours = int(hourCheck1) -1
                    new_day = int(new_day) + int(hourCheck2)
                    print(new_day)


                if int(new_day) > 31 and new_month in ThirtyOneDays: # for the months with 31 days

                    dayCheck1 = int(new_day) %31
                    dayCheck2 = int(new_day)/31

                    new_day  = dayCheck1
                    new_month = int(new_month) + int(dayCheck2)


                if int(new_day) == 31 and new_month in ThirtyDays: # for the months with 31 days


                    new_day  = 1
                    new_month = int(new_month) + 1


                if int(new_day) > 30 and new_month in ThirtyDays: # for the months with 30 days



                    dayCheck1 = int(new_day) %30
                    dayCheck2 = int(new_day)/30

                    new_day  = dayCheck1
                    new_month = int(new_month) + int(dayCheck2)



                if int(new_day) > 28 and new_month in TwentyEightdays: # for the months with 28 days

                    if int(new_day) ==29 and self.is_leap_year(new_year):
                        new_day = 29
                        new_month = 2

                    else:

                        dayCheck1 = int(new_day) % 28
                        dayCheck2 = int(new_day) / 28
                        new_day = (int(new_day) +dayCheck1 ) % int(new_day)
                        new_month = int(new_month) + int(dayCheck2)



                if int(new_month) > 12 :

                    monthCheck1 = int(new_month) %12
                    monthCheck2 = int(new_month)/12

                    new_month = monthCheck1
                    new_year = int(new_year) + int(monthCheck2)


                if len(str(new_minutes)) ==1:
                    new_minutes = "0"+str(new_minutes)

                if len(str(new_hours)) ==1:
                    new_hours = "0"+str(new_hours)

                if len(str(new_day)) ==1:
                    new_day = "0"+str(new_day)

                if len(str(new_month)) ==1:
                    new_month = "0"+str(new_month)


                status = status + str(new_year) +"-"+str(new_month)+"-"+str(new_day)+" "+ str(new_hours)+":"+str(new_minutes)
                return status



            elif int(option) == 3:
                status = "reviewed"
                return  status
            else:
                print("invalid option")
                continue


    def updateStatus(self,name,date_time,suggestedTA,flag):

        while True:

            turnaround=""
            status = "completed, "

            with open("medicalTest", 'r') as data:
                for test in data:
                    if name in test:
                        if flag ==1:
                            turnaround=suggestedTA
                            turnaround_days = turnaround.split("-")[0]
                            turnaround_hours = turnaround.split("-")[1]
                            turnaround_minutes = turnaround.split("-")[2]

                        else:
                            turnaround = test.split(";")[2].split(":")[1].split(",")[1]
                            turnaround_days = turnaround.split("-")[0]
                            turnaround_hours = turnaround.split("-")[1]
                            turnaround_minutes = turnaround.split("-")[2]




            date = date_time.split()[0]
            time = date_time.split()[1]

            date_year = date.split("-")[0]
            date_month = date.split("-")[1]
            date_day = date.split("-")[2]

            time_hours = time.split(":")[0]
            time_minutes = time.split(":")[1]

            new_hours = int(time_hours) + int(turnaround_hours)
            new_minutes = int(turnaround_minutes) + int(time_minutes)
            new_day = int(date_day) + int(turnaround_days)
            new_month = int(date_month)
            new_year = int(date_year)

            ThirtyOneDays = [1, 3, 5, 7, 8, 10, 12]
            ThirtyDays = [4, 6, 9, 11]
            TwentyEightdays = [2]

            if int(new_minutes) > 59:
                minuteCheck1 = int(
                    new_minutes) % 59  # to check if we exceeded the minutes limit, so we can add 1 to the hours part
                minuteCheck2 = int(new_minutes) / 59

                new_minutes = minuteCheck1
                new_hours = int(new_hours) + int(minuteCheck2)

            if int(new_hours) > 23:
                hourCheck1 = int(new_hours) % 23
                hourCheck2 = int(new_hours) / 23

                new_hours = int(hourCheck1) - 1
                new_day = int(new_day) + int(hourCheck2)
                print(new_day)

            if int(new_day) > 31 and new_month in ThirtyOneDays:  # for the months with 31 days

                dayCheck1 = int(new_day) % 31
                dayCheck2 = int(new_day) / 31

                new_day = dayCheck1
                new_month = int(new_month) + int(dayCheck2)

            if int(new_day) == 31 and new_month in ThirtyDays:  # for the months with 31 days

                new_day = 1
                new_month = int(new_month) + 1

            if int(new_day) > 30 and new_month in ThirtyDays:  # for the months with 30 days

                dayCheck1 = int(new_day) % 30
                dayCheck2 = int(new_day) / 30

                new_day = dayCheck1
                new_month = int(new_month) + int(dayCheck2)

            if int(new_day) > 28 and new_month in TwentyEightdays:  # for the months with 28 days

                if int(new_day) == 29 and self.is_leap_year(new_year):
                    new_day = 29
                    new_month = 2

                else:

                    dayCheck1 = int(new_day) % 28
                    dayCheck2 = int(new_day) / 28
                    new_day = (int(new_day) + dayCheck1) % int(new_day)
                    new_month = int(new_month) + int(dayCheck2)

            if int(new_month) > 12:
                monthCheck1 = int(new_month) % 12
                monthCheck2 = int(new_month) / 12

                new_month = monthCheck1
                new_year = int(new_year) + int(monthCheck2)

            if len(str(new_minutes)) == 1:
                new_minutes = "0" + str(new_minutes)

            if len(str(new_hours)) == 1:
                new_hours = "0" + str(new_hours)

            if len(str(new_day)) == 1:
                new_day = "0" + str(new_day)

            if len(str(new_month)) == 1:
                new_month = "0" + str(new_month)

            status = status + str(new_year) + "-" + str(new_month) + "-" + str(new_day) + " " + str(
                new_hours) + ":" + str(new_minutes)
            return status







