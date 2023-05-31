# https://www.acmicpc.net/problem/2164
# 백준-2164-카드2

# 풀이1
from collections import deque

n = int(input())
cards = deque([num for num in range(1, n+1)])

while len(cards) > 1:
    cards.popleft()
    cards.rotate(-1)

print(cards[0])
'''
<풀이1> 
가장 직관적인 풀이법.
카드가 하나만 남을 때까지 1) 제일 위의 카드를 버린다, 2) 그 다음 가장 위로 올라온 카드는 마지막으로 보낸다. 두가지를 반복.

카드 두개중 하나는 버려지므로 N개의 카드는 곧 N/2개가 되고 다시 N/4개가 된다. 즉 첫 항이 N이고 공비가 1/2인 등비수열의 합이라고 볼 수 있다.
N이 무한대로 갈 수록 해당 값은 2N과 같아지므로 충분히 큰 수 N에 대해서 2N이라고 할 수 있고 따라서 시간복잡도는 O(N)이다.

최악의 경우 1,000,000번의 가까운 연산을 하게 되는데 시간 제한에 걸리지 않을 만한 횟수이므로 이 방식으로 문제를 풀 수 있다.
'''


# 풀이2
n = int(input())

i = 0
while 2**i < n:
    i += 1

print(n if n == 2**i else 2*n-2**i)
'''
수학적인 규칙을 찾아서 문제를 푼 것. N이 2의 제곱 꼴인 수라면 답은 바로 N이 된다. 첫 시도에서 짝수번째의 수는 모두 살아남고, 그 다음도 마찬가지이기 때문.
2의 제곱인 수는 매번 짝수이므로 끝까지 살아남게 된다.

만약 N이 2의 제곱꼴인 수가 아니라면 N에서 N보다 작은 2의 제곱수 중 가장 큰 수를 뺀 값에 2를 곱한 값이 답이 된다. 정리하자면 2N - 2^i의 값이다.

시간복잡도는 초기에 i의 값을 계산하는 부분만 보면 된다. 2씩 곱해가며 2^i가 n보다 작은 조건 하에서 반복하면 되는데 이는 곧 logN과 같다. 즉 O(logN)이 된다.

-> 시간복잡도 면에서 가장 효율적인 방식입니다. 2N-2^i를 도출해내는 과정이 어려운데, 여러 개를 나열하고 규칙성을 찾아 추론할 수 있긴 합니다만 논리적 사고 전개 후에
도출된 값이 아니라 찝찝함이 남아있어 그 부분 더 고민해서 보충해놓도록 하겠습니다.
'''

