C= int(input())

for i in range(C):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:]) / nums[0]
    count = 0
    for score in nums[1:]:
        if score > avg:
            count += 1
    rate= count/nums[0] * 100
    print(f'{rate:.3f}%')
