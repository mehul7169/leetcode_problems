from collections import defaultdict
class Leaderboard:

    def __init__(self):
        self.pl = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.pl[playerId] += score

    def top(self, K: int) -> int:
        pls = list(self.pl.values())
        pls.sort()
        print(pls)
        return sum(pls[-K:])

    def reset(self, playerId: int) -> None:
        self.pl[playerId] = 0