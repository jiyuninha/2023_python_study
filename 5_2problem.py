def solution(strings, n):
    answer = []
    answer = sorted(sorted(strings),key=lambda x : x[n])

    return answer

strings = ["sun", "car", "bed"]
n = 1
print(solution(strings,n))