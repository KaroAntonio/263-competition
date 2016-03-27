import time, sys, math, random, queue, random
from heapq import heapify, heappop, heappush

# Inspired by https://programmingpraxis.com/2013/09/27/double-ended-priority-queues/
class DEPQ(object):
	def __init__(self):
		self.entry_finder = {}
		self.counter = 0
		self.minq, self.maxq = [], []

	def next_id(self):
		self.counter += 1
		return self.counter

	def insert(self, e, p, id_=None):
		id_ = self.next_id()
		mine, maxe = [p, e, id_],  [-p, e, id_]
		heappush(self.minq, mine)
		heappush(self.maxq, maxe)
		self.entry_finder[id_] = mine, maxe

	def min(self):
		return self.minq[0][0]

	def max(self):
		return -self.maxq[0][0]

	def pop_min(self):
		p, e, id_ = heappop(self.minq)
		entries = self.entry_finder.pop(id_)
		entries[1][2] = float('-inf')
		return e, p

	def pop_max(self):
		p, e, id_ = heappop(self.maxq)
		entries = self.entry_finder.pop(id_)
		entries[0][2] = float('-inf')
		return e, -p

	def __setitem__(self, p, e):
		self.insert(e, p)

	def __len__(self):
		return len(self.entry_finder)

class PowerHash():
	def __init__(self,k,s=3):
		self.size = s
		self.powers = [10**int(i*s) for i in range(k)]
		self.hashes = {}

	def __setitem__(self,h,a):
		self.hashes[h] = a

	def __getitem__(self,h):
		return self.hashes[h]

def smallest_sums(lines):
	# INIT
	k = int(lines[0][0])
	km1,kp1 = k - 1,k + 1
	A = [[int(e) for e in l] for l in lines[1:-1]] # The Super Array
	for a in A:
		a.sort()
	h,s = 0,sum([A[i][0] for i in range(k)])
	S = []	# Sums
	P = PowerHash(k,3)	
	P[h] = 0
	E = DEPQ()	# EDGE access to max,min in order to keep track of top k sums
	E[s] = h
	X = {h:{}}	# k: hash v: a dictionary of all non-zero indices in this sum

	def update(Xh,i,di,hidi):
		Xh[i] = 1 if i not in Xh else hidi
		if Xh[i] == 0: del Xh[i]

	def rollback(Xh,i,di):
		Xh[i] = 1 if i not in Xh else Xh[i]-di
		if Xh[i] == 0: del Xh[i]

	def explore_neighbour(A,Ai,P,Ph,E,X,Xh,S,h,h_i,i,di):
		a = Ph + (di * P.powers[i])		# new big int array		
		h_ = hash(a) 	# the hash of the new array, used for fast dictionary			
		if h_ not in X:
			P[h_] = a				
			hidi = h_i + di
			s = S[-1] - (Ai[h_i] - Ai[hidi])	
			if len(E) < k or len(E)==k and s < E.max():
				E[s] = h_	
				X[h_] = Xh.copy() 	# Add to explored set 		
				update(X[h_],i,di,hidi)
				if len(E) == kp1: E.pop_max()

	for _ in range(k):
		h,s = E.pop_min()
		S += [s]
		Xh = X[h]
		Ph = P[h]
		for i in range(k):
			Ai = A[i]
			h_i = 0 if i not in Xh else Xh[i]		
			if h_i > 0: explore_neighbour(A,Ai,P,Ph,E,X,Xh,S,h,h_i,i,-1) # Potentially uneccessary
			if h_i < km1: explore_neighbour(A,Ai,P,Ph,E,X,Xh,S,h,h_i,i,1)

	S.sort()
	return S

def gen_problems(n,k):
	'''
	gen n problems of size k
	with no solutions
	'''
	problems = []
	for i in range(n):
		A = []
		for j in range(k):
			row =  []
			for l in range(k):
				row += [int(random.random()*k)]
			A += [row]
		problems += [A]
	return problems

def test_time(n,k):
	problems = gen_problems(n,k)
	time_limit = 5.
	times = []
	for p in problems:
		start = time.clock()
		smallest_sums(p)
		end = time.clock()
		t = end-start
		times += [t]
		print (t)

	if all([t< time_limit for t in times]):
		print("All Solved within " + str(time_limit) + "s")

def test():
    # Load test files
    problems = []
    for i in range(1,6):
        with open('test_files/pc4/test'+str(i),'r') as f:
            problems += ["".join(f.readlines())]

    time_limit = 5.
    times = []
    for p in problems:
        p = [line.strip().split() for line in p.split('\n')][0:-1]
        start = time.clock()
        sol = [str(e) for e in smallest_sums(p)]
        end = time.clock()
        ans = p[-1]
        if sol != ans:
            print(sol, ans)
            assert(sol == p[-1])
        t = end-start
        times += [t]
        print (t)

    if all([t< time_limit for t in times]):
        print("All Solved within " + str(time_limit) + "s")

def run():
	f = sys.stdin
	lines = []
	for line in f:
		if line == None or len(line.strip()) == 0:
			break
		lines += [line.strip().split()]

	sol = [str(s) for s in smallest_sums(lines)]

	print(" ".join(sol).strip())
	exit(0)

if __name__ == "__main__":
	run()
	#test()
	#test_time(100,750)
