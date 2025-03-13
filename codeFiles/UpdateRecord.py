from Validations import Valid
import re
from RecordInsertion import RecordInsertion
valid = Valid()
update= RecordInsertion()

class UpdateRecord:

    def updateRecord(self):



        ID = valid.IDCheck()

        while True:

            with open("medicalRecord", 'r') as source:
                with open("Filtered", 'w') as destination:
                    content = source.read()
                    destination.write(content)

            matchedRecords = []
            line = ""



            with open("Filtered", 'r') as data:
                for record in data:
                    if ID in record:
                        matchedRecords.append(record.strip())


            with open("Filtered", 'r') as data:
                file_records =data.readlines()



            if int(len(matchedRecords)) == 1:

                line = matchedRecords[0]

            elif int(len(matchedRecords)) > 1:

                for i, record in enumerate(matchedRecords):
                    print(f"{i+1}- {record}")

                row = input("Choose the record that you want to edit: ")
                if row.isdigit():
                    index = int(row) - 1
                    if index < len(matchedRecords) and index > 0:
                        line = matchedRecords[index]
                    else:
                        print
                        print(f"choose a number from 1 to {len(matchedRecords)} ")
                        print()
                        continue
                else:
                    print()
                    print("make sure that you are choosing a valid numeric option ")
                    print()
                    continue

            else:
                print()
                print("There are no records in our system")
                print()
                continue






            ToUpdate =["Test Name","Test Date and time","Test Value","Test status"]


            while True:

                id, rest_of_line = line.split(':', 1)

                parts = rest_of_line.strip().split(',')
                parts = [part.strip() for part in parts]


                name = parts[0]
                date_time = parts[1]
                value = parts[2]
                unit = parts[3]
                status = parts[4]

                #print(name)
                #print(date_time)
                #print(value)
                #print(unit)
                #print(status)

                newRecord = id + ": " + name + ", " + date_time + ", " + str(value) + ", " + unit + ", " + status

                print()



                print(f"The record: {newRecord} ")

                parts.pop(3)# to remove the unit


                for i, field in enumerate(ToUpdate):
                    print(f"{i + 1}- {field}")

                fieldToUpdate = int(input("Choose the field that you want to update or 0 to quit: "))
                if fieldToUpdate == 0:
                    break
                fieldToUpdate = fieldToUpdate-1



                for i, record in enumerate(file_records):


                    IDPart, RData = record.split(":", 1)

                    if int(len(RData.split(","))) == 5:  # if the status is pending or reviewed (no turn around time)

                        if IDPart.strip() == id and name in RData and date_time in RData and value in RData and unit in RData and status in RData:

                            fields=RData.strip().split(",")

                            for j, part in enumerate(fields): # to remove any Unintentional Spaces
                                if ' ' in part:
                                    fields[j] = part.strip()

                            if fieldToUpdate < len(fields):

                                if fieldToUpdate == 0:

                                    fields[fieldToUpdate] = update.validName()
                                    with open("medicalTest", 'r') as data:
                                        for record in data:
                                            if fields[fieldToUpdate] in record:
                                                fields[3] = record.split(";")[2].split(":")[1].split(",")[0]# to add the unit
                                if fieldToUpdate == 1:
                                    fields[fieldToUpdate] = update.validDateTime()


                                if fieldToUpdate == 2:
                                    fields[fieldToUpdate] = str(update.validValue())
                                if fieldToUpdate == 3:
                                    fields[4] = update.validStatus(fields[0],fields[1])


                            file_records[i] =f"{IDPart.strip()}: " + ", ".join(fields).strip() + "\n"
                            line = f"{IDPart.strip()}: " + ",".join(fields).strip() + "\n"
                            with open("medicalRecord", "w") as output:
                                output.writelines(file_records)
                            break

                    elif int(len(RData.split(","))) == 6:  # if the status is completed (with turn around time)

                        if IDPart.strip() == id and name in RData and date_time in RData and value in RData and unit in RData and status in RData:

                            fields=RData.strip().split(",")

                            combinedStatus=", ".join(fields[-2:])

                            fields = fields[:-2] + [combinedStatus]

                            for j, part in enumerate(fields): # to remove any Unintentional Spaces
                                if ' ' in part:
                                    fields[j] = part.strip()

                            if fieldToUpdate == 0:

                                fields[fieldToUpdate] = update.validName()
                                with open("medicalTest", 'r') as data:
                                    for record in data:
                                        if fields[fieldToUpdate] in record:
                                            fields[3] = record.split(";")[2].split(":")[1].split(",")[0]  # to add the unit
                            if fieldToUpdate == 1:
                                fields[fieldToUpdate] = update.validDateTime()
                                fields[4] = update.updateStatus(fields[0], fields[1]," ",0)# to update the turn around time, since the test date has changed

                            if fieldToUpdate == 2:
                                fields[fieldToUpdate] = str(update.validValue())
                            if fieldToUpdate == 3:
                                fields[4] = update.validStatus(fields[0],fields[1])


                            file_records[i] =f"{IDPart.strip()}: " + ", ".join(fields).strip() + "\n"
                            line = f"{IDPart.strip()}: " + ",".join(fields).strip() + "\n"

                            with open("medicalRecord", "w") as output:
                                output.writelines(file_records)
                            break

            print(f"The record: {newRecord} ")

            choice = input(f"do you want to edit any other record for the patient with ID = {ID}, yes or no: ")
            choice = choice.lower()
            if choice == "yes":
                continue
            else:
                break












