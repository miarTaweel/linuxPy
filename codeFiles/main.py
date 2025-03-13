from Validations import Valid
from Filter import Filter
from RecordInsertion import RecordInsertion
from UpdateRecord import UpdateRecord
from UpdateTest import UpdateTest
from summary import summary
import csv
import os
import time
valid =Valid()
filter=Filter()
summary=summary()
updateTest=UpdateTest()
updateRecord=UpdateRecord()
record_insert = RecordInsertion()
i=0
flag=0
recordsFile="medicalRecord"
testsFile="medicalTest"
dataFile="data.csv"
emptyData=0
filteredFile="Filtered"
path=os.path.abspath(__file__)
directory=os.path.dirname(path)

medicalRecord=os.path.join(directory,recordsFile)

if os.path.exists(dataFile):
    if os.path.getsize(dataFile)==0:
        emptyData=1
else:
    print()
    print("the data.csv file does not exist, which will cause a problem in importing and exporting the data")
    print("create one and try again")
    exit("forced exiting")



if os.path.exists(testsFile):

    if os.path.getsize(testsFile) == 0:
        print()
        print("the file medicalTest is empty, fill it with proper data to use our program")
        exit("Exiting the program")
    else:
        print()
        print("the medicalTest file is loaded successfully")
        print()
else:
    print()
    print("the file medicalTest does not exist")
    print("do you want to create the mentioned file?")
    decision=input("yes or no: ").strip().lower()
    if decision == "yes":
        print()
        print("creating the medicalTest file...")
        time.sleep(2)
        with open("medicalTest",'w') as createFile:
            pass
        print()
        print("the medicalTest file has been created successfully")
        print("fill it with proper data to use our program")
        exit("Exiting the program")

    else:
        print()
        print("you can not proceed in using the program without this file")
        exit("Exiting the program")


if os.path.exists(recordsFile):

    if os.path.getsize(recordsFile) == 0:
        print()
        print("the medicalRecord file is empty, you can't use our program unless you fill it")
        if emptyData == 0:
            print("we can fill it for you by importing the records from the comma separated file")
            choice=input("proceed? yes or no: ").strip().lower()
            if choice == "yes":
                print("importing...")
                print("Data imported successfully...")
                print("")
                with open("data.csv", 'r') as input_file:
                    csv_read = csv.reader(input_file)

                    with open("medicalRecord", 'w') as output_file:
                        for row in csv_read:

                            if any(row):
                                record = f"{row[0]}: {row[1]},{row[2]},{row[3]},{row[4]},{row[5]}"
                                if len(row) > 6:
                                    record += f",{row[6]}"
                                output_file.write(record + '\n')
            else:
                 exit("Exiting the program")
        else:
            exit("Exiting the program")
    else:
        print()
        print("the medicalRecord file is loaded successfully")
        print()
else:
    print()
    print("the medicalRecord file does not exist")
    print("do you want to create the mentioned file?")
    decision=input("yes or no: ").strip().lower()
    if decision == "yes":
        print()
        print("creating the medicalRecord file...")
        time.sleep(2)
        with open("medicalRecord", 'w') as createFile:
            pass
        print()
        print("the medicalRecord file has been created successfully")
        if emptyData == 0:
            print("we can fill it for you by importing the records from the comma separated file")
            choice = input("proceed? yes or no").strip().lower()
            if choice == "yes":
                print("importing...")
                print("Data imported successfully...")
                print("")
                with open("data.csv", 'r') as input_file:
                    csv_read = csv.reader(input_file)

                    with open("medicalRecord", 'w') as output_file:
                        for row in csv_read:

                            if any(row):
                                record = f"{row[0]}: {row[1]},{row[2]},{row[3]},{row[4]},{row[5]}"
                                if len(row) > 6:
                                    record += f",{row[6]}"
                                output_file.write(record + '\n')
            else:
                exit("Exiting the program")
        else:
            exit("Exiting the program")

    else:
        print()
        print("you can not proceed in using the program without this file")
        if emptyData == 0:
            print("we can fill it for you by importing the records from the comma separated file")
            choice = input("proceed? yes or no").strip().lower()
            if choice == "yes":
                print("importing...")
                print("Data imported successfully...")
                print("")
                with open("data.csv", 'r') as input_file:
                    csv_read = csv.reader(input_file)

                    with open("medicalRecord", 'w') as output_file:
                        for row in csv_read:

                            if any(row):
                                record = f"{row[0]}: {row[1]},{row[2]},{row[3]},{row[4]},{row[5]}"
                                if len(row) > 6:
                                    record += f",{row[6]}"
                                output_file.write(record + '\n')
            else:
                exit("Exiting the program")
        else:
            exit("Exiting the program")


