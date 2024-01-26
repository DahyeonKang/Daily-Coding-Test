## 문제 : 노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
# 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록


def solution(genres, plays):
    answer = []
    sumdict = {}
    dict = {}

    for i in range(len(genres)):
        sumdict[genres[i]] = sumdict.get(genres[i], 0) + plays[i]
        dict[genres[i]] = dict.get(genres[i], []) + [(plays[i], i)]
    sorted_dict = sorted(sumdict.items(), key=lambda x: x[1], reverse=True)
    print(sorted_dict, dict)

    for i in sorted_dict:
        genre = i[0]
        dict[genre].sort(key=lambda x: x[0], reverse=True)
        p = dict[genre]
        if len(p) > 1:
            if p[0][0] == p[1][0]:
                if p[0][1] < p[1][1]:
                    answer.extend([p[0][1], p[1][1]])
                else:
                    answer.extend([p[1][1], p[0][1]])
            else:
                answer.extend([p[0][1], p[1][1]])
        else:
            answer.append(p[0][1])

    return answer



# 짧은 풀이
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer