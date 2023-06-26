import pickle
from Medicine import Medicine

FILENAME = 'medicine-hash.pkl'

class MedicineHash:
	def __init__(self, table_size: int):
		self.table_size = table_size
		self.hash_table = [None] * self.table_size
	
	def add_meds_to_table(self, bill):
		for item, count, rate in bill:
			med: Medicine = self.retrieve(item)
			med.set_count(med.get_count() + count)
        
	def deduct_meds_from_table(self, bill):
		for item, count, rate in bill:
			med: Medicine = self.retrieve(item)
			med.set_count(med.get_count() - count)

	def hash_medicine_str(self, key_str: str):
		hash_value = 0
		prime = 31
		for char in key_str:
			hash_value = (hash_value * prime + ord(char)) % self.table_size
		return hash_value
	
	def insert(self, medicine_obj: Medicine):
		key_str = medicine_obj.get_name()
		hash_value = self.hash_medicine_str(key_str)
		
		if self.hash_table[hash_value] is None:
			self.hash_table[hash_value] = (key_str, medicine_obj)
			self.save_records()
			return True
		else:
			#? linear probing
			i = (hash_value + 1) % self.table_size
			while i != hash_value:
				if self.hash_table[i] is None:
					self.hash_table[i] = (key_str, medicine_obj)
					self.save_records()
					return True
				i = (i + 1) % self.table_size
			self.save_records()
			return False
	
	# key_str is supposed to be medicine name
	def retrieve(self, key_str: str):
		hash_value = self.hash_medicine_str(key_str)
		if self.hash_table[hash_value] is None:
			return None
		elif self.hash_table[hash_value][0] == key_str:
			return self.hash_table[hash_value][1]
		else:
			#? linear probing
			i = (hash_value + 1) % self.table_size
			while i != hash_value:
				if self.hash_table[i][0] == key_str:
					return self.hash_table[i][1]
				i = (i + 1) % self.table_size
			return None
	
	# key_str is supposed to be medicine name
	def delete(self, key_str: int):
		hash_value = self.hash_medicine_str(key_str)
		if self.hash_table[hash_value] is None:
			self.save_records()
			return False
		elif self.hash_table[hash_value][0] == key_str:
			self.hash_table[hash_value] = None
			self.save_records()
			return True
		else:
			#? linear probing
			i = (hash_value + 1) % self.table_size
			while i != hash_value:
				if self.hash_table[i][0] == key_str:
					self.hash_table[i] = None
					self.save_records()
					return True
				i = (i + 1) % self.table_size
			self.save_records()
			return False
	
	# key_str is supposed to be medicine name
	def update(self, key_str: int):
		hash_value = self.hash_medicine_str(key_str)
		if self.hash_table[hash_value] is None:
			self.save_records()
			return False
		elif self.hash_table[hash_value][0] == key_str:
			self.hash_table[hash_value][1].update_details()
			self.save_records()
			return True
		else:
			#? linear probing
			i = (hash_value + 1) % self.table_size
			while i != hash_value:
				if self.hash_table[i][0] == key_str:
					self.hash_table[i][1].update_details()
					self.save_records()
					return True
				i = (i + 1) % self.table_size
			self.save_records()
			return False
	
	def get_records(self):
		existing_records = list()
		for i in range(self.table_size):
			ith_record = self.hash_table[i]
			if ith_record is not None:
				existing_records.append(ith_record)
		return existing_records
	
	def save_records(self):
		records = self.get_records()
		with open('med-hash.txt', 'w') as meds_file:
			for record in records:
				meds_file.write(record[1].get_string() + '\n')
	
	def get_names_rates(self):
		records = self.get_records()
		names_rates = dict()
		for record in records:
			names_rates[record[0]] = record[1].get_price()
		return names_rates