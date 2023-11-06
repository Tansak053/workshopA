def inputData ( ) :
    std_num = float(input('ป้อนรหัสนักเรียน : '))
    std_name = input('ป้อนชื่อนักเรียน : ')
    std_testone = float(input('ป้อนคะแนนสอบครั้งที่ 1 : '))
    std_testtwo = float(input('ป้อนคะแนนสอบครั้งที่ 2 : '))
    std_testthree = float(input('ป้อนคะแนนสอบครั้งที่ 3 : '))
    return std_num, std_name, std_testone,std_testtwo,std_testthree

def calTotalTest ( std_testone, std_testtwo, std_testthree ) :
    total_score = std_testone + std_testtwo + std_testthree
    return total_score

def calAverScore ( total_score ) :
    aver_score = total_score / 3
    return aver_score

def showAverage ( aver_score ) :
    print(f'คะแนนเฉลี่ย : {aver_score:.2f} คะแนน')

print('----------------------------------------')
print('-----คำนวณคะแนนเฉลี่ยจากการสอบ 3 ครั้ง-----')
print('----------------------------------------')
std_num, std_name, std_testone, std_testtwo, std_testthree = inputData( )
total_score = calTotalTest ( std_testone, std_testtwo, std_testthree )
aver_score = calAverScore( total_score )
print('----------------------------------------')
showAverage( aver_score )
print('----------------------------------------')