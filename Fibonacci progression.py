class Progression:

	def __init__(self, start=0):
		self._current = start

	def _advance(self):

		self._current += 1

	def __next__(self):
        
			answer = self._current		
			self._advance()				
			return answer				


	def __iter__(self):
		return self

	def print_progression(self, n):
		print(" ".join(str(next(self)) for i in range(n)))


obj = Progression()
obj.print_progression(10)

class Fibonacci(Progression):
	
	
	def __init__(self, num1 = 0, num2= 1 ):
		super().__init__(num1)
		self.a = num1
		self.b = num2

	def _advance(self):
		newfib= self.a + self.b
		self.b = self.a
		self.a= newfib
		self._current = self.a


fSeq = Fibonacci()
fSeq.print_progression(10)
