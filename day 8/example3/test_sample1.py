import pytest

class TestClass():
    def setup_class(self):
        print("setup class called once")

    def teardom_class(self):
        print("teardom class called once")

    def setup_method(self):
        print("setup method called before every test case")

    def teardom_method(self):
        print("teardom method called after every test case")

    def test_one(self):
        print("one")
        assert True

    def test_two(self):
        print("two")
        assert False