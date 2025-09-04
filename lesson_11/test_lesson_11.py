import pytest
import sys
from pathlib import Path

# Додавання кореневої директорії проєкту до sys.path
root_dir = Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))
from lesson_10 import lesson_10


def test_add_function():
    actual_result = 1 + 1
    expectd_result = 2
    assert actual_result == expectd_result

@pytest.mark.smoke
def test_add_function_wrong():
    actual_result = 1 + 1 + 1
    expectd_result = 3
    assert actual_result == expectd_result


def test_check_age():
    actual_result = lesson_10.check_age(15)
    expectd_result = 15
    assert actual_result == expectd_result
    with pytest.raises(ValueError):
        lesson_10.check_age(-1)


def test_input_limit():
    """
    Tra-ta-ta description paste here
    """
    limit = 100_000
    actual_result = lesson_10.get_money(limit)
    assert actual_result == True


def test_input_limit_over():
    limit = 100_000
    with pytest.raises(lesson_10.TooLargeValueError):
        lesson_10.get_money(limit + 1)

@pytest.mark.smoke
def test_car_class():
    actual_car = lesson_10.Car("ZAZ", "Dawoo")
    assert actual_car.brand == "ZAZ"
    assert actual_car.model == "Dawoo"
    assert actual_car.get_engine() == False, "Expected engine is off (False)"
    actual_car.start_engine()
    assert actual_car.get_engine()

@pytest.mark.xfail
def tc_just_xfail():
    assert False

@pytest.mark.skip(reason="Причина пропуску тесту")
def tc_just_skip():
    pass


def today_is_wensday():
    return True


@pytest.mark.skipif(today_is_wensday(), reason="Причина пропуску тесту: сьогодні середа")
def test_example():
    assert True