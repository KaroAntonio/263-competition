import time, math, sys

def dependency(lines):
    n = lines[0][0] # num of packages
    m = lines[0][1] # num of rules
    # Build Tree
    C = {} #children

    for l in lines[1:-1]:
        # Set Children
        # mapping dependent nodes to their list of depended on nodes
        C[int(l[0])] = [ int(c) for c in l[2:]]
    
    # Find nodes that are not dependent on other nodes
    free_nodes = {i:0 for i in range(1,int(n)+1)}
    for p in C:
        if p in free_nodes:
            del free_nodes[p]

    # output is a list of the output
    output = []
    starter = 1
    keys = free_nodes.keys()
    t = int(n)
    checker = 0

    # starter looks at each node
    while starter < (t+1) and len(output) < t:
        if starter not in output:
            # If node has no dependencies, can add it to output
            if starter in keys:
                output.append(starter)
                starter = 1
            else:
                # Checking if all depended on nodes are in output
                for i in C.get(starter):
                    if i in output:
                        checker = checker + 1
                if checker == len(C.get(starter)):
                    output.append(starter)
                    starter = 1
                # This runs if all the nodes' dependencies weren't in output
                else:
                    starter = starter + 1

                # Reseting checker for next node
                checker = 0
        # Runs if starter was already in output
        else:
            starter = starter + 1

    # Turning the output list into a string
    string_output = ""
    for i in output:
        string_output = string_output + str(i) + " "

    return string_output

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
    """,
    """
    100 94
