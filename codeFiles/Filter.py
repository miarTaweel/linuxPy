from Validations import Valid
from RecordInsertion import RecordInsertion
valid=Valid()
recordname=RecordInsertion()
class Filter:

    def filterOut(self,options):

        matchedRecords=[]
        TestsNames =[]

        with open("medicalRecord", 'r') as source:
            with open("Filtered", 'w') as destination:
                content = source.read()
                destination.write(content)

        i=0
        while i < len(options):


            if int(options[i]) == 1:
                ID = valid.IDCheck()

                with open("Filtered",'r') as data:
                    for record in data:
                        if ID in record:
                            matchedRecords.append(record.strip())

                with open("Filtered",'w') as delete: # to empty the file and store a new data
                    pass


                with open("Filtered",'a') as result:
                    for record in matchedRecords:
                        result.write(record + '\n')



            if int(options[i]) == 2:

                matchedRecords=[]

               # with open("medicalTest",'r') as tests:
                    #for test in tests:
                       # name = test.split(";")[0].split()[2].replace("(","").replace(")","")
                      #  TestsNames.append(name)

              #  print("Choose one of the tests below: ")
               # index=1
               # for j in TestsNames:
                 #   print(str(index)+"- "+ j)
                   # index = index +1
               # option=input("option: ")
               # test_name=TestsNames.pop(int(option)-1)

                test_name=recordname.validName()

                with open("Filtered",'r') as data:
                    for record in data:
                        if test_name in record:
                            matchedRecords.append(record.strip())

                with open("Filtered", 'w') as delete:  # to empty the file and store a new data
                    pass

                with open("Filtered", 'a') as result:
                    for record in matchedRecords:
                        result.write(record + '\n')


            if int(options[i]) == 3:
                matchedRecords=[]
                upper=""
                lower=""


                with open("Filtered",'r') as data:
                    for record in data:
                        name = record.split(",")[0].split()[1]

                        with open("medicalTest", 'r') as tests:
                            for test in tests:
                                if name in test:
                                    range=test.split(";")[1].split(":")[1]
                                    value=record.split(",")[2]
                                    if len(range.split(",")) == 2: # if two limits exist
                                        upper=range.split(",")[1].replace("<","").replace(" ","")
                                        lower=range.split(",")[0].replace(">","").replace(" ","")

                                    elif len(range.split("<")) == 2:
                                        upper=range.replace("<","").replace(" ","").replace(",","")
                                        lower=0

                                    elif len(range.split(">")) == 2:
                                        lower=range.replace(">","").replace(" ","").replace(",","")
                                        upper=0





                                    if float(value) > float(upper) or float(value) < float(lower):
                                        matchedRecords.append(record.strip())



                with open("Filtered", 'w') as delete:  # to empty the file and store a new data
                    pass

                with open("Filtered", 'a') as result:
                    for record in matchedRecords:
                        result.write(record + '\n')



            if int(options[i]) == 4:

                period = valid.PeriodCheck()
                start_date = period.split()[0]
                end_date = period.split()[1]

                start_date = start_date.replace("-","")
                end_date = end_date.replace("-","")

                matchedRecords = []


                with open("Filtered", 'r') as data:
                    for record in data:
                        date = record.split(",")[1].split()[0]
                        date = date.replace("-","")

                        if start_date <= date and end_date >= date:
                            matchedRecords.append(record.strip())


                with open("Filtered", 'w') as delete:  # to empty the file and store a new data
                    pass

                with open("Filtered", 'a') as result:
                    for record in matchedRecords:
                        result.write(record + '\n')



            if int(options[i]) == 5:

                while True:
                    status=""
                    matchedRecords=[]

                    print("What is the status that you're searching for")
                    print("1- Pending")
                    print("2- Completed")
                    print("3- Reviewed")
                    option = input("option: ")

                    if int(option) == 1:
                        status = "pending"
                    elif int(option) == 2:
                        status = "completed"
                    elif int(option) == 3:
                        status = "reviewed"
                    else:
                        print("invalid option")
                        continue

                    with open("Filtered", 'r') as data:
                        for record in data:
                            if status in record:
                                matchedRecords.append(record.strip())

                        break

                with open("Filtered", 'w') as delete:  # to empty the file and store a new data
                    pass

                with open("Filtered", 'a') as result:
                    for record in matchedRecords:
                        result.write(record + '\n')






            if int(options[i]) == 6:

                matchedRecords=[]

                print()
                print("if a test needs 2 days, 5 hours, and 10 minutes to be completed and results are obtained")
                print("then the test turnaround time is 02-05-10")
                print()

                while True:
                    print("Enter the minimum turnaround time")
                    minimum = valid.TurnAroundCheck()
                    print("Enter the maximum turnaround time")
                    maximum = valid.TurnAroundCheck()

                    min = minimum.replace("-", "")
                    max = maximum.replace("-", "")

                    if min == max or int(min) > int(max):
                        print("invalid entries, the maximum turnaround time must be greater than the minimum")
                        continue

                    with open("Filtered", 'r') as data:
                        for record in data:
                            name = record.split(",")[0].split()[1]

                            with open("medicalTest", 'r') as tests:
                                for test in tests:
                                    if name in test:
                                        turnaround = test.split(";")[2].split(",")[1]
                                        turnaround = turnaround.replace("-","")
                                        if int(turnaround) >= int(min) and int(turnaround) <= int(max):
                                            matchedRecords.append(record.strip())

                    with open("Filtered", 'w') as delete:  # to empty the file and store a new data
                        pass

                    with open("Filtered", 'a') as result:
                        for record in matchedRecords:
                            result.write(record + '\n')

                    break



            i = i + 1
        print()
        for record in matchedRecords:
            print(record)
        print()