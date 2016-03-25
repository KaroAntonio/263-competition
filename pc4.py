import time, sys, math, random, queue, random
from depq import DEPQ

class PowerHash():
	def __init__(self,k,s=3):
		self.size = s
		self.places = 10**int(s)
		self.powers = [10**int(i*s) for i in range(k)]
		self.hashes = {}
		self.mem = {i:{} for i in range(k)}
		self.hash_counter = 0
		self.unique = {}

	def get(self,h,i):
		# return 3 digits at index i*3
		return ((self.hashes[h]//self.powers[i])%self.places)
		if h not in self.mem[i]:
			self.mem[i][h] = ((self.hashes[h]//self.powers[i])%self.places)
		return self.mem[i][h]

	def hash(self,a):
		u = hash(a)
		self.hash_counter += 2
		if u not in self.unique: self.unique[u] = self.hash_counter
		return self.unique[u]

	def array_hash(self, S):
		h = 0
		for i in range(len(S)):
			e = S[i]
			h += e*(10**(i*3))
		return h

	def __setitem__(self,h,a):
		self.hashes[h] = a

	def __getitem__(self,h):
		return self.hashes[h]

def smallest_sums(lines):
	k = int(lines[0][0])
	km1 = k - 1
	kp1 = k + 1
	A = [[int(e) for e in l] for l in lines[1:-1]] # The Super Array
	for a in A:
		a.sort()
	S = []	# Sums
	P = PowerHash(k,3)		# ( , granularity of PowerHash - 1 is risky- >=3 is ideal)
	h0 = 0
	s0 = sum([A[i][0] for i in range(k)])
	P[h0] = 0
	#E = queue.PriorityQueue() # edge: next smallest sums k:sum v:(index array)
	#E.put((s0,h0)) # (sum,hash) for first element
	E = DEPQ()
	E.insert(h0,s0)
	X = {h0:{}}		# explored sums, k:str(index array) v:- ~hash([0,...]) = 0

	def update(Xh,i,di,hidi):
		Xh[i] = 1 if i not in Xh else hidi
		if Xh[i] == 0: del Xh[i]

	def rollback(Xh,i,di):
		Xh[i] = 1 if i not in Xh else Xh[i]-di
		if Xh[i] == 0: del Xh[i]

	def explore_neighbour(A,Ai,P,Ph,E,X,Xh,S,h,h_i,i,di):
		# Make a uniquely hashable token in the form (1:[list of indices]2:[list of indices])
		#update(X[h],i,di)
		#t = str(X[h])
		#rollback(X[h],i,di)
		#h_ = hash(t)
		a = Ph + (di * P.powers[i])		# new big int array		0.5s		
		h_ = hash(a) 	# the hash of the new   			< 0.5s
		if h_ not in X:
			P[h_] = a				# 0.5s
			hidi = h_i + di
			s = S[-1] - (Ai[h_i] - Ai[hidi])		# 1s
			#E.put((s,h_))
			if E.size() < k or E.size()==k and s < E.high():
				E.insert(h_,s)	
				X[h_] = Xh.copy() 	# Add to explored set 			0.5s
				update(X[h_],i,di,hidi)
				if E.size() == kp1: E.popfirst()

	for _ in range(k):
		# Remove smallest from edge (sum, hash)
		h,s = E.poplast()
		#s,h = E.get()
		# Visit smallest
		S += [s]
		Xh = X[h]
		Ph = P[h]
		for i in range(k):
			Ai = A[i]
			h_i = 0 if i not in Xh else Xh[i]		
			if h_i > 0: explore_neighbour(A,Ai,P,Ph,E,X,Xh,S,h,h_i,i,-1) # Potentially uneccessary
			if h_i < km1: explore_neighbour(A,Ai,P,Ph,E,X,Xh,S,h,h_i,i,1)
		# print(E.size(),_)

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
    for i in range(1,5):
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

if __name__ == "__main__":
	# test()
	test_time(100,750)