1 32 4 5 9 12 16 20 21 23 29 30 36 43 44 45 46 47 48 50 53 54 55 59 60 63 64 70 72 83 85 89 93 95 
2 32 7 9 12 15 17 25 26 27 29 35 40 41 44 45 46 50 51 52 54 56 59 64 69 78 80 82 83 86 88 94 98 100 
3 25 9 11 18 26 34 38 40 55 60 61 63 66 68 69 70 71 73 83 84 85 88 89 92 94 96 
4 30 8 9 11 15 17 21 24 26 28 29 31 35 38 42 43 48 51 58 61 67 71 75 79 81 83 89 91 93 94 97 
5 21 6 22 23 41 44 45 47 50 58 59 60 61 76 78 81 83 89 92 95 96 100 
6 33 14 15 16 19 21 24 28 30 32 33 34 35 45 46 47 51 52 53 54 61 62 69 71 72 74 76 80 83 84 85 87 89 91 
7 19 14 24 32 35 37 39 44 45 48 55 57 72 73 75 83 84 93 94 97 
8 26 11 14 18 19 23 25 26 32 37 49 51 53 55 58 63 65 71 74 77 79 90 91 93 95 97 98 
9 22 19 21 25 26 29 37 39 42 45 52 56 61 62 65 68 69 85 87 88 96 97 100 
10 34 13 14 15 20 22 28 30 31 34 36 38 46 54 59 60 61 66 68 69 71 73 76 78 82 83 85 88 92 93 94 97 98 99 100 
11 22 13 21 28 40 45 46 51 57 59 66 69 72 73 76 77 81 84 90 93 95 96 100 
12 28 13 18 27 28 32 33 35 38 48 52 54 56 57 59 64 67 72 75 76 79 82 84 88 90 92 96 98 100 
13 33 14 15 16 20 21 25 26 29 30 31 32 34 35 44 46 48 54 58 59 60 61 66 69 70 78 80 83 87 88 92 93 94 95 
14 21 17 18 22 30 37 38 40 44 47 51 56 57 61 62 69 82 85 89 91 99 100 
15 30 18 19 20 23 26 28 29 31 33 36 59 60 61 65 68 72 73 76 80 81 82 83 85 86 87 89 91 94 98 99 
16 21 17 22 25 33 34 38 41 43 46 47 49 61 63 64 65 66 70 75 97 98 99 
17 24 18 27 31 32 33 34 35 37 42 45 46 47 49 53 55 65 70 78 79 81 84 85 91 92 
18 21 20 23 26 28 30 31 32 44 51 53 56 62 70 74 85 87 93 95 96 99 100 
19 25 22 23 27 28 30 31 35 36 50 51 56 65 68 71 72 74 77 78 80 82 91 92 95 99 100 
20 24 22 25 27 30 32 33 39 41 45 47 50 53 59 61 63 64 65 66 70 73 79 83 88 92 
21 26 24 29 32 38 40 41 42 44 49 51 52 54 57 58 68 72 76 78 83 86 87 89 92 94 95 97 
22 25 23 27 28 29 32 39 42 43 45 47 50 51 55 61 62 71 73 74 75 76 82 90 96 99 100 
23 18 25 28 35 37 38 40 44 45 54 55 62 70 75 79 81 82 85 87 
24 19 27 35 51 55 60 61 63 66 74 75 80 81 82 83 85 86 89 93 97 
25 24 26 36 45 52 56 57 58 60 61 63 66 68 75 79 82 86 89 90 92 94 95 96 97 98 
26 20 28 29 36 37 40 52 55 56 63 65 66 67 68 69 70 71 75 83 90 95 
27 18 33 34 40 44 46 49 51 64 65 67 68 69 72 87 89 95 96 99 
28 22 31 33 36 37 41 43 48 51 55 56 57 60 68 76 77 78 80 86 88 90 91 97 
29 25 30 34 39 40 44 48 49 51 54 61 68 69 73 74 75 76 78 79 84 87 89 92 93 94 95 
30 21 31 34 36 39 41 45 49 52 55 56 57 63 64 65 67 75 81 83 85 91 99 
31 19 32 48 52 64 65 66 70 71 72 73 76 77 80 81 84 87 95 96 99 
32 17 39 43 46 47 48 51 55 64 67 68 76 77 80 88 90 91 96 
33 26 34 36 37 38 43 44 45 47 56 57 59 62 69 72 73 75 79 83 84 85 91 93 94 98 99 100 
34 17 36 37 42 44 45 49 54 57 61 64 70 79 83 88 91 96 99 
35 14 37 51 52 54 55 56 63 67 71 80 81 84 90 91 
36 13 48 52 57 58 65 67 71 75 80 81 93 94 99 
37 26 41 44 46 47 49 50 53 54 56 59 66 69 71 72 75 78 79 80 81 86 89 93 95 97 98 100 
38 19 44 46 47 50 55 57 60 61 69 74 75 77 80 81 83 86 90 92 97 
39 19 45 48 49 50 51 52 53 55 61 69 75 76 82 83 88 89 92 94 97 
40 23 42 45 48 49 51 55 56 57 58 62 68 74 75 79 80 81 82 83 84 85 89 92 100 
41 14 52 53 59 64 66 68 69 77 81 85 86 88 92 93 
42 15 44 48 54 55 56 59 64 72 73 77 83 84 92 93 97 
43 14 44 51 54 55 57 62 64 65 67 69 76 78 88 95 
44 12 46 48 49 50 52 55 71 80 85 92 96 97 
45 20 48 49 51 52 55 57 59 61 62 71 73 74 77 78 81 84 85 92 96 97 
46 17 48 49 53 57 59 62 64 71 72 79 81 86 90 93 94 95 100 
47 18 49 53 63 64 65 69 70 73 81 82 84 86 90 91 92 93 95 99 
48 19 49 52 53 58 61 65 70 73 81 83 84 85 86 88 90 92 94 96 97 
49 14 56 70 71 72 73 74 80 81 82 84 85 86 87 89 
50 17 54 62 63 64 65 66 67 71 77 80 83 86 87 90 91 95 98 
51 14 53 55 58 63 68 74 75 78 82 87 89 90 92 96 
52 9 61 63 66 70 71 73 78 82 83 
53 12 56 65 67 71 79 80 85 92 96 97 98 99 
54 14 57 58 60 64 70 72 77 78 79 80 82 94 95 98 
55 13 57 58 64 66 73 74 79 85 86 88 90 92 94 
56 12 57 59 60 64 66 69 87 89 90 92 94 100 
57 9 60 81 89 90 93 94 97 98 100 
58 17 60 63 67 68 70 71 73 75 78 79 80 85 86 88 90 91 95 
59 9 60 64 70 71 73 83 87 97 100 
60 17 65 66 67 71 72 73 76 78 80 82 84 87 88 92 95 96 98 
61 9 62 76 77 84 85 87 93 94 100 
62 10 68 70 74 77 81 82 88 89 96 98 
63 9 65 69 73 76 82 83 89 90 97 
64 9 70 77 78 81 82 83 85 91 100 
65 12 68 71 75 76 80 83 84 85 88 94 97 100 
66 15 67 70 75 77 78 80 81 83 85 86 88 91 94 98 99 
67 12 73 74 77 78 80 82 85 90 92 93 95 96 
68 13 70 71 72 73 74 75 77 79 81 84 87 90 97 
69 5 78 80 88 95 99 
70 8 75 76 78 82 84 92 97 100 
71 9 73 75 79 82 83 90 93 97 99 
72 9 74 75 78 79 81 83 87 92 96 
73 7 79 80 81 83 93 94 97 
74 4 85 90 91 98 
75 4 77 82 88 97 
76 6 81 90 91 94 96 99 
77 10 78 81 85 86 88 90 91 92 98 99 
78 10 80 86 87 91 93 94 95 96 98 100 
79 6 80 83 85 90 97 98 
80 10 86 88 90 91 92 93 95 96 97 99 
81 7 82 83 84 88 89 94 100 
82 5 90 92 93 96 99 
83 6 88 89 91 97 98 99 
84 7 85 86 87 89 93 95 96 
85 4 87 88 92 98 
87 5 88 89 91 96 97 
88 4 90 92 95 96 
89 6 91 92 96 97 98 99 
90 2 92 95 
91 4 93 94 96 97 
93 2 99 100 
94 3 95 98 100 
97 2 98 99 
86 2 90 96
92 95 90 96 86 88 98 99 97 100 93 82 94 91 80 89 83 87 78 69 85 74 79 84 81 73 76 77 67 75 70 64 66 71 72 68 62 61 65 60 57 59 56 49 53 63 47 52 41 58 48 36 46 54 50 55 44 37 38 42 51 35 43 45 34 33 39 32 31 28 30 40 27 24 29 21 26 25 23 22 19 9 20 18 15 17 14 7 16 6 5 13 10 11 3 8 4 12 1 2
    """,
    """
