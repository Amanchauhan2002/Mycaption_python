import csv


def write_into_csv(info):
    with open('student_gamma.csv', 'a',newline='')as xyz_file:
        writer = csv.writer(xyz_file)

        if xyz_file.tell() == 0:
            writer.writerow(["Name", "Age","Roll no","Contact_no","Email id"])

        writer.writerow(info)

if __name__ == '__main__':
    condition = True
    student_no = 1
    while condition:
        student_info = input("\nEnter the information of student #{} in the format"
                         "(name,age,roll no,contact_number,email id)".format(student_no))

        student_info_list = student_info.split(",")

        print("Entered information:\nName : {}\nAge : {}\nRoll no. : {}\nContact_number : {}\nEmail id : {}"
          .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))
        student_no += 1
        choice = input("Is the information entered correct(yes/no)")
        if choice == 'yes':
            write_into_csv(student_info_list)
            count = input("Do you want to enter information of another student (yes/no)")
            if count == "no":
                condition =False
        elif choice == 'no':
            print("\nPlease re-enter the information")
            student_no -=1



