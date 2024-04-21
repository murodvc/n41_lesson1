import json


class Contact:
    def __get_contact(self):
        try:
            with open(self.__file, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open(self.__file, "w") as f:
                json.dump([], f)
                data = []
        self.__contacts = data

    def __read_password(self):
        with open("password.txt") as f:
            self.__password = f.readline()

    def __init__(self, password):
        self.__file = "contact.json"
        self.__read_password()
        if self.__password != password:
            print(" Parol Xato  :(  ")
            return
        else:
            self.__get_contact()
            print("Xush kelibsiz!  :) ")

    def check_contact_exist(self, username):
        for user in self.__contacts:
            if user["username"] == username:
                return user
        else:
            return False

    def validate_number(self, number):
        if len(number) == 13 and number[0] == "+" and number[1:].isdigit():
            return True
        else:
            return print("nomerni to'g'ri kiriting!")

    def update_contact(self, username, number):
        for user in self.__contacts:
            if user["username"] == username:
                user["phone"] = number
        self.__commit()
        print("Contact muvafaqiyatli yangilandi")

    def get_all_contacts(self):
        if self.__contacts:
            print("All contacts:")
            for contact in self.__contacts:
                print(f"Username: {contact['username']}, Phone: {contact['phone']}")

    def __commit(self):
        with open(self.__file, "w") as f:
            json.dump(self.__contacts, f, indent=3)

    def add_contact(self, username, number):
        user = {
            "username":username,
            "phone":number
        }

        for contact in self.__contacts:
            if contact["username"]!=username:
                self.__contacts.append(user)
                self.__commit()
                print("contact saxranit qilindi")
                break
        else:
            print("bunday ismli contact bor! ")

    def delete_contact(self, d:str):

        for contact in self.__contacts:
            if d == contact["username"]:
                    self.__contacts.remove(contact)
                    print("kontakt ochirildi")
                    break

        else:
            print(" bunday ismli kontakt topilmadi ")

        with open("contact.json", "w") as f:
            json.dump(self.__contacts , f, indent=3)

def menu():
    # password = input("Parol kiriting: ")
    c = Contact(password)

    with open("password.txt") as f:
        data = f.readline()
    if password==data:
        print("1.all_contacts")
        print("2.add_contacts")
        print("3.update_contact")
        print("4.delete_contact")
        ch = input("menu tanlang:")

        if ch=="1":
            c.get_all_contacts()
        if ch=="2":
            username = input("username: ")
            # phone=input("phone: ")
            con = c.check_contact_exist(username)
            if con == False:
                number = input(" raqamni kiriting: ")
                if c.validate_number(number):
                    c.update_contact(username, number)
                else:
                    print("No to'g'ri raqam kiritdingiz :(")
            else:
                print("bunday ismli kontakt bor ismni o'zgartirin ")
            c.add_contact(username=username, number=number)

        if ch == "3":
            username = input("contact username ni kiriting: ")
            contact = c.check_contact_exist(username)
            if contact:
                print("Hozirgi raqam : ", contact["phone"])
                number = input("Yangi raqamni kiriting: ")
                if c.validate_number(number):
                    c.update_contact(username, number)
                else:
                    print("No to'g'ri raqam kiritdingiz :(")
        if ch == "4":
            f = input("ochirmoqchi bo'lgan kontakt ismini kiriting: ")
            c.delete_contact(d=f)
        menu()



if __name__ == '__main__':
    # menu()
    password = input("Parol kiriting: ")
    # c = Contact(password)
    menu()
