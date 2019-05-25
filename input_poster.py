class poster_input():
	def __init__(self , reqs):
		self.reqs = reqs
		self.take_input()

	def take_input(self):
		print('Enter the Title : ')
		self.reqs['title'] = input()

		print('Enter the title of talk1 : ')
		self.reqs['talk1'] = input()

		print('Enter the title of talk2 : ')
		self.reqs['talk2'] = input()


		print('Enter the speaker of talk1 : ')
		self.reqs['spk1'] = input()

		print('Enter the speaker of talk2 : ')
		self.reqs['spk2'] = input()


		print('Enter the Venue : ')
		self.reqs['venue'] = input()

		print('Enter the time duration : ')
		self.reqs['time'] = input()


		print('Enter the background color : ')
		self.reqs['bgcolor'] = input()

		print('Enter the font color : ')
		self.reqs['fontcolor'] = input()

	def get_resp(self):
		return self.reqs
