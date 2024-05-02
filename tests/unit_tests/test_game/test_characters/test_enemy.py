import pytest

from source.game.characters import EnemyStub


@pytest.mark.skip(reason="Test not implemented yet")
def test_generation():
    PES = EnemyStub()
    assert PES.name == "Pes", "Test not implemented yet"
    assert PES.description == "Nejlepsi priatel cloveka", "Test not implemented yet"
    assert PES.experience_drop == 1, "Test not implemented yet"
