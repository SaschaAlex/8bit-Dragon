class CPU:
	def __init__(self):
		self.PC = 0x0000 # Program counter
		self.AF = 0x0000 # AF register (F is the flag register)
		self.BC = 0x0000 # GC register
		self.DE = 0x0000 # DE register
		self.HL = 0x0000 # HL register
		self.SP = 0x0000 # Stack pointer 
		self.CB_MODE = False
		self.cycles = 0 

