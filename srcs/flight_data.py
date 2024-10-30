
class FlightData:
	#This class is responsible for structuring the flight data.
	def __init__(self):
		self.id = None
		self.price = None
		self.airline = None
		self.number_of_changes = None
		self.origin_airport = None
		self.destination_airport = None
		self.out_date = None
		self.return_date = None
		self.stop_overs = None
		self.via_city = None
		self.link = None


	def update_data(self, data):
		self.id = data['id']
		self.price = data['price']
		self.airline = data['itineraries']
		self.number_of_changes = data['number_of_changes']
		self.origin_airport = data['origin_airport']
		self.destination_airport = data['destination_airport']
		self.out_date = data['out_date']
		self.return_date = data['return_date']
		self.stop_overs = data['stop_overs']
		self.via_city = data['via_city']
		self.link = data['link']
		return self
	
	def get_flight_details(self):
		pass

import json	
with open('data.json') as file:
	data = json.load(file)
	for entry in data:
		print(entry)
		flight = FlightData()
		flight.update_data(entry)
		print(flight)

def __str__(self):
		return (
			f"--------------------------------flight No{self.id}-----------------------------------\n"
			f"from {self.origin_airport} \t to {self.destination_airport} \t Price: {self.price} \t Duration:{self.duration}  \n" 
			f"to: {self.destination_airport} on: {self.out_date} and return on: {self.return_date} "
			f"with {self.number_of_changes} changes\n"
		)
