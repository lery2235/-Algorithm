
def soultion(progresses, speeds):
    answer = []
    while progresses:
        release = 0
        while progresses and progresses[0] >= 100:
            release+=1
            progresses.pop(0)
            speeds.pop(0)
        progresses = [p+s for p, s in zip(progresses, speeds)]

        if release < 0:
            answer.append(release)

        return answer