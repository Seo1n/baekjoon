import sys
# https://jih3508.tistory.com/75 참고


def rectangle(l, r):
    global histogram
    # l,r 이 같은 값을 가리킬 경우 즉, 한개의 히스토그램만 남았을 경우
    # 그 직사각형의 높이가 넓이이다.
    if l == r:
        return histogram[l]
    mid = (l+r)//2  # 현재 가운데 원소
    # 왼쪽 부분과 오른쪽 부분을 분할하여 직사각형의 넓이를 구하면서 큰 값을 area에 저장
    area = max(rectangle(l, mid), rectangle(mid+1, r))
    new_left = mid  # 왼쪽에서 시작할 시작점 -> l에 맞닿을 때까지 -1
    new_right = mid+1  # 오른쪽에서 시작할 시작점 -> r에 맞닿을 때까지 +1
    # 붙어있는 new_left와 new_right 중 낮은 높이 선택 -> 직사각형 연결
    height = min(histogram[new_left], histogram[new_right])
    '''
    1. 현재 경계부분이 아닌 왼쪽 또는 오른쪽 부분에서 구한 넓이가 최대인 경우 (코드 10번 줄 참고)
    2. 현재 경계를 기준으로 new_left와 new_right로 만든 직사각형의 넓이가 최대인 경우
    3. 경계의 왼쪽에서 너비 1의 직사각형이 최대인 경우
    4. 경계의 오른쪽에서 너비 1의 직사각형이 최대인 경우
    '''
    area = max(area, height*2, histogram[new_left], histogram[new_right])
    while l < new_left or new_right < r:  # 범위 내일 경우
        # 오른쪽 부분이 더 클 경우
        if new_right < r and (new_left <= l or histogram[new_left-1] < histogram[new_right+1]):
            new_right += 1
            height = min(height, histogram[new_right])
        else:
            new_left -= 1
            height = min(height, histogram[new_left])
        # new_right - new_left + 1 = width  즉, 직사각형의 너비
        area = max(area, height*(new_right-new_left+1))
    return area


while True:
    n, *histogram = map(int, sys.stdin.readline().split())
    if n == 0:
        break
    print(rectangle(0, n-1))
