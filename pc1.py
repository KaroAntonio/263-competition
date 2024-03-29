import time, math, sys, random

def shortest_seq(n,x,y,u,d):
	'''
	n: total num floors
	x: current floor
	y: target floor
	u: up increment
	d: down increment
	'''

	edge = {0:x}
	depth = {x:0}  # Maps floors to their button distances

	# Build Moves k:move, v:cost
	moves = {u:1,-d:1}

	front = -1
	back = 0

	while True:
		front += 1
		floor = edge[front]
		depth_floor = depth[floor]
		if floor == y:
			return depth_floor

		for move in moves:
			floor_ = floor + move
			if floor_ not in depth and floor_ <= n and floor_ >= 1:
				depth[floor_] = depth_floor+moves[move]
				back += 1
				edge[back] = floor_

		if front == back:
			return 0

def test_time(problems = None, time_limit = 5.):
				
	times = []
	for p in problems:
		start = time.clock()
		seq_len = shortest_seq(p[0],p[1],p[2],p[3],p[4])
		end = time.clock()
		t = end-start
		times += [t]
		if t > time_limit:
			print (t, p, seq_len,'OVERTIME')
		else: print(t, p, seq_len)

	if all([t< time_limit for t in times]):
		print("All Solved within " + str(time_limit) + "s")

	
def test(problems = None):
	if problems == None:
		problems = [
				[10, 1, 10, 2, 3, 7],
				[5000000, 1, 4999999, 445345, 32323, 145822],
				[5000000, 4888888, 7, 2324, 585858, 0],
				[5000000, 4923847, 1, 36465, 58558, 51297],
				[5000000, 1, 2345, 12344,43111, 38276],
				[20, 19, 2, 5, 11, 3],
				[4731341, 827037, 3853750, 1625424, 2564489, 3839464],
				[4458699, 3031437, 2470168, 124451, 360544, 483911]]
	

	time_limit = 5.

	times = []
	for p in problems:
		start = time.clock()
		seq_len = shortest_seq(p[0],p[1],p[2],p[3],p[4])
		if seq_len != p[5]:
			print(seq_len, p[5])
			assert(seq_len == p[5])

		end = time.clock()
		t = end-start
		times += [t]
		print (t, p)

	if all([t< time_limit for t in times]):
		print(times)
		print("All Solved within " + str(time_limit) + "s")

	

def gen_problems(num):
	# gen num problems
	problems = []
	for i in range(num):
		n = int(random.random()*5000000)
		x = int(random.random()*n)
		y = int(random.random()*n)
		u = int(random.random()*n)
		d = int(random.random()*n)
		problems += [[n,x,y,u,d]]


	return problems

def run():
	f = sys.stdin
	lines = []
	line = f.readline().strip()
	lines += line.split()
	seq_len = shortest_seq(int(lines[0]),int(lines[1]),int(lines[2]),int(lines[3]),int(lines[4]))
	print(seq_len)
	exit(0)

if __name__== "__main__":
	run()
	#test_time(gen_problems(100))
	#test()

