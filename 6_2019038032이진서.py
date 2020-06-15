import operator
print("1. 데이터 추가\n")
print("2. 데이터 검색\n")
print("3. 데이터 삭제\n")
print("4. 데이터 정렬\n")
print("0. 종료\n")
stdInfo = {}
class Student :
    name = ""
    department = ""
    stdnum = 0
    KORgrade = 0
    ENGgrade = 0
    MTHgrade = 0
    sum = 0
    average = 0
    Grade = ""
    def add_Data(self) :
        self.name = input("enter students name : ")
        self.department = input("학과 명을 입력 : ")
        self.stdnum = input("학번입력 : ")
        self.KORgrade = int(input("국어 점수 입력 : "))
        self.ENGgrade = int(input("영어 점수 입력 : "))
        self.MTHgrade = int(input("수학 점수 입력 : "))
        self.sum = self.KORgrade + self.ENGgrade + self.MTHgrade
        self.average = int(self.sum / 3)
        if self.average >= 95:
            self.Grade = "A+"
        elif self.average >= 90:
            self.Grade = "A0"
        elif self.average >= 85:
            self.Grade= "B+"
        elif self.average >= 80:
            self.Grade = "B0"
        elif self.average >= 75:
            self.Grade = "C+"
        elif self.average >= 70:
            self.Grade = "C0"
        elif self.average >= 65:
            self.Grade = "D+"
        elif self.average < 65:
            self.Grade = "F"
        else:
            print("잘못된 점수입니다.\n")
    def Lists(self) :
        infoList = [self.department, self.stdnum, self.name, self.KORgrade, self.ENGgrade, self.MTHgrade, self.sum, self.average, self.Grade]
        return infoList

def search_Std(stdInfo) :
    searchName = input("검색할 이름 입력 : ")
    if searchName in stdInfo.keys() :
        print(searchName + "의 성적 정보들 입니다. (순서대로 학과, 학번, 이름, 국어점수, 영어점수, 수학점수, 총합, 평균, 학점)")
        print(str(stdInfo[searchName]) + "\n")
    else:
        print("잘못된 이름입니다.\n")

def delete_Std(stdInfo) :
    searchName = input("삭제할 이름 입력 : ")
    if searchName in stdInfo.keys():
        print(searchName + "의 데이터를 삭제합니다.\n")
        del stdInfo[searchName]
    else :
        print("잘못된 이름입니다.\n")

def sorting(stdInfo) :
    sortedStdInfo=sorted(stdInfo.items(), key=operator.itemgetter(1))
    print(sortedStdInfo, "\n")
        # 학과 이름으로 데이터를 정렬했습니다.

stdInfo=[]
Std1=Student()
Std2=Student()
Std3=Student()
Std4=Student()
Std5=Student()
while(True) :
    menu = int(input("메뉴를 선택하세요 : "))
    if menu ==0 :
        break
    elif menu ==1 :
        Std1.add_Data()
        Std2.add_Data()
        Std3.add_Data()
        Std4.add_Data()
        Std5.add_Data()
        stdInfo={Std1.name:Std1.Lists(), Std2.name:Std2.Lists(), Std3.name:Std3.Lists(), Std4.name:Std4.Lists(), Std5.name:Std5.Lists()}
    elif menu == 2 :
        search_Std(stdInfo)
    elif menu == 3 :
        delete_Std(stdInfo)
    elif menu == 4 :
        sorting(stdInfo)