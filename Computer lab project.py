#19-41720-3
#A computer lab management system
import os


class PC:
    def __init__(self, number, os, status):
        self.number = number
        self.os = os
        self.status = status
    def display_info(self):
        print("PC Number:", self.number)
        print("Operating System:", self.os)
        print("Status:", self.status)
def add_pc(lab):
    number = input("Enter PC number: ")
    os = input("Enter operating system: ")
    status = input("Enter status: ")
    pc = PC(number, os, status)
    for existing_pc in lab:
        if existing_pc.number == number:
           response = input("This PC number already exists. Do you want to update it (U),remove it (R), or take no action (N)? ")
        if response.lower() == 'u':
           existing_pc.os = os
           existing_pc.status = status
           print("PC updated successfully!")
        elif response.lower() == 'r':
           lab.remove(existing_pc)
           print("PC removed successfully!")
        else:
           print("No action taken.")
        return
    lab.append(pc)
print("PC added successfully!")

def update_pc(lab):
    number = input("Enter PC number: ")
    for pc in lab:
        if pc.number == number:
           os = input("Enter new operating system: ")
           status = input("Enter new status: ")
           pc.os = os
           pc.status = status
           print("PC updated successfully!")
           return
print("PC not found.")

def remove_pc(lab):
     number = input("Enter PC number: ")
     for pc in lab:
      if pc.number == number:
          lab.remove(pc)
     print("PC removed successfully!")
     return
print("PC not found.")

def display_all_pcs(lab):
    if len(lab) == 0:
       print("No PCs in the lab.")
    else:
        for pc in lab:
            pc.display_info()
            print()

def display_pc(lab):
    number = input("Enter PC number: ")
    for pc in lab:
        if pc.number == number:
           pc.display_info()
           return
print("PC not found.")

def search_pc(lab):
    number = input("Enter PC number: ")
    for pc in lab:
        if pc.number == number:
           pc.display_info()
           return
    response = input("PC not found. Do you want to add it (A) or take no action (N)? ")
    if response.lower() == 'a':
           add_pc(lab)

def store_pcs(lab):
    filename = input("Enter filename to store PCs: ")
    with open(filename, 'w') as f:
        for pc in lab:
            f.write(f"PC Number: {pc.number}\n")
            f.write(f"Operating System: {pc.os}\n")
            f.write(f"Status: {pc.status}\n")
            f.write('\n')
    print("PCs stored successfully!")

def main():
    lab = []
    while True:
       print("1. Add a new PC")
       print("2. Update PC information")
       print("3. Remove a PC")
       print("4. Display all PCs")
       print("5. Display individual PC")
       print("6. Search for a PC")
       print("7. Store PCs to file")
       print("8. Quit")
       choice = input("Enter choice: ")
       if choice == '1':
        add_pc(lab)
       elif choice == '2':
        update_pc(lab)
       elif choice == '3':
        remove_pc(lab)
       elif choice == '4':
        display_all_pcs(lab)
       elif choice == '5':
        display_pc(lab)
       elif choice == '6':
        search_pc(lab)
       elif choice == '7':
        store_pcs(lab)
       elif choice == '8':
        print("Turning OFF.")
        break
       else:
            print("Invalid choice. Please try again.")
if __name__ == '__main__':
 main()

