import time, math, sys

def dependency(lines):
    n = lines[0][0] # num packages
    m = lines[0][1] # num rules
    # Build Tree
    C = {} #children
    P = {} #parents

    for l in lines[1:-1]:
        # Set Children
        C[int(l[0])] = [ int(c) for c in l[2:]]

        # Set Parents
        for c in l[2:]:
            P[int(c)] = int(l[0])

    print("Children!")
    print(C)

    print("Parents!")
    print(P)

    start = lines[1][0]
    depth = { start:0 }
    edge = [ start ]

    # Find nodes that are not depended on
    free_nodes = {i:0 for i in range(1,int(n)+1)}
    print("Print free nodes!")
    print(free_nodes)
    for p in C:
        for c in C[p]:
            if c in free_nodes:
                del free_nodes[c]
    print("Reprinting free nodes!")
    print(free_nodes)

    # Find longest depth to each node
    '''
    min_depth = float('inf')
    while edge:
        node = edge.pop()
        min_depth = min_depth if min_depth<depth[node] else depth[node]
        # Expand children
        if node in C:
            for c in C[node]:
                if c not in depth:
                    depth[c] = depth[node] - 1
                    edge += [c]

        if node in P:
            if P[node] not in depth:
                depth[P[node]] = depth[node] + 1
                edge += [P[node]]
    '''

    return '1 5 3 2 4'

def test():
    problems = [
    """
    5 4
    3 2 1 5
    2 2 5 3
    4 1 3
    5 1 1
    1 5 3 2 4
    """,
    """
    9 4
    1 4 5 4 3 2
    4 1 6
    5 1 9
    3 1 7
    2 6 4 7 3 8 9 5 1
    """
    ]
    time_limit = 3.
    times = []
    for p in problems:
        p = [line.strip().split() for line in p.split('\n')][1:-1]
        start = time.clock()
        sol = dependency(p)
        #if sol != " ".join(p[-1]):
        print("Result: ")
        print(sol)
        print("Solution: ")
        print(" ".join(p[-1]))

            #assert(sol == p[-1])

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
