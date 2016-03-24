

// A hello world program in C++

#include<iostream>
#include <unordered_map>
using namespace std;

int shortest_seq(int n, int x, int y, int u, int d)
{
	unordered_map <int, int> edge;	
	unordered_map <int, int> depth;	
	edge[0] = x;
	depth[x] = 0;

	int moves [2] = {u,-1*d};

	int front = -1;
	int back = 0;

	for ( ;; ) {
		front += 1;
		int floor = edge[front];
		if (floor == y) { return depth[floor]; }

		for(int i = 0; i < 2; ++i) {
			int move = moves[i];
			int floor_ = floor + move;	
			// int &stored_val = depth[floor_];
			// if (stored_val == 0 && floor_ <= n && floor >= 1) {
			if (depth.find(floor_) == depth.end() && floor_ <= n && floor >= 1) {
				depth[floor_] = depth[floor] + 1;
				back += 1;
				edge[back] = floor_;
			}
		}

		if (front == back) { return 0; }
	}
}

int main()
{
	cout << shortest_seq(10,1,10,2,3);
	cout << "\n";

	cout << shortest_seq(5000000, 1, 2345, 12344,43111);
	cout << "\n";
}
