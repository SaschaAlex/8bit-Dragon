from Instruction_spec import INSTRUCTION_SPEC_LIST,CB_INSTRUCTION_LIST

unique_instruction = set()

for instruction_spec in INSTRUCTION_SPEC_LIST:
	unique_instruction.add(instruction_spec.name)

for instruction_spec in CB_INSTRUCTION_LIST:
	unique_instruction.add(instruction_spec.name)

print(unique_instruction)
print(f"Unique instruction : {len(unique_instruction)}")