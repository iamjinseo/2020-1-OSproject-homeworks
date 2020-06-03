import operator
print("1. 데이터 추가\n")
print("2. 데이터 검색\n")
print("3. 데이터 삭제\n")
print("4. 데이터 정렬\n")
print("0. 종료\n")
stdInfo = {}

def add_Data() :
    name = input("enter students name : ")
    stdInfo[name] = []

    department = input("학과 명을 입력 : ")
    stdNum = input("학번입력 : ")
    stdInfo[name].append(department)
    stdInfo[name].append(stdNum)

    KORgrade = int(input("국어 점수 입력 : "))
    stdInfo[name].append(KORgrade)

    ENGgrade = int(input("영어 점수 입력 :"))
    stdInfo[name].append(ENGgrade)

    MTHgrade = int(input("수학 점수 입력 : "))
    stdInfo[name].append(MTHgrade)

    sum = KORgrade + ENGgrade + MTHgrade
    average = int(sum / 3)
    stdInfo[name].append(sum)
    stdInfo[name].append(average)

    if average >= 95:
        stdInfo[name].append("A+")
    elif average >= 90:
        stdInfo[name].append("A0")
    elif average >= 85:
        stdInfo[name].append("B+")
    elif average >= 80:
        stdInfo[name].append("B0")
    elif average >= 75:
        stdInfo[name].append("C+")
    elif average >= 70:
        stdInfo[name].append("C0")
    elif average >= 65:
        stdInfo[name].append("D+")
    elif average < 65:
        stdInfo[name].append("F")
    else:
        print("잘못된 점수입니다.\n")

def search_Std() :
    searchName = input("검색할 이름 입력 : ")
    if searchName in stdInfo:
        print(searchName + "의 성적 정보들 입니다. (순서대로 학과, 학번, 국어점수, 영어점수, 수학점수, 총합, 평균, 학점)")
        print(str(stdInfo[searchName]) + ("\n"))
    else:
        print("잘못된 이름입니다.\n")

def delete_Std() :
    searchName2 = input("삭제할 이름 입력 : ")
    if searchName2 in stdInfo:
        print(searchName2 + "의 데이터를 삭제합니다.\n")
        del stdInfo[searchName2]
    else :
        print(("잘못된 이름입니다.\n"))

def sorting() :
    sortedInfo = sorted(stdInfo.items(), key=operator.itemgetter(1))
    print(sortedInfo, "\n")
    # 학과 이름으로 데이터를 정렬했습니다.

while(True) :
    menu = int(input("메뉴를 선택하세요 : "))
    if menu ==0 :
        break
    elif menu ==1 :
        i=1
        for i in range(5) :
            add_Data()
    elif menu == 2 :
        search_Std()
    elif menu == 3 :
        delete_Std()
    elif menu == 4 :
        sorting()