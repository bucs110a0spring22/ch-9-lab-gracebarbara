class Rectangle:
	def __init__(self, x, y, h, w):
		x=self.x
		y=self.y
		h=self.height
		w=self.width
		if x <= 0:
			x=0
		if y <= 0:
			y=0
		if h <= 0:
			h=0
		if w <= 0:
			w=0
			
	def str(self):
		string="(x:"+ str(self.x) +",y:"+ str(self.y) +") width:"+ str(self.width) +" height:"+ str(self.height)
		return string
		