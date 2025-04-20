class TennisGame:
    _SCORES = ["love", "15", "30", "40"]

    def __init__(self, player1, player2):
        self.player1_points = 0
        self.player2_points = 0
        self.player1_name = player1
        self.player2_name = player2

    def __str__(self):
        return (
            f"{self.player1_name}: {self.get_player_score(self.player1_points)} | "
            f"{self.player2_name}: {self.get_player_score(self.player2_points)}"
        )

    def get_score(self):
        if self.player1_points >= 4 and self.player1_points - self.player2_points >= 2:
            return "Player 1 wins"
        if self.player2_points >= 4 and self.player2_points - self.player1_points >= 2:
            return "Player 2 wins"

        if self.player1_points >= 3 and self.player2_points >= 3:
            if self.player1_points == self.player2_points:
                return "Deuce"
            elif self.player1_points - self.player2_points == 1:
                return "Advantage player 1"
            elif self.player2_points - self.player1_points == 1:
                return "Advantage player 2"

        return (
            f"{self._SCORES[self.player1_points]} - {self._SCORES[self.player2_points]}"
        )

    def player1_scores(self):
        if not self.is_game_over():
            self.player1_points += 1

    def player2_scores(self):
        if not self.is_game_over():
            self.player2_points += 1

    def is_game_over(self):
        return (self.player1_points >= 4 and self.player1_points - self.player2_points >= 2) or \
            (self.player2_points >= 4 and self.player2_points - self.player1_points >= 2)
