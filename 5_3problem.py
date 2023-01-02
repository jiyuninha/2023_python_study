def solution(n, wires):
    answer = -1
    # 각 송전탑 만들기
    towers = []
    for trans_tower in range(1, n+1):
        towers.append([trans_tower,0])

    row = len(wires)
    col = len(wires[0])

    # 각 송전탑에 연결되는 전선
    for i in range(row):
        # wires의 세로만큼 반복
        for j in range(col):
            # wires의 가로만큼 반복
            if j == 0:
                towers[i][j]