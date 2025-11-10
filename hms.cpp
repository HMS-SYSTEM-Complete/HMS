#include <iostream>
#include<string>

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
        }

        string GetName()
        {
            return Name;
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

            cin.ignore();
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

        void Input()
        {
            Person::Input();
            cin.ignore();
            cout << "Enter Disease: ";
            getline(cin, Disease);
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

    int Dcount = 0;
    int Pcount = 0;

    while(true)
    {
        cout << "1. Add Doctor\n";
        cout << "2. Add Patient\n";
        cout << "3. Display Doctor Details\n";
        cout << "4. Display Patient Details\n";
        cout << "5. Exit\n";
        
        int Choice;

        cout<<"Enter which action you want to Perform: ";
        cin>>Choice;

        switch(Choice)
        {
            case 1:
                if(Dcount < Size)
                {
                    d1[Dcount++].Input();
                }
                else
                {
                    cout<<"Array is full you cant add more Doctors!!"<<endl;
                }
                break;
            case 2:
                if(Pcount < Size)
                {
                    p1[Pcount++].Input();
                }
                else
                {
                    cout<<"Array is full you cant add more Patients!!"<<endl;
                }
                break;
            case 3:
                cout<<"\nDoctor Details are Following:\n";
                for(int i = 0; i < Dcount; i++)
                {
                    d1[i].Show();
                }
                cout<<endl;
                break;
            case 4:
                cout<<"\nPatients Details are Following:\n";
                for(int i = 0; i < Pcount; i++)
                {
                    p1[i].Show();
                }
                cout<<endl;
                break;
            case 5:
                exit(1);
                break;
            default:
                cout<<"Invalid Choice!Choose between 1-5."<<endl;
        }
    }    
    return 0;
}
