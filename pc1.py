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
        # value of depth dict is num of moves you have to make to reach the key

        # Build Moves k:move, v:cost
        moves = {u:1,-d:1}

        # Check if not possible to get there at all
        if y > x:
                if (y - x) < u and (y - x) < d and (y == x):
                        return 0

        front = -1
        back = 0

        while True:
                front += 1
                floor = edge[front]
                if floor == y:
                        return depth[floor]

                for move in moves:
                        floor_ = floor + move
                        if floor_ not in depth and floor_ <= n and floor_ >= 1:
                                depth[floor_] = depth[floor]+moves[move]
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
                        print (t, seq_len,'OVERTIME')
                else: print(t, seq_len)

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
                                [4731341, 827037, 3853750, 1625424, 2564489, 3839464]]
        

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
                if t > time_limit:
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

if __name__ == "__main__":

        # test_time(gen_problems(100))
        test()

        '''
    f = sys.stdin
    line = f.readline().strip()
    n = int(line)
    line = f.readline().strip()
    array = line.split()
    for i in range(n):
        if array[i] == '42':
            print(i+1)
            exit(0)


    print(0)
        '''
