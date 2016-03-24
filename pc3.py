import math, sys, time

def process_lines(lines):
	cases = []
	b = True # beggining
	ptr = 1
	for i in range(int(lines[0][0])):
		case = {}
		case['n'] = int(lines[ptr][0])
		case['m'] = int(lines[ptr][1])
		case['o'] = []
		ptr += 1
		for j in range(case['n']):
			case['o'] += [int(lines[ptr][0])]
			ptr += 1
		case['f'] = {}
		for j in range(case['m']):
			F = [ int(lines[ptr][0]), int(lines[ptr][1])]
			for k in range(2):
				f1 = F[k]
				f2 = F[(k+1)%2]
				if f1 in case['f']:
					case['f'][f1] += [f2]
				else:
					case['f'][f1] = [f2]
			ptr += 1
		cases += [case]
	
	return cases

def is_solvable(case):
	# We are trying to 

	pass




def mo_problems(lines):
	cases = process_lines(lines)

	results = []
	for case in cases:
		results += [is_solvable(case)]
		print(case)
		print(sum(case['o']))

	return '\n'.join(results)

def test():
	problems = [
	"""
	2 
	5 3 
	100 
	-75 
	-25 
	-42 
	42 
	0 1 
	1 2 
	3 4 
	4 2 
	15 
	20 
	-10 
	-25 
	0 2 
	1 3	
	""",
	]
	time_limit = 3.
	times = []
	for p in problems:
		p = [line.strip().split() for line in p.split('\n')][1:-1]
		start = time.clock()
		sol = mo_problems(p)
		if sol != " ".join(p[-1]):
			print(sol, p[-1])
			assert(sol == p[-1])

		end = time.clock()
		t = end-start
		times += [t]
		if t > time_limit:
			print (t, p)

	if all([t< time_limit for t in times]):
		print(times)
		print("All Solved within " + str(time_limit) + "s")

if __name__ == "__main__":
	test()
