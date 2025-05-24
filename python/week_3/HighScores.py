class HighScores:
    def __init__(self, scores):
        self.scores = list(scores)

    def latest(self):
        if self.scores:
            return self.scores[-1]

    def best(self):
        if self.scores:
            return max(self.scores)


    def personal_top_three(self):
        if len(self.scores):
            return sorted(self.scores, reverse=True)[:3]



if __name__ == '__main__':
    highScope = HighScores([10, 70])
    print(highScope.personal_top_three())