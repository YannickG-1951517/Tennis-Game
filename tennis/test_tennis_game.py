from tennis_game import TennisGame


def test_initial_score_is_love_love():
    game = TennisGame("p1", "p2")
    assert game.get_score() == "love - love"


def test_player1_scores_once():
    game = TennisGame("p1", "p2")
    game.player1_scores()
    assert game.get_score() == "15 - love"


def test_player1_scores_twice():
    game = TennisGame("p1", "p2")
    game.player1_scores()
    game.player1_scores()
    assert game.get_score() == "30 - love"


def test_player1_scores_three_times():
    game = TennisGame("p1", "p2")
    game.player1_scores()
    game.player1_scores()
    game.player1_scores()
    assert game.get_score() == "40 - love"


def test_player1_wins_without_deuce():
    game = TennisGame("p1", "p2")

    for _ in range(4):
        game.player1_scores()

    assert game.get_score() == "Player 1 wins"


def test_player2_scores_once():
    game = TennisGame("p1", "p2")
    game.player2_scores()
    assert game.get_score() == "love - 15"


def test_player2_wins_without_deuce():
    game = TennisGame("Player 1", "Player 2")

    for _ in range(4):
        game.player2_scores()

    assert game.get_score() == "Player 2 wins"


def test_deuce_at_40_40():
    game = TennisGame("p1", "p2")

    for _ in range(3):
        game.player1_scores()
        game.player2_scores()

    assert game.get_score() == "Deuce"


def test_player1_leads_after_deuce():
    game = TennisGame("p1", "p2")

    for _ in range(3):
        game.player1_scores()
        game.player2_scores()

    game.player1_scores()
    assert game.get_score() == "Advantage player 1"


def test_player2_leads_after_deuce():
    game = TennisGame("p1", "p2")

    for _ in range(3):
        game.player1_scores()
        game.player2_scores()

    game.player2_scores()
    assert game.get_score() == "Advantage player 2"


def test_returns_to_deuce_after_loosing_advantage():
    game = TennisGame("p1", "p2")

    for _ in range(3):
        game.player1_scores()
        game.player2_scores()

    game.player1_scores()
    game.player2_scores()
    assert game.get_score() == "Deuce"


def test_player1_wins_after_advantage():
    game = TennisGame("p1", "p2")

    for _ in range(3):
        game.player1_scores()
        game.player2_scores()

    game.player1_scores()
    game.player1_scores()
    assert game.get_score() == "Player 1 wins"

def test_player2_wins_after_advantage():
    game = TennisGame("p1", "p2")

    for _ in range(3):
        game.player1_scores()
        game.player2_scores()

    game.player2_scores()
    game.player2_scores()
    assert game.get_score() == "Player 2 wins"


# edge case
def test_score_does_not_change_after_game_won():
    game = TennisGame("p1", "p2")

    for _ in range(4):
        game.player1_scores()
    
    # extra point after game won
    game.player1_scores()
    assert game.get_score() == "Player 1 wins"
