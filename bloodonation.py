import sys
import csv
reciever=[]
bankdata=[]    
#making sure that we donot need to run the code again and again to do more than one things; im using while true here which is always true.
while True:
    
    
        print('\n1. type info. of blood donor\n2. take info. of blood donor using unique id\n3. type info. of reciever \n4. get data of reciever using unique id.')
        ch = int(input('\ntype the number of your choice. :'))
        if ch==1:
            print('\ntype the following information.:')
            name=input("Donor name:")
            id=input("\nUnique id:")
            phno=input("\nPhone Number:")
            email=input("\nEmail id:")
            add=input("\nAddress:")
            bg=input("\nBloodGroup")
            age=int(input("\nAge:"))
            with open('bankdata.csv','a',newline='') as f:
               
               thewriter=csv.writer(f)
               thewriter.writerow([id,name,phno,email,add,bg,age])
               f.close()
            print("\n\ndone.")
        elif ch==3:
            print("\ntype the following info.:")
            Rid=input('\nReciepent ID:')
            name=input("Reciepent Name:")
            sex=input("Gender:")
            bg=input("BloodGroup:")
            Hname=input("Hospital Name:")
            with open('reciever.csv','a',newline='') as R:
                writ=csv.writer(R)
                writ.writerow([Rid,name,sex,bg,Hname])
                R.close()
            print("\n\ndone")
        elif ch==2:
             with open('bankdata.csv','r') as f:
                 reader=csv.reader(f)
                 for row in reader:
                     bankdata.append(row)
             uid=input('\nunique id:')
             col=[x[0]for x in bankdata]
             if uid in col:
                 for x in range(0,len(bankdata)):
                     if uid==bankdata[x][0]:
                         print(bankdata[x])
            
             else:
                 print("\nInvalid Donor ID!!")
             f.close()
            
        elif ch==4:
            with open('reciever.csv','r') as R:
                reader=csv.reader(R)
                for row in reader:
                    reciever.append(row)
            Rid=input('\nReciever ID:')
            col=[x[0]for x in reciever]
            if Rid in col:
                for x in range(0,len(reciever)):
                    if Rid==reciever[x][0]:
                        print(reciever[x])
            else:
                print('\nInvalid ID')
            R.close()
       
            
        else:
            print("\n\ntype numbers between 1 to 4")
sys.exit(1)    