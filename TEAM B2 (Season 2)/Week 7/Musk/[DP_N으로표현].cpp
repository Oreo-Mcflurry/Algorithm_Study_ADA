#include <string>
#include <vector>
#include <set>
#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;
// Solution. 
// 1~8개로 만들수 있는 숫자들 다 저장해놓고 조합?

// 기존은 3개면 5 55 , 55 5로 사칙연산만 했었는데 기타 사항 고려하기가 힘듬.
// 생각해보니 DP문제여서 계산해놓은거 가져와서 다시 돌림

int powCustom(int N, int cnt) {
    int n = 0;
    while(cnt--) {
        n += N * pow(10, cnt);
    }
    return n;
}

int solution(int N, int number) {
    vector<set<int>> dp(8);
    for(int i=0;i<8;i++) {
        int cnt = i+1;
        int n = 0;
        n = powCustom(N, cnt);
        dp[i].insert(n);
    }
    
    for(int i=0;i<8;i++) {
        for(int j=0;j<i;j++) {
            // int a = powCustom(N, j);
            // int b = powCustom(N, i+1-j);
            for(auto &a: dp[j]) {
                for(auto &b: dp[i-j-1]) {
                    dp[i].insert(a+b);
                    dp[i].insert(a*b);
                    dp[i].insert(a-b);
                    if (b != 0) { dp[i].insert(a/b); }
                }
            }
        }
        // i=0이 그냥 5여서 1부터 시작하니 5,5,1케이스를 못찾는 경우가 생김
        if(dp[i].find(number) != dp[i].end()) { return i+1; }
    }
    return -1;
}

/*
5
55
555
5555
55555
555555
5555555
55555555
vector<string> dp2;
*/