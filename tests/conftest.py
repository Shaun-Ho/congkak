import pytest
import numpy as np
from congkak.containers import BoardState, PlayerNumber, Player

@pytest.fixture
def board_state_example()->BoardState:
    return BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1
        ),
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1
        ),
        side_one=np.array([0,0,0,0,0,0,1]),
        side_two=np.array([0,0,0,0,0,0,1])
    )


@pytest.fixture
def extra_turn_board_state_example()->BoardState:
    return BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1
        ),
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1
        ),
        side_one=np.array([0,0,0,0,0,0,1]),
        side_two=np.array([0,0,0,0,0,0,0])
    )


@pytest.fixture
def steal_board_state_example()->BoardState:
    return BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1
        ),
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1
        ),
        side_one=np.array([0,0,0,0,0,0,0]),
        side_two=np.array([0,0,0,0,0,0,0])
    )


@pytest.fixture
def lose_go_board_state_example()->BoardState:
    return BoardState(
        active=True,
        turn=PlayerNumber.ONE,
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1
        ),
        player_one=Player(
            number=PlayerNumber.ONE,
            score=1
        ),
        side_one=np.array([0,0,0,0,0,0,0]),
        side_two=np.array([0,0,0,0,0,0,0])
    )