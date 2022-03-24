def solution(genres, plays):

    counts = dict()
    songs = dict()
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre not in counts:
            counts[genre] = 0
        counts[genre] += play

        if genre not in songs:
            songs[genre] = []
        songs[genre].append((i, play))

    answer = []
    _sorted = sorted(counts.items(), key=lambda x:-x[1])
    for genre, count in _sorted:
        for i, c in sorted(songs[genre], key=lambda x:-x[1])[:2]:
            answer.append(i)
    return answer

if __name__ == "__main__":
    genres = ["classic", "pop", "classic", "classic", "pop"]
    plays = [500, 600, 150, 800, 2500]
    print(solution(genres, plays))