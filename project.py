import csv
def write_into_csv(info_list):
    with open('task.csv','a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(['Name', 'Age', 'Contact Number', 'E-mail ID'])
        writer.writerow(info_list)
if __name__=='__main__':
    condition= True
    student_num=1
    while(condition): 
        task=input("Enter some student information for student #{}(Name Age Contact_number E-mail_ID): ".format(student_num))
        print("Entered information: "+task)
        student_info_list=task.split(' ')
        print('Entered split information is: '+str(student_info_list))
        print('\nThe entered information is-\nName: {}\nAge {}\nContact_number: {} \nE-mail_ID: {}'.format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        choice_check=input('Is the entered info correct? (yes/no): ')
        if choice_check=='yes':
            write_into_csv(student_info_list)
            condition_check=input("Enter (yes/no) if you want to enter information for another student: ")
            if condition_check== "yes":
                condtion = True
                student_num=student_num+1
            elif condition_check=="no":
                condition = False
        elif choice_check=='no':
            print('\nPlease re-enter the values!')