import pytest 
import robot

@pytest.fixture
def mon_robot():
    return robot.Robot()

@pytest.mark.parametrize("X, Y, expG, expD",  [
    (0, 100, 100, 100),   # avance droit
    (0, -100, -100, -100), # recule droit
    (100, 100, 100, 0), # tourne droite à fond
    (50, 100, 100, 50), # moitié droite à fond
    (-100, 100, 0, 100), # tourne gauche à fond
    (-100, 50, 0, 50), # tourne gauche à moitie de la vitesse
    (100, 50, 50, 0), # tourne droite à moitie de la vitesse
    (-100, -100, 0, -100), # AR Gauche à fond
    (100, -100, -100, 0), # AR droit à fond
])

def test_vector_to_differential(mon_robot, X, Y, expG, expD):
    g, d = mon_robot.vector_to_differential(X, Y)
    assert d == expD and g == expG
    