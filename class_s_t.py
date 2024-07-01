
class student:
    status="Student"
    Name=""
    email=""
    phone=0
    address=""
    Rollno=None
    subjectmarks=[]

    def __init__(self,status,Name,email,phone,address,Rollno):
        self.status=status
        self.Name=Name
        self.email=email
        self.phone=phone
        self.address=address
        self.Rollno=Rollno

    def edit(self):
        self.status=input("enter status: ")
        self.Name=input("enter the name: ")
        self.email=input("email: ")
        self.phone=int(input("phone: "))
        self.address=input("enter the address: ")
        self.Rollno=input("rollno: ")
    
    def list_return(self):
        list=[self.status,self.Name,self.email,self.phone,self.address,self.Rollno]
        return list

class teacher(student):
    id=int
    subjectstatus=""

    def __init__(self, status, Name, email, phone, address, id, subjectstatus):
        self.subjectstatus=subjectstatus
        self.id=id
        student.status=status
        student.Name=Name
        student.email=email
        student.phone=phone
        student.address=address

    def edit(self):
        self.status=input("enter status: ")
        self.Name=input("enter the name: ")
        self.email=input("email: ")
        self.phone=int(input("phone: "))
        self.address=input("enter the address: ")
        self.id=input("idno: ")
        self.subjectstatus=input("subject: ")

    def list_return(self):
        list=[self.status,self.Name,self.email,self.phone,self.address,self.id,self.subjectstatus]
        return list
    


# master_key=teacher("Teacher",Name="Aashish",email="aashis5657@gmail.com",phone=9841907142,address="Dolpa",id=10,subjectstatus="All")
# list1=master_key.list_return()
# print(list1)
# print(master_key.Name)
# print(master_key.email)
selection_login=input("Enter the login selection 'Teacher' for Teacher or 'Student' for student: ")

if selection_login=="Teacher":
    Name=input("Enter the name of Teacher: ")
    id=int(input("Enter the id No. of Teacher: "))
    email=input("Enter the email: ")
    phone=int(input("Enter the phone No.: "))
    address=input("Enter the address: ")
    subjectstatus=input("Enter the subject:")
    T1=teacher("Teacher",Name,email,phone,address,id,subjectstatus)
    


# count=1

# while count==1:
#     count=int(input("Enter 1 for re"))







