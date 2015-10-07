# -*- coding: utf-8 -*-

from pymongo import MongoClient
from MenuChoiceException import MenuChoiceException
client = MongoClient()
db = client.cm

class PhoneBookManager:
    def _readFriendInfo(self):
        _name = raw_input("이름 : ")
        _phoneNum = raw_input("전화번호 : ")
        return {"이름":_name, "전화번호" : _phoneNum}
    
    def _readUnivFriendInfo(self):
        _name = raw_input("이름 : ")
        _phoneNum = raw_input("전화번호 : ")
        _major = raw_input("전공 : ")
        _year = raw_input("학년 : ")
        return {"이름":_name, "전화번호" : _phoneNum, "전공" : _major, "학년" : _year}

    def _readCompanyInfo(self):
        _name = raw_input("이름 : ")
        _phoneNum = raw_input("전화번호 : ")
        _company = raw_input("회사 : ")
        return {"이름":_name, "전화번호" : _phoneNum, "회사": _company}
    
    def inputData(self):
        print "데이터 입력을 시작합니다."
        print "1. 일반 2.대학 3.회사"
        print "선택>>"

        choice = int(raw_input())

        if choice > 3 or choice<1:
            raise MenuChoiceException

        elif choice == 1:
            db.cm.insert(self._readFriendInfo())

        elif choice == 2:
            db.cm.insert(self._readUnivInfo())

        elif choice == 3:
            db.cm.insert(self._readCompanyInfo())

    def searchData(self, _name):
        _result = db.cm.find_one({"이름" : _name})
        if _result is None:
            return None
        if _result is not None:
            return _result
    
    def deleteData(self, _name):
        _result = db.cm.delete_one({"이름":_name})

        if _result == 1:
            return true
        else:
            return false




