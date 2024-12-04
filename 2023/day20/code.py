
import numpy as np
from typing import List
import copy
import re

# with open("input.txt", "r") as file:
with open("example.txt", "r") as file:
	lines = file.readlines()


########### PART 1

def get_ind(letter: str) -> int:
	if letter == 'x':
		return 0
	if letter == 'm':
		return 1
	if letter == 'a':
		return 2
	if letter == 's':
		return 3

def find_next_flow(obj, flow_name: str):

	flow = flows[flow_name]

	operations = flow.split(',')
	for op in operations[:-1]:

		letter, segno, valore, new_flow = re.findall(r"(\w)(.)(\d+):(\w+)", op)[0]

		if segno=='>':
			if obj[get_ind(letter)]>int(valore):
				return new_flow
		elif segno=='<':
			if obj[get_ind(letter)]<int(valore):
				return new_flow
		
	last_flow = operations[-1]
	return last_flow

objects=[]
flows=dict()

for ind,line in enumerate(lines):
	if line[:2] == "{x":
		temp = re.findall(r"x=(\d+),m=(\d+),a=(\d+),s=(\d+)", line)[0]
		objects.append([int(i) for i in temp])

	elif len(line)>1:
		flow_name = line.split("{")[0]
		flow_text = re.findall(r"\{.*\}", line)[0][1:-1]
		flows[flow_name] = flow_text

total=0
for obj in objects:

	cur_flow = 'in'
	while cur_flow not in ['A', 'R']:
		cur_flow = find_next_flow(obj, cur_flow)

	if cur_flow=='A':
		total += np.sum([int(i) for i in obj])

print(total)


########### PART 2

def find_successors(flow_name: str):

	if flow_name in ['A', 'R']:
		return set(flow_name)

	successors=set()

	flow = flows[flow_name]

	operations = flow.split(',')
	for op in operations[:-1]:

		new_flow = re.findall(r"\w.\d+:(\w+)", op)[0]
		successors.add(new_flow)
		successors = successors | find_successors(new_flow)
	
	last_flow = operations[-1]
	successors.add(last_flow) 
	successors = successors | find_successors(last_flow)

	return successors

successors_dic=dict()
for flow_name in flows:
	successors_dic[flow_name]=find_successors(flow_name)
print(successors_dic)


def inverti_segno(formula):
	if formula[1]=='>':
		formula = re.sub('>', '<', formula)
		return formula
	elif formula[1]=='<':
		formula = re.sub('<', '>', formula)
		return formula
	else:
		raise ValueError


accepted_flows=[]

def find_accepted_flows(flow_name: str):

	if flow_name in ['A', 'R']:
		return [[flow_name]]

	result = []

	flow = flows[flow_name]

	operations = flow.split(',')

	L = len(operations)
	filtri_saltati = []
	for ind_op, op in enumerate(operations[:-1]):

		formula,new_flow = re.findall(r"(\w.\d+):(\w+)", op)[0]		
		chains = find_accepted_flows(new_flow)

		for ind_chain,chain in enumerate(chains):
			chains[ind_chain].append(formula)
			for filtro in filtri_saltati:
				chains[ind_chain].append(filtro)

		filtri_saltati.append(inverti_segno(formula))

		result += chains

	last_flow = operations[-1]
	chains = find_accepted_flows(last_flow)

	for ind_chain,chain in enumerate(chains):
		chains[ind_chain].append(formula)
		for filtro in filtri_saltati:
			chains[ind_chain].append(filtro)

	result += chains

	return result

accepted = find_accepted_flows('in')
accepted = [i[1:] for i in accepted if i[0]=='A']

print("ACCEPTED:", accepted)
print(f"{len(accepted)} ACCEPTED:")

total=0
for chain in accepted:
	sum_per_letter = [0,0,0,0]
	for letter in ['x', 'm', 'a', 's']:
		for valore in range(1,4001):
			ok=True
			for op in chain:
				if ok and op[0]==letter:
					if op[1]=='<' and valore>=int(op[2:]):
						ok=False
					if op[1]=='>' and valore<=int(op[2:]):
						ok=False

			if ok:
				sum_per_letter[get_ind(letter)] += 1
	print(sum_per_letter)
	total += np.prod(sum_per_letter)

print(total)








# non guarade solo il filtro ch passa ma anche chi non è passato
# ovvero nella prima op metto il filtro che ha passato, ma nella seconda 
# op metto il filtro che ha passato ma anche il precedente che non ha passato, 
# invertendo segno
