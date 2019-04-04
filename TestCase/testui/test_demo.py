from selenium import webdriver
from Common import Assert
from Common.Assert import Assertions
from Common.baseui import baseUI
import time
import os
import allure
from Common import Request


class TestFirstUIDemo1:
    def test_demo3(self, driver):
        base = baseUI(driver)
        driver.get("http://192.168.60.132/#/login")
        # 输入用户名
        # 通过xpath定位元素
        base.send_keys("请输入用户名", "//input[@name='username']", "admin")
        # username = driver.find_element_by_xpath("//input[@name='username']")
        # #清空一下
        # username.clear()
        # #输入登录数据
        # username.send_keys("admin")
        base.send_keys("请输入密码", "//input[@name='password']", "123456")
        # password = driver.find_element_by_xpath("//input[@name='password']")
        # password.clear()
        # password.send_keys("123456")
        # 点击登录按钮 "//span[contains(text(),'登录')]"
        base.click("点击登录按钮", "//span[contains(text(),'登录')]")
        # 点击订单
        base.click("点击营销按钮", "//span[contains(text(),'订单')]")
        # 点击订单列表
        base.click("点击优惠券列表", "//span[(text()='订单列表')]")
        # 点击订单分类
        base.click("点击订单状态", "//label[contains(text(),'订单状态')]/following-sibling::div//input")
        # 点击待发货
        base.click("点击待发货", "//span[(text()='待发货')]")
        # 点击查询搜索
        base.click("点击查询搜索", "//span[contains(text(),'查询搜索')]")
        base.click("点击选择条数","(//div/div/input[contains(text(),'')])[8]")
        base.click("点击选择5条","//span[text()='5条/页']")
        base.click("点击全选编号","//label[@role='checkbox']")
        base.click("点击批量操作","//input[@placeholder='批量操作']")
        base.click("点击批量发货","//span[text()='批量发货']")
        base.click("点确定","//span[contains(text(),'确定')]")
        #获取有多少行
        a = len(driver.find_elements_by_xpath("//tbody/tr"))

        for i in range(1,a+1):
            base.click("配送方式","//tbody/tr[{0}]/td[6]".format(i))
            base.click("点顺丰快递","(//span[text()='顺丰快递'])[5]")
            base.send_keys("点击输入订单编号","//tbody/tr[{0}]/td[7]//input".format(i),"666666666666666")


        base.click("点击确定", "//span[text()='确定']")
        base.click("在次点击确定", "(//span[contains(text(),'确定')])[2]")




        driver.quit()



    #配送方式//tbody/tr/td[6]
    #点顺丰快递//span[text()='顺丰快递']
    #点击输入订单编号//tbody/tr/td[7]
    #点击确定
        # # 定位编号
        # num = base.get_text('获取编号', '//tbody/tr[3]/td[2]')
        # # 定位订单编号
        # order_num = base.get_text('获取订单编号', '//tbody/tr[3]/td[3]')
        # # 点击订单发货
        # base.click("点击订单发货", "(//tbody/tr[3]/td[10]/div/button/span)[3]")
        # # 点击确定
        # base.click("#点击确定", "//span[(text()='确定')]")
        # # 点击确定
        # base.click("#点击确定", "(//span[contains(text(),'确定')])[2]")
        # text1 = driver.find_element_by_xpath("//div[@role='alert']/p").text
        # Assert = Assertions()
        # Assert.assert_in_text(text1, '发货成功')
        # # 点击输入搜索订单编号
        # base.send_keys("点击输入搜索订单编号", "(//input[contains(text(),'')])[1]", order_num)
        # # 点击查询搜索
        # base.click("点击查询搜索", "//span[contains(text(),'查询搜索')]")
        # time.sleep(1)
        # # 获取所有编号
        # nums = driver.find_elements_by_xpath("//tbody/tr/td[2]")
        #
        # # 先给a赋0的值
        # a = 0
        # for n in nums:
        #     # 将n转换为可示文本
        #     print(n.text)
        #     if n.text == num:
        #         a = 1
        # assert a == 1


        # base.click("点击提交按钮", "//span[(text()='提交')]")
        # base.click("点击确认","//span[contains(text(), '确定')]")
        # text1 = driver.find_element_by_xpath("//div[@role='alert']/p").text

        # print(text1)
        # Assert = Assertions()
        # Assert.assert_in_text(text1,'成功')

