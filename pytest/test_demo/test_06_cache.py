#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 7/23/2021 17:38 
# @Author : Julia
# @Version：V 0.1
# @File : test_06_cache.py
# @desc :   pytest test_06_cache.py
#           pytest test_06_cache.py --lf  last failed
#           pytest test_06_cache.py --ff   failed first
#           pytest --last-failed --last-failed-no-failures all    # run all tests (default behavior)
#           pytest --last-failed --last-failed-no-failures none   # run no tests and exit
#           pytest --cache-show命令行选项查看缓存的内容：

import pytest

@pytest.mark.parametrize("i",range(30))
def test_num(i):
    if i in (17,25,30):
       pytest.fail("bad luck")