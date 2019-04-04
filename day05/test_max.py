import allure

@allure.feature('类上装饰器')
class TestZong:

    @allure.story('max方法上的')
    def test_max(self):
        assert 3>5

    @allure.story('max1方法上的')
    def test_max1(self):
        assert 4<5

    @allure.story('max2方法上的')
    def test_max2(self):
        assert 5<4
