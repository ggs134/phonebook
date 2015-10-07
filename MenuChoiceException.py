#-*- coding: utf-8 -*-

class MenuChoiceException(Exception):
    def __init__(self, choice):
        print "잘못된 선택이 이뤄졌습니다."
        self._wrongChoice = choice

    def showWrongChoice(self):
        print "%d에 해당하는 선택은 존재하지 않습니다."%(_wrongChoice)
