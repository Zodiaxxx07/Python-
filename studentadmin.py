import csv
def csv_write(info):
    with open('student_info.csv','w+',newline='')as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["NAME","D.O.B","CONTACT NO.","E-MAIL ID"])
        writer.writerow(info)
if __name__=='__main__':
    condition=1
    n=1
    while(condition==1):
         student_list=raw_input("Enter Name,D.O.B,Contact Number&E-mail ID(seperated by a comma) of #{} student:".format(n))
         print("The entered information is:" + str(student_list))
         st_info=student_list.split(',')
         print("Entered split-up information is:\n Name:{}\n D.O.B:{}\n Contact Number:{}\n E-Mail ID:{}".format(st_info[0],st_info[1],st_info[2],st_info[3]))
         correct=raw_input("Is the entered information correct(yes/no)?")
         if correct=='yes':
             csv_write(st_info)
             x=raw_input("Do you want to enter more(yes/no)")
             if x=='yes':
                 condition=1
                 n=n+1
             elif x=="no":
                 condition=0
         elif correct=='no':
            print("\n Please re-enter the values!")
