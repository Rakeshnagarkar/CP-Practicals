Practical 7
Bridge
 n people wish to cross a bridge at night. A group of at most two people may cross at any time, and each group must have a flashlight. Only one flashlight is available among the n people, so some sort of shuttle arrangement must be arranged in order to return the flashlight so that more people may cross.
 Each person has a different crossing speed; the speed of a group is determined by the speed of the slower member. Your job is to determine a strategy that gets all n people across the bridge in the minimum time.
 Input 
The input begins with a single positive integer on a line by itself indicating the number of the cases following, each of them as described below. This line is followed by a blank line, and there is also a blank line between two consecutive inputs.
 The first line of input contains n, followed by n lines giving the crossing times for each of the people. There are not more than 1000 people and nobody takes more than 100 seconds to cross the bridge.
 Output
 For each test case, the output must follow the description below. The outputs of two consecutive cases will be separated by a blank line. 
The first line of output must contain the total number of seconds required for all n people to cross the bridge. The following lines give a strategy for achieving this time. Each line contains either one or two integers, indicating which person or people form the next group to cross. (Each person is indicated by the crossing time specified in the input. Although many people may have the same crossing time the ambiguity is of no consequence.) 
Note that the crossings alternate directions, as it is necessary to return the flashlight so that more may cross. If more than one strategy yields the minimal time, any one will do. 
Sample Input
 1

 4
 1
 2
 5
10
 Sample Output 
17 
1 2
 1
 5 10
 2 
1 2
Program:




include <iostream>
include <cstdio>
include <algorithm>
include <cstring>
include <string>
include <cctype>
include <stack>
include <queue>
include <list>
include <vector>
include <map>
include <sstream>
include <cmath>
include <bitset>
include <utility>
include <set>
include <numeric>
include <time.h>
include <fstream>
define INT_MAX 2147483647
define INT_MIN -2147483648
define pi acos(-1.0)
define E 2.71828182845904523536
using namespace std;
int main()
{
    int N,n;
    cin >> N;
    for (int i=0; i<N; i++)
    {
        deque<int> LeftSide, RightSide;
        cin >> n;
        int T;
        for (int i=0; i<n; i++)
            {
                cin >> T;
                LeftSide.push_back(T);
            }
        sort(LeftSide.begin(), LeftSide.end());
        int TotalTime = 0;
        stringstream fout;
        while(1)
        {
            int A = LeftSide[0];
            if (LeftSide.size() == 1) {fout << A; TotalTime += A; break;}
            int B = LeftSide[1];
            if (LeftSide.size() == 2)
            {
                fout << A << " " << B; TotalTime += B;break;
            }
            if (LeftSide.size() == 3)
            {
                fout << A << " " <<LeftSide[2] << endl << A << endl << A << " " <<  B ;
                TotalTime += B + A +  LeftSide[2];
                break;
            }
            int Y, Z;
            Z = LeftSide.back();
            LeftSide.pop_back();
            Y = LeftSide.back();
            LeftSide.pop_back();
            if (A + Y < 2*B)
            {
                fout << A << " " << Z << endl << A << endl << A << " " << Y << endl << A << endl;
                TotalTime += Z + 2*A + Y;
            }
            else
            {
                fout << A << " " << B << endl << A << endl << Y << " " << Z << endl << B << endl;
                TotalTime += 2*B + A + Z;
            }
        }
 
        cout<< TotalTime << endl << fout.str() << endl;
 
        if (i != N-1) cout << endl ;
    }
    return 0;
}








Input:
 1

 4
 1
 2
 5
10
Output:
17 
1 2
 1
 5 10
 2 
1 2

