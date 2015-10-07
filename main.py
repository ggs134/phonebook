#-*- coding: utf-8 -*-

from MenuViewer import MenuViewer
from PhoneBookManager import PhoneBookManager
from MenuChoiceException import MenuChoiceException

def main():
    while(1):
        manager = PhoneBookManager()
        viewer=MenuViewer()
        viewer.showMenu()
        choice = int(raw_input()) 
        
        try:
            if choice < 1 or choice >3:
                raise MenuChoiceException()
            elif choice == 1:
                manager.inputData()
            elif choice == 2:
                print "프로그램을 종료합니다."
                return
        except MenuChoiceException as error:
            print "메뉴 선택을 처음부터 다시 시작합니다."



if __name__ == "__main__":
    main()
