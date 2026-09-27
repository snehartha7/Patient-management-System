import time

patient = {}


def add_patient(name,blood_group,):
    patient[name] = blood_group
    print(f"Added {name} with blood group {blood_group}.")

def update_student(name,blood_group):    
    if name in patient :
        patient[name] = blood_group
        print(f"Updated {name} to grade {blood_group}")
    else:
        print(f"Student {name} not found.")
        
def get_patient(name):
    if name in patient:
        print(f"{name}: {patient[name]}")
    else:
        print(f"{name} not found.")
        
def delete_patient(name):
    if name in patient:
        del patient[name]
        print(f"deleted {name}")
    else:
        print(f"{name} not found.")
        
def display_all_students():
    if patient:
        for name,blood_group in patient.items():
            print(f"{name} : {blood_group}")
    else:
        print("no patient found")
        
print()
print()



def main():
    while True:
        print("1. Add Patient")
        print("2. Get Patient")
        print("3. Delete patient")
        print("4. Update Patient")
        print("5. Display all patients")
        print("6. Exit")
            
        print()
            
        choice = input("Enter your Choice : ")
        
        if choice == "1":
            name = input("Enter Patient's name = ")
            blood_group = input("Enter Patient's Blood group = ").upper()
            add_patient(name,blood_group,)
                
        elif choice == "2":
            name = input("Enter the Patient's name = ")
            get_patient(name)
            
        elif choice == "3":
            name = input("Enter the name of the patient = ")
            delete_patient(name)
            
        elif choice == "4":
            name = input("Enter the name of the patient = ")
            blood_group = input("Enter the patient's blood group = ")
            
        elif choice == "5":
            display_all_students()
           
        elif choice == "6":
            break
            
        else :
            print("Invalid Choice. Enter a valid choice.")
            continue 
        
        
        
main()
       
    


    