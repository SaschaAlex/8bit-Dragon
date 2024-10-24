MEM_8KB = 8192

class Memory:
	def __init__(self):
		self.memory = [0x00] * MEM_8KB
		