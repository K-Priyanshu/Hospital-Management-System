import emoji 
# import sqlite3
# from DATABASE import Name, number, Address, E_Mail 
# conn = sqlite3.connect("E:\VS codes\Python\ContactBook.db")
# cur = conn.cursor()

def optional_info():
    global DOB,Designation

    DOB = input("Enter Your Date of Birth: ")
    Designation =input("Your Position: ")
    Print_details()

def Personal_details():
    global Name
    First_Name= input("First Name : ")
    Last_Name=input("Last Name : ")
    Nickname= input("Nickname : ")
    Name=(First_Name, Last_Name)

    contact_details()
    



def contact_details():
    global Number
    Number = input("Contact Number : +91 " )
    if len(Number) != 10:
        print("Invalid input")
        contact_details()
    else:
        Number = int(Number)
        Address_details()
        



def Address_details():
    global Address

    Address_line_1=input("Address Line 1 : ")
    Address_line_2=input("Address Line 2 : ")
    City=input("City : ")
    State=input("State : ")
    Postal_Code=input("Postal Code : ")
    if len(Postal_Code) !=6:
        print("Invalid input")
        Address_details()
    else:
        Postal_Code = int(Postal_Code)
        Address=(Address_line_1, Address_line_2, City, State, Postal_Code)
        E_Mail_details()
        

def E_Mail_details():
    global E_Mail

    E_Mail= input("E-mail: ")
    if  ('@' in E_Mail and '.' in E_Mail and (len(E_Mail)>=6)):
        print(E_Mail)
        #Print_details()
       
    else :
        print("INVALID E-Mail address \nPlease enter your email address again: ")
        E_Mail_details()

    print("Wheater you wnat to enter optional data")
    choice = input("Enter Your Choice: ").title()
    if choice == 'Yes' or choice == '1':
        optional_info()
        Print_details()
    else:
        Print_details()
       

def Print_details():
    try:
        print("Contact Name : ", Name)
        print("Phone Number : ", emoji.emojize(":telephone_receiver: :"), Number)          
        print("Address : ", emoji.emojize(":house_with_garden: :"), Address)
        print("E-mail : ",emoji.emojize(":envelope_with_arrow: :"), E_Mail)
        print("Date of Birth : ", DOB)
        print("Designation : ", Designation)
        print("Contact successfully created!")
    except:
        print("Contact Name : ", Name)
        print("Phone Number : ", Number)          
        print("Address : ", Address)
        print("E-mail : ", E_Mail)
        print("Contact successfully created!")
    

Personal_details()

# sql = "INSERT INTO 'ContactBook' (Name, Phone Number, Address, E-Mail, Date of Birth, Designation) VALUES(?,?,?,?,?,?)"
# cur.execute(sql)
# conn.commit()

# conn.close()



# sql = "INSERT INTO 'ContactBook' (Name, Number, Address, E_Mail) VALUES(?,?,?,?)"
# c.execute(sql,(self.val1, self.val2, self.val3, self.val4))
# conn.commit()
