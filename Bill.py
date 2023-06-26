from MedicineHash import MedicineHash

class Bill:
    def __init__(self, med_table: MedicineHash) -> None:
        self.insert_details(med_table)
    
    def __str__(self) -> str:

        return f'''
Bill ID: {self.__bill_id}
Phone Number: {self.__phone}
Customer: {self.__name}
Meds (Name, Count, Price): {self.__meds_list}
Total Amount: {self.__total_amount}
Payment Mode: {self.__pay_mode}
'''
    
    def get_string(self):
        meds_list = str(self.__meds_list)[1:-1]
        total_str = str(self.__total_amount)
        return '|'.join([self.__bill_id, self.__phone, self.__name, meds_list, total_str, self.__pay_mode])
    
    def insert_details(self, med_table: MedicineHash, update=False):
        if update:
            print(f"Enter modified details for {self.__bill_id}:")
            med_table.add_meds_to_table(self.__meds_list)
        else:
            self.__phone = input("Enter user's phone number: ")
            self.__name = input("Enter user's name: ")
            hex_ph = hex(abs(hash(self.__phone)))
            self.__bill_id = hex_ph[:5] if len(hex_ph) > 5 else hex_ph
            print(f"Generated Bill ID: {self.__bill_id}")
        max_meds_count = len(med_table.get_records())
        # med_data is supposed to be a dictionary which holds name as key and price as the value
        med_data, meds_added = med_table.get_names_rates(), 0
        self.__meds_count = int(input(f"Count of types of medicines (<= {len(med_data)}): "))
        if self.__meds_count > len(med_data):
            print(f"Defaulting to {len(med_data)}, since there are only {len(med_data)} types in the inventory.")
            self.__meds_count = len(med_data)
        self.__meds_list, self.__total_amount = list(), 0
        while meds_added < self.__meds_count:
            med_name = input("Enter a medicine name from the inventory: ")
            while med_name not in med_data:
                print("Try again!")
                med_name = input("Enter a medicine name from the inventory: ")
            med_count = int(input(f"Enter the units of {med_name} to order: "))
            self.__meds_list.append((med_name, med_count, med_data[med_name]))
            self.__total_amount += med_count * med_data[med_name]
            meds_added += 1
        print(f"{self.__meds_count} meds added!")
        med_table.deduct_meds_from_table(self.__meds_list)
        self.__pay_mode = input("Enter the payment method: ")
        if update:
            print(f"Details updated for bill {self.__bill_id}")
    
    def update_details(self, med_table: MedicineHash):
        self.insert_details(med_table, update=True)
    
    def get_bill_id(self):
        return self.__bill_id

    def set_bill_id(self, bill_id):
        self.__bill_id = bill_id

    def get_phone(self):
        return self.__phone

    def set_phone(self, phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_meds_list(self):
        return self.__meds_list

    def set_meds_list(self, meds_list):
        self.__meds_list = meds_list

    def get_pay_mode(self):
        return self.__pay_mode

    def set_pay_mode(self, pay_mode):
        self.__pay_mode = pay_mode