if os.path.exists(filteredFile):
    pass
else:
    with open("Filtered",'w') as filter:
        pass




print("Welcome to our medical system")

while i != 9:
    print("choose an option: ")
    print("1- Add a new medical test ")
    print("2- Add a new medical test record ")
    print("3- Update patient records ")
    print("4- Update a medical test ")
    print("5- Filter medical tests ")
    print("6- Summary reports ")
    print("7- Export medical records to a CSV file ")
    print("8- Import medical records from a CSV file ")
    print("9- Exit ")
    print()
    option = input("option: ")

    if option == "1":
        print("add a new medical test:")
        TestName = valid.checkTestName()
        print()
        TestRange = valid.checkRange()
        numOfLimits = len(TestRange.split())
        upper=""
        lower=""
        if numOfLimits == 2:
            upper = "< " + TestRange.split()[0]
            lower = "> " + TestRange.split()[1] +", "

        else:
            if TestRange[0] == "L":
                lower = "> " + TestRange[1:] # from 1 to the end, to remove the L that was added to identify it as Lower
            elif TestRange[0] == "U":
                upper = "< " + TestRange[1:] # from 1 to the end, to remove the U that was added to identify it as upper


        print()
        TestUnit = valid.unitCheck()
        print()
        print("if a test needs 2 days, 5 hours, and 10 minutes to be completed and results are obtained")
        print("then the test turnaround time is 02-05-10")
        print()
        TestTurnAround = valid.TurnAroundCheck()
        print()
        tests_file1 = open("medicalTest",'r')
        tests_file2 = open("medicalTest", 'a')
        index = len(tests_file1.readlines()) +1
        test = str(index) + ". " + "Name: " + TestName + "; " + "Range: " + lower + upper + "; " + "Unit: " + TestUnit +", " + TestTurnAround
        tests_file2.write('\n'+test)
        print(f"The new test: {test} ,is inserted successfully")
        flag=0


    elif option == "2":
        print("add a new medical record")

        record_insert.insert()
        flag=0





    elif option == "3":
        print("update patient records")

        updateRecord.updateRecord()
        flag=0

    elif option == "4":
        print("update a medical test")

        updateTest.testUpdate()
        flag=0

    elif option == "5":
        print("filter")

        combination = valid.combinationCheck()

        filter.filterOut(combination)
        flag=1



    elif option == "6":
        print("summary")

        while True:
            if flag==1:
                print("Would you like to use the last filtered reports to create a summary?")
                print("Yes or no")
                ans=input().lower()
                if(ans=="yes"):
                    summary.summarise()
                    break
                elif (ans=="no"):
                    combination = valid.combinationCheck()
                    filter.filterOut(combination)
                    summary.summarise()
                    break
                else:
                    print("invalid input")
            else:
                combination = valid.combinationCheck()
                filter.filterOut(combination)
                summary.summarise()
                break


        



    elif option == "7":
        print("exporting.....")
        print("Data Exported successfully...")
        print("")

        with open("medicalRecord", 'r') as input_file:

            with open("data.csv", 'w') as output_file:
                csv_write=csv.writer(output_file)


                for row in input_file:
                    id_part, rest_of_record = row.split(': ', 1)
                    record=[id_part] +rest_of_record.strip().split(",")
                    csv_write.writerow(record)



    elif option == "8":
        print("importing...")
        print("Data imported successfully...")
        print("")
        with open("data.csv", 'r') as input_file:
            csv_read=csv.reader(input_file)

            with open("medicalRecord", 'w') as output_file:
                for row in csv_read:

                    if any(row):
                        record =f"{row[0]}: {row[1]},{row[2]},{row[3]},{row[4]},{row[5]}"
                        if len(row) > 6:
                            record += f",{row[6]}"
                        output_file.write(record+'\n')




    elif option == "9":
        print("exit")
        break
    else:
        print("invalid option")
        continue