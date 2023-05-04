import sys
input = sys.stdin.readline

gun, animal, gun_range = (map(int, input().split()))

lst = list(map(int, input().split()))
lst.sort()
ans = 0

for i in range(animal):
    x, y = (map(int, input().split()))
    if y > gun_range:
        continue
    else:
        gap = gun_range - y
        min = x - gap
        max = x + gap

        left, right = 0, gun-1

        while left <= right:
            mid = (left + right) // 2
            if min <= lst[mid] <= max:
                ans += 1
                break
            elif lst[mid] < min:
                left = mid + 1
            elif lst[mid] > max:
                right = mid - 1


print(ans)
