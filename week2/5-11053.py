import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):
        if dp[i] > dp[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))


# def binary(arr, n):
#     left = 0
#     right = len(arr)
#     if n > arr[-1]:
#         return len(arr)
#     elif n < arr[0]:
#         return 0
#     mid = (left +right )//2
#     while left <= right:
#         if arr[mid] > n:
#             right = mid-1
#         elif arr[mid] < n:
#             left = mid+1
#         else:
#             return mid
#         mid = (left + right )//2
#     return mid + 1


# n = int(input())
# a_list = list(map(int, input().split()))

# dp = [0]
# l = [0]

# for a in a_list:
#     idx = binary(l, a)
#     if idx == len(l):
#        l.append(a)
#     else:
#         l[idx] = a
#     dp.append(idx)
# print(max(dp))
