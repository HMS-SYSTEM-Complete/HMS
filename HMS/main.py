class Person:
    def __init__(self,name="",age=0,id=0):
        self.__name=name
        self.__age=age
        self.__id=id
    def input(self):
        self.__name=input("Enter name = ")
        self.__age=int(input("Enter age = "))
        self.__id=int(input("Enter ID = "))
    def show(self):
        print(f"Name is = {self.__name}")
        print(f"Age is = {self.__age}")
        print(f"ID is = {self.__id}")

class Doctor(Person):
    def __init__(self, specialization="",name="", age=0, id=0):
        super().__init__(name, age, id)
        self.__specialization=specialization
    def input(self):
        super().input()
        self.__specialization=input("Enter specialization of Doctor = ")
    def show(self):
        super().show()
        print(f"Specialization od Doctor is = {self.__specialization}")
class Patient(Person):
    def __init__(self, pname="", page=0, pid=0,p_disease="",doc_name="",doc_ID=0,
                doc_age=0,doc_sp=""):
        super().__init__(pname, page, pid)
        self.__disease=p_disease
        self.assign_doctor=Doctor(specialization=doc_sp,name=doc_name,age=doc_age,id=doc_ID)
    def input(self):
        print("Enter Patient Details\n")
        super().input()
        self.__disease=input(f"Enter Disease = ")
        print("Enter Doctor Details you are assigning to Patient\n")
        self.assign_doctor.input()
    def show(self):
        print("Patient Details:\n")
        super().show()
        print(f"Disease = {self.__disease}")
        print("Assigned Doctor Details:\n")
        self.assign_doctor.show()
    
    
def main():
    p1=Patient()
    p1.input()
    p1.show()
if __name__=="__main__":
   main()