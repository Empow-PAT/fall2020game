from players import PlayerWaving, PlayerStrobing

def test_waving_player_init():
    player = PlayerWaving()
    assert player.image != None


def test_strobing_player_init():
    player = PlayerStrobing()
    assert player.image != None

