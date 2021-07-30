#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/23/2021 11:13 
# @Author : Julia
# @Version：V 0.1
# @File : test_02_fixture.py
# @desc :   text fixtures的目的是为测试的重复执行提供一个可靠的固定基线。 pytest fixture比经典的xUnit setUp/tearDown方法有着显着的改进：
#           1. fixtures具有明确的名称,在测试用例/类/模块或整个项目中通过声明使用的fixtures名称来使用。
#           2. fixtures以模块化方式实现,因为每个fixture名称都会触发调用fixture函数,该fixture函数本身可以使用其它的fixtures。
#           3. 从简单的单元测试到复杂的函数测试,fixtures的管理允许根据配置和组件选项对fixtures和测试用例进行参数化,
#           或者在测试用例/类/模块或整个测试会话范围内重复使用该fixture。
#           pytest继续支持经典的xUnit风格的setup方法
#           Pytest一次只会缓存一个fixture实例。 这意味着当使用参数化fixture时,pytest可能会在给定范围内多次调用fixture函数。

import pytest
import random
import allure

#---------------------------fixtures------------------------------------------------------
@pytest.fixture
def random_num():
    return random.randint(0,100)


@pytest.fixture(scope='module')
def ramdom_int_in_module():
    return random.randint(10,20)


@pytest.fixture(scope='module')
def chrome_driver():
    print('create a chrome headless driver')
    from selenium import webdriver
    option = webdriver.ChromeOptions()
    option.headless = True
    driver = webdriver.Chrome(options=option)
    print(type(driver))
    yield driver
    print('close chrome driver')
    driver.close()

import smtplib
@pytest.fixture(scope="module")
def smtp_connection(request):
    smtp_connection = smtplib.SMTP("smtp.gmail.com",587,timeout=5)

    def fin():
        print("teardown smtp_connection")
        smtp_connection.close()

    request.addfinalizer(fin)
    return smtp_connection  # provide the fixture value


@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {
            "name": name,
            "orders": []
        }
    return _make_customer_record


@pytest.fixture(scope="module",
                params=["smtp.gmail.com","mail.python.org"])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param,587,timeout=5)
    yield smtp_connection
    print("finalizing %s" % smtp_connection)
    smtp_connection.close()

@pytest.fixture(params=[0,1,pytest.param(2,marks=pytest.mark.skip)])
def data_set(request):
    return request.param

@pytest.fixture(scope="module",params=["mod1","mod2"])
def modarg(request):
    param = request.param
    print("  SETUP modarg %s" % param)
    yield param
    print("  TEARDOWN modarg %s" % param)

@pytest.fixture(scope="function",params=[1,2])
def otherarg(request):
    param = request.param
    print("  SETUP otherarg %s" % param)
    yield param
    print("  TEARDOWN otherarg %s" % param)
#---------------------------tests------------------------------------------------------

@allure.feature("feature: test_02_fixture")
@allure.story("story: fixture 作为函数参数使用")
def test_fixture(random_num):
    print(f'random_num: {random_num}')
    assert random_num < 100


@allure.feature("feature: test_02_fixture")
@allure.story("story: conftest.py: 共享fixture函数, 共享测试数据")
def test_fixture_in_configtest(fixture_in_config):
    assert fixture_in_config == 'fixture in configtest'


@allure.feature("feature: test_02_fixture")
@allure.story("story: scope")
def test_fixture_scope_module01(ramdom_int_in_module):
    assert ramdom_int_in_module < 10


@allure.feature("feature: test_02_fixture")
@allure.story("story: scope")
def test_fixture_scope_module02(ramdom_int_in_module):
    assert ramdom_int_in_module < 10


@allure.feature("feature: test_02_fixture")
@allure.story("story: scope")
def test_fixture_scope_function01(random_num):
    print(f'random_num: {random_num}')
    assert random_num > 100


@allure.feature("feature: test_02_fixture")
@allure.story("story: scope")
def test_fixture_scope_function02(random_num):
    print(f'random_num: {random_num}')
    assert random_num > 100


@allure.feature("feature: test_02_fixture")
@allure.story("story: 高范围的fixture函数优先实例化")
def test_teardown(chrome_driver):
    chrome_driver.get('https://www.baidu.com')
    assert chrome_driver.current_url == 'https://www.baidu.com/'



@allure.feature("feature: test_02_fixture")
@allure.story("story: Fixture作为函数工厂")
def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
    assert customer_1 !=customer_2 !=customer_3



@allure.feature("feature: test_02_fixture")
@allure.story("story: Fixtures参数化")
def test_ehlo(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes


@allure.feature("feature: test_02_fixture")
@allure.story("story: 使用参数化fixtures标记")
def test_data(data_set):
    pass


@allure.feature("feature: test_02_fixture")
@allure.story("story: 使用fixture实例自动组织测试用例")
@allure.testcase("case url","test case: 01")
def test_0(otherarg): #最先运行 完全独立
    print("  RUN test0 with otherarg %s" % otherarg)

@allure.feature("feature: test_02_fixture")
@allure.story("story: 使用fixture实例自动组织测试用例")
@allure.testcase("case url","test case: 02")
def test_1(modarg): # 1[mod1] 2[mod1-1]  2[mod1-2] 1[mod2] 2[mod2-1] 2[mod2-2]
    print("  RUN test1 with modarg %s" % modarg)

@allure.feature("feature: test_02_fixture")
@allure.story("story: 使用fixture实例自动组织测试用例")
@allure.testcase("case url","test case: 03")
def test_2(otherarg,modarg):
    print("  RUN test2 with otherarg %s and modarg %s" % (otherarg,modarg))

@allure.feature("feature: test_02_fixture")
@allure.story("story: 指定多个Fixture方法")
@pytest.mark.usefixtures("otherarg","modarg")
def test_multifixture():
    print("  RUN test2 with otherarg %s and modarg %s" % (otherarg,modarg))

