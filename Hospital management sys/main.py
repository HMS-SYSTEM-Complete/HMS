import json
global patien_record
global doctor_record
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
        #IF initilize through constructor
    def input(self):
        super().input()
        self.__specialization=input("Enter specialization of Doctor = ")
        try:
            with open(r"Hospital management sys\doctor_records.json","r") as file:
                data=json.load(file)
        except FileNotFoundError:
            with open(r"Hospital management sys\doctor_records.json","w") as file:
                json.dump([self.to_dict()],file,indent=4)
        else:
            data.append(self.to_dict())
            with open(r"Hospital management sys\doctor_records.json","w") as file:
                json.dump(data,file,indent=4)
    @staticmethod
    def show():
        doc_id=int(input("Enter doctor ID you want to show data = "))
        with open(r"Hospital management sys\doctor_records.json","r") as file:
            doctors=json.load(file)
            find=False
            for doctor in doctors:
                if doctor["ID"]==doc_id:
                    print(doctor)
                    find=True
                    break
            if find==False:
                print("Doctor with this ID Does not exist!")
                    

        # super().show()
        # print(f"Specialization od Doctor is = {self.__specialization}")
    def to_dict(self):
        return {
            "Name": self._Person__name,      # Access private attributes of Person
            "Age": self._Person__age,
            "ID": self._Person__id,
            "Specialization": self.__specialization    
        }
class Patient(Person):
    def __init__(self, pname="", page=0, pid=0,p_disease="",doc_name="",doc_ID=0,
                doc_age=0,doc_sp=""):
        super().__init__(pname, page, pid)
        self.__disease=p_disease
        self.assign_doctor=Doctor(specialization=doc_sp,name=doc_name,age=doc_age,id=doc_ID)
    def input(self):
        print("Enter Patient Details\n")
        super().input()
        self.__disease=input("Enter Disease = ")
        print("Enter Doctor Details you are assigning to Patient\n")
        self.assign_doctor.input()
    def show(self):
        print("Patient Details:\n")
        super().show()
        print(f"Disease = {self.__disease}")
        print("Assigned Doctor Details:\n")
        self.assign_doctor.show()

    
def main():
    while(True):
        choice=int(input("Which option you want to perform\n"
        "1.Add Doctor\n2.Add Patient\n3.Display Doctor Details"
        "\n4.Display Patient Details\n"))
        match choice:
            case 1:
                new_doctor=Doctor()
                new_doctor.input()
            case 2:
                new_patient=Patient()
                new_patient.input()
            case 3:
                new_doctor=Doctor()
                new_doctor.show()
            case 4:
                pass
        print("\n")


if __name__=="__main__":
   main()