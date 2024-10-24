from IInstruction import IInstruction
 
# Refer to the following ressource https://meganesu.github.io/generate-gb-opcodes/

class ADD_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented 

class AND_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class RLA_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class HALT_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class CALL_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class SCF_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class SRA_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class RES_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class PUSH_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class LDH_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class DAA_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class RR_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class XOR_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class JP_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class SLA_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class JR_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class ADC_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class SET_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class LD_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class DI_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class RETI_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class RRCA_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class RRC_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class SWAP_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class INC_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class OR_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class SRL_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class RLCA_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class RL_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class PREFIX_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented
	
class CCF_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class CPL_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class BIT_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class SBC_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class RST_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class EI_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class DEC_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class CP_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class POP_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class STOP_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class RET_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class NOP_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class RLC_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented

class SUB_Instruction(IInstruction):
	def execute(self, state, operand):
		raise NotImplemented
