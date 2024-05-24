import pytest
from calculator.calculator import Calculator


class TestCalculator: 
    def test_add(self):
        # arrange
        a = 5
        b = 5
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 10
        assert result == expected

    def test_subtract(self):
        # arrange
        a = 2
        b = 1
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 1
        assert result == expected

    def test_multiply(self):
        # arrange
        a = 4
        b = 2
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 8
        assert result == expected


    def test_divide(self):
        # arrange
        a = 8
        b = 2
        cal = Calculator()

        # act
        result = cal.divide(a, b)

        # assert
        expected = 4  # floating-point division
        assert result == expected

    def test_divide_by_zero(self):
        a=8
        b=0
        cal=Calculator()
        with pytest.raises(ZeroDivisionError):
            cal.divide(a,b)