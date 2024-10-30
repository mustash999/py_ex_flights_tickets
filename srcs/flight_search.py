from amadeus import		Client, ResponseError
import 					json
from dotenv import 		load_dotenv
import 					os

class FlightSearch:
	def __init__(self):
		load_dotenv()
		self.amadeus = Client(
		client_id= 			os.getenv('AMADEUS_KEY'),
		client_secret= 		os.getenv('AMADEUS_SECRET')
	)

	def airline_routes(self, airline_code):
		'''
		What are the destinations served by the British Airways (BA)?
		'''
		try:
			response = self.amadeus.airline.destinations.get(airlineCode=airline_code)
			return response.data
		except ResponseError as error:
			raise error
	
	def airport_routes(self, origin_IataCode):
		try:
			'''
			What are the destinations served by MAD airport?
			'''
			response = self.amadeus.airport.direct_destinations.get(
				departureAirportCode=		origin_IataCode)
			return response.data
		except ResponseError as error:
			raise error

	def find_return_flight(self, origin, destination, dep_date, ret_date , travelers_count):
		'''
		What is the cheapest flight from London to Paris on 2022-08-01 for 2 adults?
		'''
		try:
			response = self.amadeus.shopping.flight_offers_search.get(
				originLocationCode=			origin,
				destinationLocationCode=	destination,
				departureDate=				dep_date,
				returnDate=					ret_date,
				adults=						travelers_count
			)
			return response.data
		except ResponseError as error:
			raise error
		
	def finf_one_way_flight(self, origin, destination, dep_date, travelers_count):
		'''
		What is the cheapest flight from London to Paris on 2022-08-01 for 2 adults?
		'''
		try:
			response = self.amadeus.shopping.flight_offers_search.get(
				originLocationCode=			origin,
				destinationLocationCode=	destination,
				departureDate=				dep_date,
				adults=						travelers_count
			)
			return response.data
		except ResponseError as error:
			raise error
		
	

	def get_iata_code(self, city_name):
		'''
		What is the IATA code for Paris?
		'''
		try:
			response = self.amadeus.reference_data.locations.get(
				keyword=	city_name,
				subType=	'AIRPORT'
			)
			return response.data[0]['iataCode']
		except ResponseError as error:
			raise error



""" 	def random_cheap(self, origin, date):
		try:
			response = self.amadeus.shopping.flight_destinations.get(origin=origin, departureDate=date)
			return response.data
		except ResponseError as error:
			raise error

	def find_cheapest_date(self, origin, destination):
		'''
		What is the cheapest date for a flight from London to Paris?
		'''
		try:
			response = self.amadeus.shopping.flight_dates.get(
				origin=			origin,
				destination=	destination
			)
			return response.data
		except ResponseError as error:
			raise error
		 """

search=FlightSearch()
search_result=search.find_cheapest_flight('HAM', 'CDG', '2024-12-24', '2024-12-26', 1)
with open('data_return.json', 'w') as file:
	json.dump(search_result, file)
	print(search_result)
