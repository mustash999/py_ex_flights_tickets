from amadeus import		Client, ResponseError
import 					json
from dotenv import 		load_dotenv
import 					os

class FlightSearch:
	def __init__(self):
		load_dotenv()
		self.amadeus = Client(
		client_id= 			os.getenv('AMADEUS_API_KEY'),
		client_secret= 		os.getenv('AMADEUS_API_SECRET')
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


