import allure
from Common import Assert
from Common import Request

# 新建一个 Assert.Assertions() 的对象 对象名: assertions
assertions = Assert.Assertions()

# 新建一个 Request.Request() 的对象 对象名: request
request = Request.Request()

myToken = ''
head = {'Authorization': myToken}


@allure.feature("登录模块")
class TestLogin(object):

    @allure.story("登录系统")
    def test_case_login(self):
        login_data = {"password": "123456", "username": "admin"}
        login_resp = request.post_request(url="http://qa.guoyasoft.com:8099/admin/login", json=login_data)
        # .assert_code 用来断言 状态码 ; 第一个参数 填 响应的状态码, 第二个参数 期望值
        assertions.assert_code(login_resp.status_code, 200)
        # 获取响应正文  字典格式
        login_resp_json = login_resp.json()
        # .assert_in_text 用来断言字符 第一个参数填 比较多的那个字符; 第二参数填 这个字符 是否存在第一个字符里面
        assertions.assert_in_text(login_resp_json['message'],'成功')

        data_token = login_resp_json['data']
        token = data_token['token']
        token_head = data_token['tokenHead']

        # global : 引入 全局变量 然后才可以对全局变量重新赋值
        global myToken
        global head
        myToken = token_head + token
        head = {'Authorization': myToken}

    @allure.story("获取用户信息")
    def test_case(self):
        get_info_resp = request.get_request(url='http://qa.guoyasoft.com:8099/admin/info', headers=head)

        assertions.assert_code(get_info_resp.status_code, 200)

    @allure.story("获取列表")
    def test_case1(self):
        param = {'pageNum': 1, 'pageSize': 3}
        get_info_resp = request.get_request(url='http://qa.guoyasoft.com:8099/brand/list',params=param, headers=head)

        assertions.assert_code(get_info_resp.status_code, 200)
