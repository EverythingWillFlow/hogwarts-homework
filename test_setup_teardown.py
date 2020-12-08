import pytest


def setup_module():
    print("\nsetup_module:整个module只执行一次")


def teardown_module():
    print("\nteardown_module:整个module只执行一次")


def setup_function():
    print("\nsetup_function: 每个不在类中的用例开始之前会执行！")


def teardown_function():
    print("\nteardown_function:每个不在类中的用例结束后会执行！")


def test_one():
    print("正在执行测试模块--test_one")


def test_two():
    print("正在执行测试模块--test_two")


class TestCase():
    def setup_class(self):
        print("\nsetup_class:所有类中用例执行之前")

    def teardown_class(self):
        print("\nteardown_class:所有类中用例执行之后")

    def setup_method(self):
        print("\nsetup_method:每个用例执行之前")

    def teardown_method(self):
        print("\nteardown_method:每个用例执行之后")

    def test_three(self):
        print("正在执行测试类里的方法--test three")

    def test_four(self):
        print("正在执行测试类里的方法--test four")
