from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Common import Assert
from Common.baseui import baseUI
import time
import os


#打开浏览器
#确定chromedriver.exe的位置
class TestFirstUIDemo:
    def test_testdemo1(self, driver, xpath=None):
        base=baseUI(driver)



        #打开网址
        driver.get("http://192.168.60.132/#/login")
        #输入用户名
        #通过xpath定位元素
        base.send_keys("请输入用户名","//input[@name='username']","admin")
        # username = driver.find_element_by_xpath("//input[@name='username']")
        # #清空一下
        # username.clear()
        # #输入登录数据
        # username.send_keys("admin")
        base.send_keys("请输入密码","//input[@name='password']","123456")
        # password = driver.find_element_by_xpath("//input[@name='password']")
        # password.clear()
        # password.send_keys("123456")
        #点击登录按钮 "//span[contains(text(),'登录')]"
        base.click("点击登录按钮","//span[contains(text(),'登录')]")


        # 点击商品按钮
        base.click("点击商品按钮","//span[contains(text(),'商品')]")
        # yingxiao = driver.find_element_by_xpath("//span[contains(text(),'商品')]")
        # yingxiao.click()
        # time.sleep(1)
        # #点击添加商品

        youhuiqueliebiao = driver.find_element_by_xpath("//span[contains(text(),'添加商品')]")
        youhuiqueliebiao.click()
        #
        anniu1 = driver.find_element_by_xpath("//label[contains(text(),'商品分类')]/following-sibling::div//span")
        anniu1.click()
        time.sleep(1)
        #
        anniu2 = driver.find_element_by_xpath("//li[contains(text(),'手机数码')]")
        anniu2.click()
        time.sleep(1)
        #
        anniu3 = driver.find_element_by_xpath("//li[contains(text(),'手机通讯')]")
        anniu3.click()
        time.sleep(1)
        #
        spmc = driver.find_element_by_xpath("//label[contains(text(),'商品名称')]/following-sibling::div//input")
        spmc.clear()
        spmc.send_keys("华为")
        time.sleep(1)
        #
        fbt = driver.find_element_by_xpath("//label[contains(text(),'副标题')]/following-sibling::div//input")
        fbt.clear()
        fbt.send_keys("华为P20Pro")
        time.sleep(1)
        #
        anniu4 = driver.find_element_by_xpath("//label[contains(text(),'商品品牌')]/following-sibling::div//input")
        anniu4.click()
        time.sleep(1)
        #
        anniu5 = driver.find_element_by_xpath("(//div/ul/li[contains(text(),'')])[26]")
        anniu5.click()
        time.sleep(1)
        #下一步，填写商品促销
        base.click("下一步，填写商品促销","//span[(text()='下一步，填写商品促销')]")
        # driver.find_element_by_xpath("//span[(text()='下一步，填写商品促销')]").click()
        #
        # #填写赠送积分 //label[contains(text(),'赠送积分')]/following-sibling::div//input
        # baseui.send_keys( "//label[contains(text(),'赠送积分')]/following-sibling::div//input", "111")
        base.send_keys("填写赠送积分","//label[contains(text(),'赠送积分')]/following-sibling::div//input","111" )
        base.send_keys("赠送成长值","//label[contains(text(),'赠送成长值')]/following-sibling::div//input", "222")
        base.send_keys("积分购买限制","//label[contains(text(),'积分购买限制')]/following-sibling::div//input", "333")
        # # 点击特惠促销  //span[contains(text(),'特惠促销')]
        base.click("点击特惠促销","//span[contains(text(),'特惠促销')]")
        base.click("下一步，填写商品属性","//span[(text()='下一步，填写商品属性')]")
        #点击属性类型 //input[@placeholder="请选择属性类型"]
        base.click("点击属性类型","//input[@placeholder='请选择属性类型']")
        #点击手机数码-手机通讯
        base.click("手机数码-手机通讯","//span[text()='手机数码-手机通讯']")
        #给颜色输入框输值
        base.send_keys("给颜色输入框输值","(//label[contains(text(),'商品规格')]/following-sibling::div//input)[1]","极光色")
        base.scroll_screen("滚动窗口")

        iframe = driver.find_element_by_xpath("(//iframe[contains(@id,'vue-tinymce-')])[1]")
        driver.switch_to.frame(iframe)

        base.send_keys("随便填值","(//body[@id='tinymce'])[1]","华为手机发布了最新旗舰手机P20系列宣布由“神奇女侠”盖尔·加朵担任东北欧地区代言人并放出了一支由她主演的P20 Pro大片《See More》。")
        driver.switch_to.default_content()
        time.sleep(1)
        base.click("下一步，选择商品关联","//span[(text()='下一步，选择商品关联')]")
        time.sleep(2)
        abc = "//div[@divrole='alert']/p[contains(text(),'修改成功')]"






        driver.quit()





















        # #输入优惠券列表文本框
        # yhqwb = driver.find_element_by_xpath("//label[contains(text(),'优惠券名称')]/following-sibling::div//input")
        # yhqwb.clear()
        # #输入文本框数据
        # yhqwb.send_keys("小米")
        # time.sleep(1)
        # #点击查询搜索按钮
        # sousuo = driver.find_element_by_xpath("(//button)[1]")
        # sousuo.click()
        # time.sleep(2)
        #
