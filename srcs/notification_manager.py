from twilio.rest import		Client
from dotenv import			load_dotenv
import						os

class NotificationManager:
	def __init__(self):
		load_dotenv()
		account_sid =	os.getenv('TWILIO_SID')
		auth_token =	os.getenv('TWILIO_TOKEN')
		self.client = 	Client(account_sid, auth_token)
	
	def send_sms(self, bodytext):
		message = self.client.messages.create(
			from_=os.getenv('TWILIO_NUM'),
			body=bodytext,
			to=os.getenv('MY_NUM'))
		print(message.sid)



send = NotificationManager()
send.send_sms("Hello, this is a test message from the Notification Manager.")