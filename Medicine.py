class Medicine:
    def __init__(self) -> None:
        self.insert_details()
    
    def __str__(self) -> str:
        return f'''
Name: {self.__name}
Remedy for: {self.__purpose}
Brand: {self.__brand}
Price: {self.__price}
Count: {self.__count}
Needs Prescription: {'Yes' if self.__needs_prescription else 'No'}
'''
    
    def get_string(self):
        price_str = str(self.__price)
        count_str = str(self.__count)
        needs_pres_str = str(self.__needs_prescription)
        return '|'.join([self.__name, self.__purpose, self.__brand, price_str, count_str, needs_pres_str])
    
    def insert_details(self, update=False):
        if update:
            print(f'Enter the new details for {self.__name}:\n')
        else:
            self.__name = input("Enter the medicine name: ")
            self.__purpose = input("Remedy for (Illness/Symptom/Injury): ")
            self.__brand = input("Enter the medicine brand: ")
        self.__price = float(input("Enter the unit price (in ₹): "))
        self.__count = int(input("Enter the medicine count: "))
        if not update:
            self.__needs_prescription = True if input("Does this medicine need a prescription? (Yes/No): ").lower()[0] == 'y' else False
    
    def update_details(self):
        self.insert_details(update=True)
    
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
    
    def get_purpose(self):
        return self.__purpose
    
    def set_purpose(self, purpose):
        self.__purpose = purpose
    
    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_count(self):
        return self.__count

    def set_count(self, count):
        self.__count = count

    def get_needs_prescription(self):
        return self.__needs_prescription

    def set_needs_prescription(self, needs_prescription):
        self.__needs_prescription = needs_prescription
