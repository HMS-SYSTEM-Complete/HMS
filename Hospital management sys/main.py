import json
import pandas
class Person:
    def __init__(self,name="",age=0,id=""):
        self.__name=name
        self.__age=age
        self.__id=id
    def input(self):
        self.__name=input("Enter name = ")
        self.__age=int(input("Enter age = "))
        self.__id=input("Enter ID = ")
    def show(self):
        print(f"Name is = {self.__name}")
        print(f"Age is = {self.__age}")
        print(f"ID is = {self.__id}")

class Doctor(Person):
    def __init__(self, specialization="",name="", age=0, id=""):
        super().__init__(name, age, id)
        self.__specialization=specialization
    def input(self):
        super().input()
        self.__specialization=input("Enter specialization of Doctor = ")
        try:
            with open(r"HMS\doctor_records.json","r") as file:
                data=json.load(file)
        except FileNotFoundError:
            with open(r"HMS\doctor_records.json","w") as file:
                json.dump([self.to_dict()],file,indent=4)
                print("\n")
                print("Doctor Record added successfully!")
        except json.JSONDecodeError:
                with open(r"HMS\doctor_records.json","w") as file:
                    json.dump([self.to_dict()],file,indent=4)
                    print("\n")
                    print("Doctor Record added successfully!")
        else:
            data.append(self.to_dict())
            with open(r"HMS\doctor_records.json","w") as file:
                json.dump(data,file,indent=4)
                print("\n")
                print("Doctor Record added successfully!")
    @staticmethod
    def show():
        doc_id=input("Enter doctor ID you want to show data = ")
        try:
            with open(r"HMS\doctor_records.json","r") as file:
                doctors=json.load(file)
        except FileNotFoundError:
            print("Record not found!")
            return
        except json.JSONDecodeError:
            print("Record not found!")
            return
        else:
            find=False
            for doctor in doctors:
                if doctor["ID"]==doc_id:
                    data=pandas.DataFrame([doctor])
                    print("\n")
                    print("Doctor Record Found:\n")
                    print(data.to_string(index=False))
                    find=True
                    break
            if find==False:
                print("\nDoctor with this ID Does not exist!")
    def to_dict(self):
        return {
            "Name": self._Person__name,      # Access private attributes of Person
            "Age": self._Person__age,
            "ID": self._Person__id,
            "Specialization": self.__specialization    
        }
class Patient(Person):
    def __init__(self, pname="", page=0, pid="",p_disease="",doc_name="",doc_ID="",
                doc_age=0,doc_sp=""):
        super().__init__(pname, page, pid)
        self.__disease=p_disease
        self.assign_doctor_to_patient=Doctor(specialization=doc_sp,name=doc_name,age=doc_age,id=doc_ID)
    def input(self):
        print("Enter Patient Details\n")
        super().input()
        self.__disease=input("Enter Disease = ")
        print("\n") 
        check=self.assign_doctor()
        # print()
        # print("Enter Doctor Details you are assigning to Patient\n")
        # self.assign_doctor.input() 
        if check:
            try:
                with open(r"HMS\patient_records.json","r") as file:
                    data=json.load(file)
            except FileNotFoundError:
                with open(r"HMS\patient_records.json","w") as file:
                    json.dump([self.to_dict()],file,indent=4)
                    print("\n")
                    print("Patient Record added successfully!")
            else:   
                data.append(self.to_dict())
                with open(r"HMS\patient_records.json","w") as file:
                    json.dump(data,file,indent=4)
                    print("\n")
                    print("Patient Record added successfully!")
    @staticmethod
    def show():
        patient_id=input("Enter Patient ID you want to show data = ")
        try:
            with open(r"HMS\patient_records.json","r") as file:
                patients=json.load(file)
        except FileNotFoundError:
            print("Record not found!")
            return
        except json.JSONDecodeError:
            print("Record not found!")
            return
        else:
            find=False
            for patient in patients:
                if patient["ID"]==patient_id:
                    patient_data=pandas.DataFrame([patient])
                    print("\n")
                    print("Patient Record Found:\n")
                    print(patient_data.to_string(index=False))
                    find=True
                    break
            if not find:
                print("\nPatient with this ID Does not exist!")
    def to_dict(self):
        return {
            "Name": self._Person__name,      # Access private attributes of Person
            "Age": self._Person__age,
            "ID": self._Person__id,
            "Disease": self.__disease,
            "Doctor": self.assigned_doc,
            "Doctor ID":self.assign_doctor_id
        }
    def assign_doctor(self):
        try:
            with open(r"HMS\doctor_records.json","r") as file:
                doctors=json.load(file)
        except FileNotFoundError:
            print("No Doctors record in system!")
            return False
        except json.JSONDecodeError:
            print("Doctors are not available sorry!")
            return False
        else:
            print("\n")
            print("Here is the list of doctors which doctor you want to assign to patient:")
            data=pandas.DataFrame(doctors)
            print("\n")
            print(data.to_string(index=False))
            print("\n")
            doc_id=input("Enter doctor ID you want to assign to patient = ")
            find=False
            for (index,row) in data.iterrows():
                if row.ID==doc_id:
                    self.assigned_doc=row["Name"]
                    self.assign_doctor_id=row["ID"]
                    print("\n")
                    print("Doctor Assigned successfully!")
                    find=True
                    break
            if  not find:
                print("\nDoctor with this ID Does not exist!")
                return False
            else:
                return True    
def main():
    exit=False
    while(exit==False):
        choice=int(input("Which option you want to perform\n"
        "1.Add Doctor\n2.Add Patient\n3.Display Doctor Details"
        "\n4.Display Patient Details\n5.Exit\n"))
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
                new_patient=Patient()
                new_patient.show()
            case 5:
                exit=True
        print("\n")
if __name__=="__main__":
   main()