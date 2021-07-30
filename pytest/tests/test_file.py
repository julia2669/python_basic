# _*_ coding: utf-8 _*_
# @Time : 7/22/2021 15:19 
# @Author : Julia
# @Version：V 0.1
# @File : test_file.py
# @desc :   测试文件以test_开头（以_test结尾也可以）
#           以test_开头的测试函数
#           断言使用assert
import pytest

def romanToInt(s: str) -> int:
    dic = {
        "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
        "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900
    }
    l=len(s)
    i=0
    sum=0
    while i < l:
        if l==1:
            return dic.get(s)
        else:
            if s[i:i+2] in dic:
                sum = sum+dic.get(s[i:i+2])
                i+=2
            else:
                sum += dic.get(s[i])
                i+=1
    return sum


def test_romanToInt_01():
    num = "III"
    assert romanToInt(num) == 3

def test_romanToInt_02():
    num = "IV"
    assert romanToInt(num) == 4

def test_romanToInt_03():
    num = "IX"
    assert romanToInt(num) == 9

def test_romanToInt_04():
    num = "LVIII"
    assert romanToInt(num) == 58

def test_romanToInt_05():
    num = "MCMXCIV"
    assert romanToInt(num) == 1994

@pytest.mark.skip
def test_romanToInt_06():
    num = "IM"
    assert romanToInt(num) == 1994



