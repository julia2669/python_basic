#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/23/2021 15:16 
# @Author : Julia
# @Version：V 0.1
# @File : conftest.py
# @desc :
import pytest, pytest_html
import tempfile
import os

# 把case失败的接口会话写入报告
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    # 如果错误了
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            try:
                html = item.funcargs["api"].info
                extra.append(pytest_html.extras.html(f'<pre>{html}</pre>'))
            except Exception:
                pass
        report.extra = extra
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")  # 解决乱码

@pytest.fixture()
def cleandir():
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)