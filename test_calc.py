import pytest
from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        print("开始计算")
        self.calc = Calculator()

    def teardown_class(self):
        print("结束计算")

    @pytest.mark.parametrize('a,b,expect', [
        (3, 5, 8), (-1, -2, -3), (100, 200, 300)
    ], ids=["int", "minus", "bigint"])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect
