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
	# We perform a DFS and sum the node values of each subgraph

	class DFS():
		def __init__(self,G, N):
			self.C = {};	# Color
			self.F = {};	# Finish time
			self.D = {};	# Distance
			self.P = {};	# Parent
			self.t = 0;		# time
			self.G = G;		# GRaph adj list
			self.N = N;		# Node Values	
			#init
			for v in range(len(N)):
				self.C[v] = 0
				self.P[v] = None
				self.F[v] = self.D[v] = float('inf')
	
	# graph
	g = DFS(case['f'],case['o'])
	def DFS_visit(g,u):
		# Itiratively traverse graph
		graph_sum = 0
		edge = [u]
		while True:
			u = edge.pop()
			graph_sum += g.N[u]
			g.C[u] = 1
			if u in g.G:
				for v in g.G[u]:
					if g.C[v] == 0:
						g.C[v] = 1
						edge += [v]
			if len(edge) == 0:
				return graph_sum

	sums = [] # sums of each subgraph
	for v in range(len(g.N)):
		if g.C[v] == 0:
			sums += [DFS_visit(g,v)]

	return not any(sums)

def mo_problems(lines):
	cases = process_lines(lines)

	results = []
	for case in cases:
		result = is_solvable(case)
		results += [result]

	return "\n".join(['POSSIBLE' if r else 'IMPOSSIBLE' for r in results])

def gen_case():
	# generate a case for testing
	pass

def test():
	# Load test files
	problems = []
	for i in range(1,5):
		with open('test_files/pc3/test'+str(i),'r') as f:
			problems += ["".join(f.readlines())]

	time_limit = 7.
	times = []
	for p in problems:
		p = [line.strip().split() for line in p.split('\n')][0:-1]
		start = time.clock()
		sol = mo_problems(p)
		ans = "\n".join([e[0] for e in p[-1 * int(p[0][0]):]])
		if sol != ans:
			print(sol, ans)
			assert(sol == p[-1])

		end = time.clock()
		t = end-start
		times += [t]
		if t > time_limit:
			print (t, p)

	if all([t< time_limit for t in times]):
		print("All Solved within " + str(time_limit) + "s")

if __name__ == "__main__":
	test()
