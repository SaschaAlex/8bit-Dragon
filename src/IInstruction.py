from abc import abstractmethod
from Instruction_spec import InstructionSpec

class IInstruction:
	def __init__(self,spec : InstructionSpec):
		self.sepc = spec

	@abstractmethod
	def execute(self,state,operand) -> None:
		pass

	def generate_code(self,operand) -> str:
		return f"{self.spec.name} {self.spec.operand}" 	