100 99
3 23 8 29 9 22 92 94 37 74 1 100 64 67 2 68 75 23 56 10 12 91 45 15 59 
8 13 10 12 59 68 94 37 2 1 74 45 92 64 23 
88 10 16 5 49 64 40 90 41 85 93 68 
48 47 93 96 15 2 27 32 12 68 14 65 37 5 73 45 8 67 50 43 64 90 56 62 52 49 91 9 71 75 92 57 29 83 22 13 35 74 40 94 61 11 100 6 7 63 3 23 10 
89 4 37 45 22 35 
42 18 59 75 5 83 100 7 93 50 90 32 48 9 10 74 8 19 2 40 
54 44 7 59 91 27 22 56 2 49 5 94 74 90 11 65 100 9 61 73 29 50 15 52 96 63 92 68 6 83 62 37 3 57 10 32 13 8 14 67 40 64 23 75 71 43 
60 13 3 87 23 10 54 73 56 48 82 34 14 100 52 
97 3 19 99 13 
96 20 75 57 23 14 15 100 65 35 68 12 8 2 83 45 49 3 94 1 73 13 
85 13 50 36 54 8 92 40 9 22 37 32 12 60 91 
66 4 29 32 21 15 
65 6 12 100 64 93 71 61 
95 12 29 69 11 6 80 27 72 60 71 41 30 9 
2 3 56 1 29 
62 5 22 8 45 94 59 
15 18 45 94 64 59 23 91 92 56 68 10 37 29 1 12 2 9 74 67 
14 40 29 56 40 13 57 92 49 62 2 94 23 7 67 15 64 27 22 5 12 93 32 37 59 73 75 71 3 6 45 74 1 91 35 10 100 68 90 61 9 8 
30 34 91 82 94 7 45 90 6 83 68 54 35 61 92 100 11 49 9 56 52 14 65 40 23 8 64 20 2 1 5 84 51 75 48 89 
35 32 57 75 91 92 9 59 3 62 37 10 29 74 64 67 2 68 90 49 12 100 7 23 1 27 56 94 61 8 15 45 22 32 
59 3 29 1 56 
49 18 1 74 12 94 100 2 59 92 67 29 15 22 75 45 23 10 64 9 
74 11 2 12 29 23 56 1 59 9 67 94 64 
25 31 27 2 33 99 13 48 93 19 90 47 71 24 49 60 92 6 57 94 96 50 97 31 5 29 52 16 72 100 65 1 51 
47 22 63 49 65 29 54 20 36 71 74 7 35 26 11 83 64 31 93 92 42 39 60 94 
33 4 50 62 49 75 
31 6 5 63 27 61 43 67 
21 14 91 82 48 97 87 32 74 68 2 8 94 51 83 26 
70 50 44 88 33 51 23 16 75 94 90 3 46 14 98 63 55 91 35 32 93 41 43 74 68 54 69 50 72 85 27 67 26 56 80 9 20 83 59 48 25 57 34 40 66 13 79 64 96 42 45 53 
40 26 27 10 1 15 74 92 59 8 91 22 45 94 12 57 3 9 90 62 61 7 75 23 67 32 29 100 
10 11 12 64 1 94 29 67 59 56 9 23 2 
39 22 7 45 92 32 98 14 54 27 23 1 6 75 3 96 99 57 60 71 15 83 100 50 
92 11 64 12 9 23 94 67 59 56 29 2 1 
7 11 2 64 91 23 59 10 22 68 100 9 29 
6 6 73 40 12 37 22 32 
94 7 56 9 64 2 29 59 1 
98 8 31 43 56 45 10 50 87 8 
71 36 12 94 49 10 62 57 91 3 35 45 23 59 22 29 15 8 75 2 1 27 68 93 7 37 32 56 100 73 92 67 90 64 61 74 40 9 
50 14 93 3 9 64 62 22 32 61 56 8 13 45 100 6 
19 13 83 1 23 43 92 57 10 56 14 15 64 62 67 
93 20 68 32 74 90 59 92 2 10 45 8 15 61 57 9 12 3 22 49 94 1 
55 20 19 54 18 22 61 23 10 50 69 51 45 34 90 53 94 6 93 24 75 33 
17 36 1 59 50 28 42 6 69 18 13 24 57 86 92 65 72 16 23 36 21 2 85 73 41 83 90 47 9 60 44 67 54 40 87 91 11 45 
12 7 1 2 29 9 64 59 56 
63 28 68 94 8 5 65 93 61 22 35 1 23 100 67 13 7 49 59 32 6 40 62 12 9 57 45 73 71 75 
43 21 62 5 64 100 71 23 90 68 13 67 9 45 15 2 91 92 61 22 6 3 7 
22 9 29 56 23 37 9 10 64 92 45 
64 1 1 
34 19 43 11 91 6 23 90 49 14 22 10 13 37 52 3 9 68 94 2 83 
90 23 37 2 100 22 1 64 12 15 59 56 8 23 45 91 9 68 75 10 74 92 29 94 67 
51 7 13 59 83 37 96 49 68 
99 33 43 67 3 87 41 74 48 94 96 29 100 14 83 51 82 61 45 31 15 71 27 35 52 91 54 89 6 73 50 2 7 63 65 
23 7 2 29 59 64 9 56 1 
13 6 75 8 9 49 90 27 
37 11 64 1 29 59 94 67 12 23 2 9 56 
38 21 48 91 81 25 50 23 27 88 40 28 32 93 15 63 97 86 54 59 11 41 55 
36 21 91 71 65 11 67 49 2 73 5 50 7 27 35 100 37 56 8 59 14 57 23 
45 11 12 94 64 9 59 56 23 29 2 67 1 
9 6 1 29 2 59 56 64 
52 44 45 32 10 6 94 43 3 14 49 73 12 93 35 23 68 92 56 37 40 7 8 13 1 62 2 100 59 22 74 90 67 29 71 15 27 75 91 61 65 64 9 83 57 5 
28 11 57 10 27 100 32 82 93 94 54 52 99 
91 11 2 56 29 9 59 1 23 64 67 12 94 
61 23 59 9 64 91 56 92 29 12 10 74 68 100 67 22 45 23 75 1 15 8 37 94 2 
86 16 74 12 52 40 93 98 26 8 62 14 71 45 100 32 16 90 
41 16 35 57 5 13 94 43 51 10 37 40 9 92 7 48 65 64 
83 12 71 6 67 61 90 68 22 27 29 35 3 59 
78 12 7 98 22 42 11 47 84 50 24 17 73 93 
68 11 59 29 56 1 12 2 67 64 23 94 9 
87 32 96 3 43 83 48 27 49 14 57 73 93 64 52 67 40 100 7 1 74 59 45 37 9 13 10 8 34 12 2 91 94 36 
4 38 99 45 6 64 42 88 79 74 19 34 100 12 98 67 75 21 81 24 62 56 3 32 86 55 65 50 13 5 18 87 26 92 11 83 44 93 7 49 
53 1 19 
57 23 9 12 29 94 92 23 68 2 45 22 10 75 64 15 8 74 100 91 67 59 56 37 1 
73 18 29 37 45 74 49 57 10 90 62 3 1 2 8 15 61 7 67 59 
11 8 32 75 15 35 13 68 59 94 
75 18 23 91 67 56 68 37 64 1 94 12 59 2 92 10 45 29 74 9 
56 1 1 
69 34 23 43 45 14 54 75 93 73 11 59 7 62 2 5 26 12 67 94 40 52 32 35 22 65 3 13 36 68 83 6 63 90 31 10 
32 22 59 2 15 68 100 10 29 23 75 45 37 12 22 74 56 64 1 94 91 8 67 9 
20 40 87 94 74 41 92 31 91 52 68 56 64 51 27 13 9 50 90 35 34 29 48 12 7 65 6 45 75 62 10 15 22 8 100 26 83 49 14 37 73 5 
82 6 15 35 59 74 6 65 
100 18 56 64 91 12 2 68 94 29 23 59 67 9 45 1 92 74 37 10 
80 4 99 16 12 37 
84 1 23 
46 5 19 82 42 52 69 
29 1 1 
81 46 92 56 10 98 35 49 29 30 88 86 93 31 2 22 72 32 23 63 5 82 12 96 46 39 52 16 89 74 47 28 62 13 33 43 87 15 80 37 41 36 68 7 65 71 90 54 
79 43 32 29 63 62 87 24 9 45 3 22 89 52 57 86 34 82 47 48 41 90 39 68 74 59 60 13 14 53 26 67 51 37 46 97 72 7 35 56 21 16 11 49 75 
58 36 47 84 80 26 40 68 50 91 52 15 1 75 56 66 92 100 29 63 27 83 81 42 96 7 30 90 85 35 13 79 51 24 32 43 6 45 
77 40 26 80 94 61 18 9 25 62 41 33 12 37 30 36 20 51 52 29 45 99 54 56 7 72 66 27 91 40 21 86 97 35 19 55 79 53 85 73 22 82 
5 36 91 35 8 9 73 59 90 74 2 94 93 7 92 49 37 12 1 67 100 62 10 57 61 22 23 29 27 3 32 40 68 15 75 64 45 56 
16 49 83 74 49 23 60 6 29 31 62 71 94 100 43 57 93 27 26 5 13 69 89 61 91 73 84 1 14 3 15 90 92 87 11 68 82 98 54 10 64 8 56 63 20 36 96 34 12 40 48 
72 35 82 86 44 23 50 91 22 97 98 31 37 59 92 84 52 40 20 93 9 39 62 43 53 63 24 16 96 89 64 41 51 18 60 19 99 
67 7 2 29 1 9 64 59 56 
26 47 57 71 11 90 65 93 64 52 9 62 49 83 7 63 10 50 22 35 3 1 73 56 12 13 32 94 8 45 100 92 43 75 15 91 74 6 40 5 29 2 96 23 68 61 14 67 59 
24 21 56 23 48 11 57 69 49 50 22 42 67 2 35 28 93 21 45 74 34 90 3 
44 31 93 2 50 12 92 7 42 8 27 85 39 34 100 63 68 84 16 32 49 37 13 43 94 67 28 22 15 96 1 26 5 
27 6 8 45 100 1 67 68 
76 36 57 75 46 98 79 80 34 29 12 32 26 89 69 71 65 64 21 49 50 20 24 6 60 56 35 61 72 54 81 53 17 39 90 19 10 13 
18 13 64 22 47 35 48 28 37 75 52 29 40 57 92
1 29 56 2 59 64 9 12 23 67 84 94 10 37 45 68 74 91 92 8 15 22 62 75 100 3 7 27 32 49 57 61 90 13 35 11 40 73 6 89 93 5 50 33 71 14 43 65 36 63 31 82 83 19 52 34 53 96 26 48 42 51 41 54 69 46 87 20 30 60 85 98 16 86 88 99 28 39 44 47 18 80 97 21 24 55 66 72 17 25 78 79 70 77 81 4 38 58 76 95
    """,
    """
    1 0
    1
    """,
    """
    4 1
    1 3 4 2
    2 3 4 1
    """
    ]
    time_limit = 0.5
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