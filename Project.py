from MedicineHash import MedicineHash, FILENAME as MED_FILENAME
from Medicine import Medicine
from BillHash import BillHash, FILENAME as BILL_FILENAME
from Bill import Bill
from time import sleep
from os import system as prompt
from tabulate import tabulate
import pickle

def clearscreen():
	prompt('cls||clear')

def delay(times, sleeptime = 0.4, char = '.'):
	for i in range(times):
		sleep(sleeptime)
		print(char, end='', flush=True)

def execute_function_idx(functions: list, idx: int):
	clearscreen()
	functions[idx]()

def insert_med():
	new_med = Medicine()
	med_table.insert(new_med)
	wait_input = input('Press enter to continue...↩')

def display_meds():
	print(tabulate(med_table.get_records(), headers=['Medicine Name', 'Medicine Data'], tablefmt='rounded_grid'))
	wait_input = input('Press enter to continue...↩')

def display_bills():
	print(tabulate(bill_table.return_records(), headers=['Bill ID', 'Order Data'], tablefmt='rounded_grid'))
	wait_input = input('Press enter to continue...↩')

def search_med():
	med_name_to_search = input('Enter medicine name to search: ')
	did_find_train = med_table.retrieve(med_name_to_search)
	print('Searching for medicine', end='')
	delay(5, sleeptime=0.25)
	print('Search complete!\n')
	if did_find_train:
		print('✅ Entry found.')
		print(did_find_train)
	else:
		print('❌ Entry not found!')
	wait_input = input('Press enter to continue...↩')

def update_med():
	med_name_to_search = input('Enter medicine name to modify: ')
	did_find_med = med_table.update(med_name_to_search)
	print('Searching for entry', end='')
	delay(3, sleeptime=0.25)
	print('Search complete!\n')
	if did_find_med:
		print('Updating the database', end='')
		delay(4, sleeptime=0.25)
		print('✅ Details updated.')
	else:
		print('❌ Entry not found!')
	wait_input = input('Press enter to continue...↩')

def delete_med():
	med_name_to_search = input('Enter medicine name to delete: ')
	print('Searching for entry', end='')
	delay(3, sleeptime=0.25)
	print('Search complete!\n')
	did_find_med = med_table.delete(med_name_to_search)
	if did_find_med:
		print('Deleting the entry', end='')
		delay(4, sleeptime=0.25)
		print('✅ Details deleted!')
	else:
		print('❌ Entry not found!')
	wait_input = input('Press enter to continue...↩')

def admin_workflow():
	admin_functions = [insert_med, display_bills, display_meds, search_med, update_med, delete_med]
	while True:
		clearscreen()
		print('1. Add a new medicine 💊')
		print('2. Display all bills 🎫')
		print('3. Display all medicines 📃')
		print('4. Search a medicine 🔍')
		print('5. Modify an existing entry 🔁')
		print('6. Delete an existing entry ❎')
		print('7. Log Out 🔙')
		print()
		choice = int(input('Enter a choice: '))
		if choice < 1 or choice > 7:
			print('❌ Invalid input! Try again', end='')
			delay(2)
			continue
		if choice == 7:
			break
		execute_function_idx(admin_functions, choice - 1)

def login_admin():
	clearscreen()
	print('\n\n')
	WRONG_CREDS = False
	usr = input('Enter username: ')
	if usr == 'admin':
		pwd = input('Enter password: ')
		if pwd == '1234':
			print('✅ Credentials verified! Logging in ', end='')
			delay(8, sleeptime=0.15, char='🟩')
			admin_workflow()
		else:
			WRONG_CREDS = True
	else:
		WRONG_CREDS = True
	if WRONG_CREDS:
		print('❌ Invalid credentials. Going back to previous screen', end='')
		delay(3)

def new_order():
	new_bill = Bill(med_table)
	bill_table.insert(new_bill)
	wait_input = input('Press enter to continue...↩')

def search_order():
	phone_number_to_search = input('Enter bill ID to search: ')
	did_find_bill = bill_table.retrieve(phone_number_to_search)
	print('Searching for bill', end='')
	delay(5, sleeptime=0.25)
	print('Search complete!\n')
	if did_find_bill:
		print('✅ Bill found.')
		print(did_find_bill)
	else:
		print('❌ Bill not found!')
	wait_input = input('Press enter to continue...↩')

def update_order():
	bill_id_to_search = input('Enter bill ID to modify: ')
	print('Searching for bill', end='')
	delay(3, sleeptime=0.25)
	print('Search complete!\n')
	did_find_bill = bill_table.update(bill_id_to_search, med_table)
	if did_find_bill:
		print('Updating the database', end='')
		delay(4, sleeptime=0.25)
		print('✅ Details updated.')
	else:
		print('❌ Bill not found!')
	wait_input = input('Press enter to continue...↩')

def delete_order():
	bill_id_to_search = input('Enter bill ID to delete: ')
	print('Searching for bill', end='')
	delay(3, sleeptime=0.25)
	print('Search complete!\n')
	did_find_bill = bill_table.delete(bill_id_to_search)
	if did_find_bill:
		print('Deleting the bill record', end='')
		delay(4, sleeptime=0.25)
		print('✅ Details deleted!')
	else:
		print('❌ Bill not found!')
	wait_input = input('Press enter to continue...↩')

clearscreen()

TABLE_SIZE = 100

print('--------------PHARMACY MANAGEMENT SYSTEM 💊--------------\n\n')
print('1. Read data from files 📁')
print('2. Create new tables 📑\n')
choice = int(input('Enter your choice: '))
if choice == 1:
	try:
		print('📂 Reading the files', end='')
		delay(1)
		with open(MED_FILENAME, 'rb') as pickle_file:
			med_table = pickle.load(pickle_file)
		delay(1)
		with open(BILL_FILENAME, 'rb') as pickle_file:
			bill_table = pickle.load(pickle_file)
		delay(1)
		print('✅ Data loaded successfully!')
	except:
		print('❌ Error occurred, couldn\'t read files!')
		choice = 2
if choice == 2:
	print('🔃 Creating new tables', end='')
	delay(3, 0.25)
	med_table = MedicineHash(TABLE_SIZE)
	bill_table = BillHash(TABLE_SIZE)
	print(' Tables created successfully!')
wait_input = input('Press enter to continue...↩')
print('\nLoading main menu ', end='')
delay(4, 0.25, '⬜')

while True:
	clearscreen()
	print('--------------PHARMACY MANAGEMENT SYSTEM 💊--------------\n\n')
	print('1. Login as Admin 🔐')
	print('2. New Order 🆕')
	print('3. Search Order 🔍')
	print('4. Modify Order 🔀')
	print('5. Delete Order 🚮')
	print('6. Save and Exit 📁\n')
	print()
	choice = int(input('Enter your choice: '))
	if choice == 1:
		login_admin()
	elif choice == 2:
		new_order()
	elif choice == 3:
		search_order()
	elif choice == 4:
		update_order()
	elif choice == 5:
		delete_order()
	elif choice == 6:
		print('📂 Saving the file', end='')
		delay(1)
		try:
			with open(MED_FILENAME, 'wb') as pickle_file:
				pickle.dump(med_table, pickle_file)
			delay(1)
			with open(BILL_FILENAME, 'wb') as pickle_file:
				pickle.dump(bill_table, pickle_file)
			delay(1)
			print(' Successfully saved! ✅')
		except:
			print(' Error while saving! ❌')
		break
	else:
		print('❌ Invalid choice! Try again', end='')
		delay(3)
