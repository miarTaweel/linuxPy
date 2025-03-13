import os

from Validations import Valid
valid=Valid()

class summary:

    def summarise(self):

        with open("Filtered", "r") as file:
            lines = file.readlines()
        if os.path.getsize("Filtered") == 0:
            print("No filtered Records exist")
            return 0

        with open("medicalTest", "r") as file:
            tests = file.readlines()
        values=[]
        min_record=""
        max_record = ""
        for i in lines:
            values.append(float(i.split(',')[2].split(',')[0]))

        min_value = min(values)
        max_value = max(values)
        average = sum(values) / len(values)

        #Retrieving the records of the min and max
        for i in lines:
            if (float(i.split(',')[2].split(',')[0])==min_value):
                min_record = i
        for i in lines:
            if (float(i.split(',')[2].split(',')[0])==max_value):
                max_record = i


        types=[]
        for i in lines:
            types.append(i.split(',')[0].split(':')[1].strip())
        typeset=set(types)

        alltypes = []
        names=[]
        for i in tests:
            alltypes.append(i.split(',')[0].split(':')[1].split(')')[0].split('(')[1].strip())
            names.append(i.split(',')[0].split(':')[1].split(';')[0].strip())

        # finding the min ,max ,sum ,count of each test
        dict={}
        for i in alltypes:
            count=0
            summ=0
            minn = float('inf')
            maxx = float('-inf')
            min_r=""
            max_r=""

            for k in lines:
                if (i==k.split(',')[0].split(':')[1].strip()):
                    if float(k.split(',')[2].split(',')[0]) < minn :
                        minn = float(k.split(',')[2].split(',')[0])
                        min_r=k
                    if float(k.split(',')[2].split(',')[0]) > maxx :
                        maxx = float(k.split(',')[2].split(',')[0])
                        max_r = k
                    summ+=float(k.split(',')[2].split(',')[0])
                    count+=1
            dict[i]=(summ,count,minn,min_r.strip(),maxx,max_r.strip())


        #Retriveing the turnaround of each test from the medical test file
        turnaround=[]
        for k in typeset:
            for i in tests:
                if(i.split(',')[0].split(':')[1].split(')')[0].split('(')[1].strip()==k):
                    turnaround.append(i.split(';')[2].split(',')[1].strip())

        days=[]
        hours=[]
        minutes=[]
        for i in turnaround:
            days.append(int(i.split('-')[0]))
            hours.append(int(i.split('-')[1]))
            minutes.append(int(i.split('-')[2]))



        minutes_list = [convert_to_minutes(x) for x in turnaround]
        max_minutes = max(minutes_list)
        max_time_index = minutes_list.index(max_minutes)
        max_time = turnaround[max_time_index]


        minutes_list = [convert_to_minutes(time) for time in turnaround]

        # Find the minimum value and its corresponding time
        min_minutes = min(minutes_list)
        min_time_index = minutes_list.index(min_minutes)
        min_time = turnaround[min_time_index]



        print("")
        print("********************************** The Value Report **************************************")
        print("")
        print("For all filtered records:")
        print(f"  The Minimum value ={min_value}")
        print(f"  The Record  : {min_record.strip()}")
        print(f"  The Average value ={average:.3f}")
        print(f"  The Maxmum value ={max_value}")
        print(f"  The Record  : {max_record}")
        print("       -------------------------------------------------")
        print("For each filtered Test type:")
        print("")
        x=0
        for key,v in dict.items():

            print(f"-{names[x]}:")
            x+=1
            if not v[3]:
                print(f"  Records of this type dont exit")
                print()
            elif v[2]==v[4]:
                print(f"  Only one Record of this type exists:")
                print(f"  The Record ={v[5]}")
                print(f"  The Minimum value = The Maximum value= The average= {v[2]}")
                print()
            else:
                print(f"  The Minimum value ={v[2]}")
                print(f"  The Minimum Record  = {v[3]}")
                print(f"  The Maximum value ={v[4]}")
                print(f"  The Maximum Record = {v[5]}")
                avg=float(v[0])/float(v[1])
                print(f"  The average  ={avg:.3f}")
                print()




        print("********************************** The Turnaround Time Report **************************************")
        #find the avg of each days , hours , minutes
        avgd = sum(days) / len(days)
        avgh = sum(hours) / len(hours)
        avgm=  sum(minutes) / len(minutes)

        # Turning the decimal point into hours or minutes
        decimal_part = avgh - int(avgh)
        decimal_part1 = avgd - int(avgd)
        avgm += decimal_part * 60
        avgh+= decimal_part1 *24

        if (avgm>59):
            avgm = avgm-60
            avgh+=1
        if (avgh>23):
            avgh = avgh-24
            avgd+=1
        print("")
        print(f"  The Minimum turnaround time = {int(min_time.split('-')[0])} days {int(min_time.split('-')[1])} hours {int(min_time.split('-')[2])} minutes")
        print("")
        print(f"  The Average turnaround time = {int(avgd)} days {int(avgh)} hours {int(avgm)} minutes")
        print("")
        print(f"  The Maximum turnaround time = {int(max_time.split('-')[0])} days {int(max_time.split('-')[1])} hours {int(max_time.split('-')[2])} minutes")
        print("")
        print("************************************************************************************************")


def convert_to_minutes(time_str):
    day, hours, minutes = map(int, time_str.split('-'))
    return day * 24 * 60 + hours * 60 + minutes




