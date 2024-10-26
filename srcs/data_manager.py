import requests
import os
from dotenv import load_dotenv

class DataManager:
	def __init__(self):
		load_dotenv()
		self.destination_data = {}
		self.url = os.getenv('SHEETY_URL')
		self.data = requests.get(self.url)
		
	
	def add_data(self, data):
		response = requests.post(self.url, json=data)
		print(response.text)
	
	def update_data(self, nw_wrp_data):
		newdata 		= nw_wrp_data['mssFlightPrice']
		current_data 	= self.data.json()['mssFlightPrices']

		if all((entry['city'] != newdata['city'] or entry['iataCode'] != newdata['iataCode']) for entry in current_data):
			self.add_data(nw_wrp_data)
			print(f"Added {newdata['city']} to the list")
		else:
			for entry in current_data:
				if (entry['city'] == newdata['city']) and (entry['iataCode'] == newdata['iataCode']):
					if entry['lowestPrice'] > newdata['lowestPrice']:
						id = entry['id']
						requests.put(f"{self.url}/{id}", json=nw_wrp_data)
						print(f"Updated price for {newdata['city']} to {newdata['lowestPrice']}")
					break

data = DataManager()
print(data.data.json())
new_data = {'city': 'Paris', 'iataCode': 'CDG', 'id': 3}
lowes_price = 7
newpricedata = {'mssFlightPrice': {'city': 'Paris', 'iataCode': 'ORY', 'lowestPrice': lowes_price}}
#requests.put(f"{data.url}/3", json=newpricedata)
data.update_data(newpricedata)
#data.add_data(new_data)