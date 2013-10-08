class UI_Diagnosis():
	def __init__(self):
		#Tab 1
		self.name = ''
		self.sex = ''
		self.age = ''
		self.job = ''
		self.nation = ''
		self.address = ''
		self.eduDegree = ''
		#Tab2
		
		#Others
		self.images = []
	def __str__(self):
		items = [x+":"+str(getattr(self, x))  for x in dir(self)]
		return "\n".join(items)
		