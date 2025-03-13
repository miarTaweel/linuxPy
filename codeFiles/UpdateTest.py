from RecordInsertion import RecordInsertion
recordname=RecordInsertion()
from Validations import Valid
valid=Valid()
class UpdateTest:

    def testUpdate(self):
        TestsNames = []
        test_name = ""
        fields = []
        index = 0

        while True:

            with open("medicalTest", 'r') as data:
                file_tests = data.readlines()

            ToUpdate = ["Test Name", "Test normal Range", "Test Unit", "Test turnaround"]

            test_name = recordname.validName()

            with open("medicalTest", 'r') as tests:
                for test in tests:
                    if test_name in test:
                        for i, field in enumerate(ToUpdate):
                            print(f"{i + 1}- {field}")

                        # Loop to handle invalid option for fieldToUpdate
                        fieldToUpdate = input("Choose the field that you want to update or 0 to quit: ")

                        while not fieldToUpdate.isdigit() or int(fieldToUpdate) < 0 or int(fieldToUpdate) > len(ToUpdate):
                            print()
                            print("Invalid option. Please choose a valid field number.")
                            print()
                            fieldToUpdate = input("Choose the field that you want to update or 0 to quit: ")

                        fieldToUpdate = int(fieldToUpdate)

                        if fieldToUpdate == 0:
                            return  # Exit the function if the user chooses to quit

                        fieldToUpdate =fieldToUpdate- 1  # Adjust to 0-based index

                        fields.insert(0, test.split(";")[0].split(":")[0].split(".")[1] + ": ")
                        fields.insert(1, test.split(";")[0].split(":")[1] + "; ")
                        fields.insert(2, test.split(";")[1].split(":")[0] + ": ")
                        fields.insert(3, test.split(";")[1].split(":")[1] + "; ")
                        fields.insert(4, test.split(";")[2].split(":")[0] + ": ")
                        fields.insert(5, test.split(";")[2].split(":")[1].split(",")[0] + ", ")
                        fields.insert(6, test.split(";")[2].split(":")[1].split(",")[1])


                        for i, record in enumerate(file_tests):

                            fields = [part.strip() for part in fields]  # Remove any unintentional spaces

                            if test_name in record:

                                if fieldToUpdate == 0:
                                    print(f"the current test name is : {fields[1]}")
                                    print()
                                    old_name = fields[1]
                                    fields[1] = valid.checkTestName() + ";"
                                    new_name = fields[1]
                                    self.updateRecordsNames(old_name, new_name)
                                    print()
                                    print(f"the new test name is : {fields[1]}")
                                    print()
                                    index = i
                                    break

                                elif fieldToUpdate == 1:

                                    print(f"the current test normal range is : {fields[3]}")
                                    print("Enter the new Range")
                                    print()
                                    fields[3] = valid.checkRange()
                                    TestRange = fields[3]
                                    numOfLimits = len(TestRange.split())
                                    upper = ""
                                    lower = ""
                                    if numOfLimits == 2:
                                        upper = "< " + TestRange.split()[0]
                                        lower = "> " + TestRange.split()[1] + ", "
                                    else:
                                        if TestRange[0] == "L":
                                            lower = "> " + TestRange[1:]
                                        elif TestRange[0] == "U":
                                            upper = "< " + TestRange[1:]
                                    fields[3] = lower + upper + ";"
                                    print()
                                    print(f"the new test normal range is : {fields[3]}")
                                    print()
                                    index = i
                                    break

                                elif fieldToUpdate == 2:

                                    print(f"the current test unit is : {fields[5]}")
                                    print()
                                    old_unit = fields[5]
                                    fields[5] = valid.unitCheck() + ","
                                    print()
                                    self.updateRecordsUnit(fields[1], old_unit, fields[5])
                                    print(f"the new test unit is : {fields[5]}")
                                    print()
                                    index = i
                                    break

                                elif fieldToUpdate == 3:
                                    print(f"the current test turnaround time is : {fields[6]}")
                                    print()
                                    old_turnaround = fields[6]
                                    fields[6] = valid.TurnAroundCheck()
                                    new_turnaround = fields[6]
                                    self.updateRecordstrunaround(fields[1], new_turnaround)
                                    print()
                                    print(f"the new test turnaround time is : {fields[6]}")
                                    print()
                                    index = i
                                    break

                        file_tests[index] = f"{index + 1}. " + " ".join(fields).strip() + "\n"
                        print()
                        print(f"The updated test is now {file_tests[index]}")
                        print()

                        with open("medicalTest", "w") as output:
                            output.writelines(file_tests)
                        return #Exit after updating

    def updateRecordsNames(self, old_name, new_name):
        print("hi")
        with open("medicalRecord", 'r') as source:
            file_records = source.readlines()

        updated_records = []
        old_name =old_name.split("(")[1].replace(")","").replace(";","")
        new_name=new_name.split("(")[1].replace(")","").replace(";","")



        for record in file_records:
            if old_name in record:
                parts = record.split(":",1)
                ID = parts[0].strip()
                test_details = parts[1].strip().split(",")

                test_name = test_details[0].strip()


                if test_name in old_name:
                    test_details[0] = new_name  # Update the test name

                    if len(test_details) == 6:  #records with turnaround time
                        updated_record = f"{ID}: " + ", ".join(test_details).strip() + "\n"
                    else:  #records without turnaround time
                        updated_record = f"{ID}: " + ", ".join(test_details).strip() + "\n"

                    updated_records.append(updated_record)
                else:
                    updated_records.append(record)
            else:
                updated_records.append(record)

        with open("medicalRecord", 'w') as destination:
            destination.writelines(updated_records)


    def updateRecordstrunaround(self,name,turnaround):
        with open("medicalRecord", 'r') as source:
            file_records = source.readlines()

        updated_records = []
        name =name.split("(")[1].replace(")","").replace(";","")# to extract the abbr





        for record in file_records:
            if name in record and "completed" in record:
                parts = record.split(":",1)
                ID = parts[0].strip()
                test_details = parts[1].strip().split(",")

                combinedStatus = ", ".join(test_details[-2:])
                test_details[4] = combinedStatus

               # turnaround = test_details[5].strip()
                date_time = test_details[1].strip()
                test_details.pop(4)
                test_details[4] = recordname.updateStatus(name,date_time,turnaround,1)  # Update the test turnaround




                for j, part in enumerate(test_details):  # to remove any Unintentional Spaces
                    if ' ' in part:
                        test_details[j] = part.strip()



                updated_record = f"{ID}: " + ", ".join(test_details).strip() + "\n"



                updated_records.append(updated_record)
            else:
                updated_records.append(record)


        with open("medicalRecord", 'w') as destination:
            destination.writelines(updated_records)



    def updateRecordsUnit(self,name,old_unit,new_unit):
        new_unit =new_unit[:-1]
        old_unit=old_unit[:-1]
        with open("medicalRecord", 'r') as source:
            file_records = source.readlines()

        updated_records = []
        name =name.split("(")[1].replace(")","").replace(";","")# to extract the abbr




        for record in file_records:
            if name in record and old_unit in record:
                parts = record.split(":",1)
                ID = parts[0].strip()
                test_details = parts[1].strip().split(",")


               # turnaround = test_details[5].strip()
               # date_time = test_details[1].strip()
                test_details[3] = new_unit  # Update the test unit




                for j, part in enumerate(test_details):  # to remove any Unintentional Spaces
                    if ' ' in part:
                        test_details[j] = part.strip()



                updated_record = f"{ID}: " + ", ".join(test_details).strip() + "\n"


                updated_records.append(updated_record)
            else:
                updated_records.append(record)


        with open("medicalRecord", 'w') as destination:
            destination.writelines(updated_records)







