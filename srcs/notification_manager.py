from twilio.rest import		Client
from dotenv import			load_dotenv
import						os

class NotificationManager:
	def __init__(self):
		load_dotenv()
		account_sid =	os.getenv('TWILIO_ACCOUNT_SID')
		auth_token =	os.getenv('TWILIO_TOKEN')
		self.client = 	Client(account_sid, auth_token)
	
	def send_sms(self, bodytext):
		message = self.client.messages.create(
			from_='+17324106584',
			body=bodytext,
			to='+34695086573')
		print(message.sid)

