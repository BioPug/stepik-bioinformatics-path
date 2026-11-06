# Сводная таблица чемпионата по результатам футбольных матчей.
# Программа читает протокол игр со стандартного входа, считает очки
# (победа — 3, ничья — 1, поражение — 0) и печатает статистику команд.

d = {}
x = int(input())
for i in range(x):
    info = input()
    team1,score1,team2,score2 = info.split(';')
    score1 = int(score1)
    score2 = int(score2)
    if team1 not in d:
        d[team1] = [0,0,0,0,0]
    if team2 not in d:
        d[team2] = [0,0,0,0,0]
    d[team1][0]+= 1
    d[team2][0]+= 1
    if score1 > score2:
        d[team1][1]+= 1
        d[team1][4]+= 3
        d[team2][3]+= 1
    elif score1 < score2:
        d[team2][1]+= 1
        d[team2][4]+= 3
        d[team1][3]+= 1
    elif score1 == score2:
        d[team1][2]+= 1
        d[team2][2]+= 1
        d[team1][4]+= 1
        d[team2][4]+= 1
for k,v in d.items():
    print(k+': ',v[0],v[1],v[2],v[3],v[4])





