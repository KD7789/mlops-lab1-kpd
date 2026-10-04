import pytest
from src import calculator


def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5, 0) == 5
    assert calculator.fun1(-1, 1) == 0
    assert calculator.fun1(-1, -1) == -2


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5, 0) == 5
    assert calculator.fun2(-1, 1) == -2
    assert calculator.fun2(-1, -1) == 0


def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5, 0) == 0
    assert calculator.fun3(-1, 1) == -1
    assert calculator.fun3(-1, -1) == 1


def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5, 0, -1) == 4
    assert calculator.fun4(-1, -1, -1) == -3
    assert calculator.fun4(-1, -1, 100) == 98


def test_fun4_invalid_input():
    with pytest.raises(ValueError):
        calculator.fun4(1, 2, "3")
    with pytest.raises(ValueError):
        calculator.fun4(1, None, 3)


def test_divide():
    assert calculator.divide(10, 4) == 2.5
    assert calculator.divide(-6, 3) == -2
    assert calculator.divide(0, 5) == 0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(5, 0)


def test_divide_invalid_input():
    with pytest.raises(ValueError):
        calculator.divide("a", 2)
    with pytest.raises(ValueError):
        calculator.divide(True, 2)


def test_power():
    assert calculator.power(2, 3) == 8
    assert calculator.power(5, 0) == 1
    assert calculator.power(2, -1) == 0.5
    assert calculator.power(4, 0.5) == 2.0


def test_power_negative_base_fractional_exponent():
    with pytest.raises(ValueError):
        calculator.power(-4, 0.5)


def test_average():
    assert calculator.average(1, 2, 3) == 2.0
    assert calculator.average(5) == 5.0
    assert calculator.average(-1, 1) == 0.0


def test_average_no_input():
    with pytest.raises(ValueError):
        calculator.average()


def test_modulo():
    assert calculator.modulo(10, 3) == 1
    assert calculator.modulo(9, 3) == 0
    assert calculator.modulo(-7, 3) == 2


def test_modulo_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.modulo(5, 0)


def test_sqrt():
    assert calculator.sqrt(16) == 4.0
    assert calculator.sqrt(0) == 0.0
    assert calculator.sqrt(2) == pytest.approx(1.41421356, rel=1e-6)


def test_sqrt_negative():
    with pytest.raises(ValueError):
        calculator.sqrt(-1)


def test_sqrt_invalid_input():
    with pytest.raises(ValueError):
        calculator.sqrt("16")    