#include <iostream>
#include<string>
#include<cstring>

using namespace std;

int const Size = 5;

class Person
{
    private:
        string Name;
        int Age;
        int Id;
    public:
        Person(string name = " ", int age = 0, int id = 0) : Name(name), Age(age), Id(id) {}

        void Input()
        {
            cout << "Enter Name: ";
            getline(cin, Name);
            cout << "Enter Age: ";
            cin >> Age;
            cout << "Enter Id: ";
            cin >> Id;
            cin.ignore();
        }

        string GetName()
        {
            return Name;
        }

        int GetId()
        {
            return Id;
        }

        void Show()
        {
            cout << "Name of Person is: " << Name << endl;
            cout << "Age of Person is : " << Age << endl;
            cout << "ID of Person is: " << Id << endl;
        }
};

class Doctor : public Person
{
    private:
        string Specialization;
    public:
        Doctor(string special = " ") : Specialization(special) {}

        void Input()
        {
            Person::Input();
            cout << "Enter Specialization of Doctor: ";
            getline(cin, Specialization);
        }

        void Show()
        {
            Person::Show();

            cout << "Specialization of Doctor is: " << Specialization << endl;
        }
};

class Patient : public Person
{
    private:
        string Disease;
        string Temp;
    public:
        Patient(string disease = " ")
        {
            Disease = disease;
        }

        Patient(Doctor& d1)
        {
            Temp = d1.GetName();
        }

        void Input(Doctor d1[] , int Dcount , int Pcount)
        {
            Person::Input();
            cout << "Enter Disease: ";
            getline(cin, Disease);
            
            if(Pcount <= Dcount - 1) 
            {
                Temp = d1[Pcount].GetName();
            }
            else 
            {
                Temp = "No Doc left!";
            }
        }

        void Show()
        {
            Person::Show();

            cout << "Disease: " << Disease << endl;
            cout << "Assigned Doctor is: " << Temp << endl;
        }
};

int main()
{
    Doctor d1[Size];
    Patient p1[Size];

    string DSrchName;
    int DSrchId;
    string PSrchName;
    int PSrchId;
    int Dcount = 0;
    int Pcount = 0;

    while(true)
    {
        cout << "\n";
        cout << "1. Add Doctor\n";
        cout << "2. Add Patient\n";
        cout << "3. Display Doctor Details\n";
        cout << "4. Display Patient Details\n";
        cout << "5. Search Doctor by Name\n";
        cout << "6. Search Doctor by ID\n";
        cout << "7. Search Patient by Name\n";
        cout << "8. Search Patient by ID\n";
        cout << "9. Edit Doctor Details\n";
        cout << "10. Edit Patient Details\n";
        cout << "11. Exit\n";
        
        int Choice;

        cout << "Enter which action you want to Perform: ";
        cin >> Choice;
        cin.ignore();

        cout << "\n";

        switch(Choice)
        {
            case 1:
                if(Dcount < Size)
                {
                    d1[Dcount++].Input();
                }
                else
                {
                    cout << "Array is full you cant add more Doctors!!"<<endl;
                }
                break;
            case 2:
                if(Pcount < Size)
                {
                    p1[Pcount].Input(d1 , Dcount , Pcount);
                    Pcount++;
                }
                else
                {
                    cout << "Array is full you cant add more Patients!!"<<endl;
                }
                break;
            case 3:
                cout << "\nDoctor Details are Following:\n";
                for(int i = 0; i < Dcount; i++)
                {
                    d1[i].Show();
                }
                cout<<endl;
                break;
            case 4:
                cout << "\nPatients Details are Following:\n";
                for(int i = 0; i < Pcount; i++)
                {
                    p1[i].Show();
                    cout<<endl;
                }
                cout<<endl;
                break;
            case 5:
            {
                cin.ignore();
                cout << "Enter the Name of Doctor you want to Search: ";
                getline(cin , DSrchName);

                bool DocFound = false;

                for(int i = 0; i < Dcount; i++)
                {
                    if(DSrchName == d1[i].GetName())
                    {
                        d1[i].Show();
                        DocFound = true;
                        break;
                    }
                }

                if(DocFound == false)
                {
                    cout << "Doctor is not Listed!!\n";
                }
                break;
            }
            case 6:
                {
                    cout << "Enter ID of Doctor you want to Search: ";
                    cin>>DSrchId;

                    bool docFnds = false;

                    for(int i = 0; i < Dcount; i++)
                    {
                        if(DSrchId == d1[i].GetId())
                        {
                            cout << "\n";
                            d1[i].Show();
                            docFnds = true;
                            break;
                        }
                    }

                    if(docFnds == false)
                    {
                        cout << "Doctor is not Listed!!\n";
                    }                
                    break;
            }
            case 7:
            {
                cin.ignore();
                cout << "Enter the Name of Patient you want to Search: ";
                getline(cin , PSrchName);

                bool Pfound = false;

                for(int i = 0; i < Pcount; i++)
                {
                    if(PSrchName == p1[i].GetName())
                    {
                        p1[i].Show();
                        Pfound = true;
                        break;
                    }
                }

                if(Pfound == false)
                {
                    cout << "Patient is not in the Hospital!!\n";
                }  
                break;
            }
            case 8:
            {
                cout << "Enter the ID of Patient you want to Search: ";
                cin >> PSrchId;

                bool Pfnds = false;

                for(int i = 0; i < Pcount; i++)
                {
                    if(PSrchId == p1[i].GetId())
                    {
                        p1[i].Show();
                        Pfnds = true;
                        break;
                    }
                }

                if(Pfnds == false)
                {
                    cout << "Patient is not in the Hospital!!\n";
                }  
                break;
            }
            case 9:
                {
                    if(Dcount > 0)
                    {
                        int rec;
                        cout << "Enter Index of Doctor you want to change(0-4): ";
                        cin >> rec;

                        if (rec >= 0 && rec < Dcount)
                        {
                            cout << "\nIndex " << rec << " currently holds this Doctor Information:\n";
                            d1[rec].Show();

                            cout << "\nEnter the New Information of Doctor: \n";
                            d1[rec].Input();
                            cout << "\nDoctor Information successfully updated!!\n\n";
                        }
                        else
                        {
                            cout << "\nEnter valid Index only then you can update Info!!\n" << endl;
                        }
                    }
                    else
                    {
                        cout << "\nCurrently there are no Doctors in the Hospital!!\n";
                    }
                    break;
                }
            case 10:
            {
                if(Pcount > 0)
                {
                    int rec;
                    cout << "\nEnter Index of Patient you want to chnage(0-4): \n";
                    cin >> rec;
                    if (rec >= 0 && rec < Pcount)
                    {
                        cout << "\nIndex " << rec << " currently holds this Patient Information:\n";
                        p1[rec].Show();

                        cout << "\nEnter the New Information of Patient: \n";
                        p1[rec].Input(d1  , Dcount , rec);
                        cout << "\nPatient Information successfully updated!!\n\n";
                    }
                    else
                    {
                        cout << "\nEnter valid Index only then you can update Info!!\n" << endl;
                    }
                }
                else
                {
                    cout << "\n\nCurrently there are no Patients in the Hospital!!\n";
                }
                break;
            }
            case 11:
                exit(1);
                break;
            default:
                cout<<"Invalid Choice!Choose between 1-11."<<endl;
        }
    }    
    return 0;
}
