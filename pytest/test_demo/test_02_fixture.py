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




# 1. fixture 作为函数参数使用
@pytest.fixture
def random_num():
    return random.randint(0,100)


def test_fixture(random_num):
    print(f'random_num: {random_num}')
    assert random_num < 100

# 2. conftest.py: 共享fixture函数, 共享测试数据

def test_fixture_in_configtest(fixture_in_config):
    assert fixture_in_config == 'fixture in configtest'

# 3. scope one of ``"function"`` (default), ``"class"``, ``"module"``, ``"package"`` or ``"session"``.

@pytest.fixture(scope='module')
def ramdom_int_in_module():
    return random.randint(10,20)



def test_fixture_scope_module01(ramdom_int_in_module):
    assert ramdom_int_in_module < 10



def test_fixture_scope_module02(ramdom_int_in_module):
    assert ramdom_int_in_module < 10


def test_fixture_scope_function01(random_num):
    print(f'random_num: {random_num}')
    assert random_num > 100


def test_fixture_scope_function02(random_num):
    print(f'random_num: {random_num}')
    assert random_num > 100

# 4. 高范围的fixture函数优先实例化 相同范围的fixture对象的按引入的顺序及fixtures之间的依赖关系按顺序调用。fixture结束/执行teardown代码
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


def test_teardown(chrome_driver):
    chrome_driver.get('https://www.baidu.com')
    assert chrome_driver.current_url == 'https://www.baidu.com/'

# 5. 请注意,如果在设置代码期间(yield关键字之前)发生异常,则不会调用teardown代码(在yield之后)。
#    执行teardown代码的另一种选择是利用请求上下文对象的addfinalizer方法来注册teardown函数。
#       使用addfinalizer可以注册多个teardown函数。
#       无论fixture中setup代码是否引发异常,都将始终调用teardown代码。 即使其中一个资源无法创建/获取,也可以正确关闭fixture函数创建的所有资源：
import smtplib
@pytest.fixture(scope="module")
def smtp_connection(request):
    smtp_connection = smtplib.SMTP("smtp.gmail.com",587,timeout=5)

    def fin():
        print("teardown smtp_connection")
        smtp_connection.close()

    request.addfinalizer(fin)
    return smtp_connection  # provide the fixture value

# 6. Fixture作为函数工厂: Fixture返回一个函数，以支持根据参数得到不同的结果。适用于登录。。。
@pytest.fixture
def make_customer_record():
    def _make_customer_record(name):
        return {
            "name": name,
            "orders": []
        }
    return _make_customer_record


def test_customer_records(make_customer_record):
    customer_1 = make_customer_record("Lisa")
    customer_2 = make_customer_record("Mike")
    customer_3 = make_customer_record("Meredith")
    assert customer_1 !=customer_2 !=customer_3

# 7. Fixtures参数化 它们将被多次调用,每次执行一组相关测试
@pytest.fixture(scope="module",
                params=["smtp.gmail.com","mail.python.org"])
def smtp_connection(request):
    smtp_connection = smtplib.SMTP(request.param,587,timeout=5)
    yield smtp_connection
    print("finalizing %s" % smtp_connection)
    smtp_connection.close()


def test_ehlo(smtp_connection):
    response,msg = smtp_connection.ehlo()
    assert response == 250
    assert b"smtp.gmail.com" in msg
    assert 0  # for demo purposes

# 8.使用参数化fixtures标记
@pytest.fixture(params=[0,1,pytest.param(2,marks=pytest.mark.skip)])
def data_set(request):
    return request.param


def test_data(data_set):
    pass

# 9. 使用fixture实例自动组织测试用例  pytest在测试运行期间最小化活动Fixture方法的数量
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


def test_0(otherarg): #最先运行 完全独立
    print("  RUN test0 with otherarg %s" % otherarg)


def test_1(modarg): # 1[mod1] 2[mod1-1]  2[mod1-2] 1[mod2] 2[mod2-1] 2[mod2-2]
    print("  RUN test1 with modarg %s" % modarg)


def test_2(otherarg,modarg):
    print("  RUN test2 with otherarg %s and modarg %s" % (otherarg,modarg))

# 10. 指定多个Fixture方法
#       使用标记机制的通用函数在测试模块级别指定Fixture方法使用情况 必须使用pytestmark
#       pytestmark = pytest.mark.usefixtures("cleandir")


@pytest.mark.usefixtures("otherarg","modarg")
def test_multifixture():
    print("  RUN test2 with otherarg %s and modarg %s" % (otherarg,modarg))

# 11. 自动使用fixtures @pytest.fixture(autouse=True) autouse fixtures服从scope=关键字参数 慎用!

