def inputData ( ) :
    employ_num = float( input('ป้อนรหัสพนักงาน : ') )
    employ_name = input('ป้อนชื่อพนักงาน : ')
    employ_money = float( input('ป้อนเงินเดือนปกติ : ') )
    return employ_num, employ_name, employ_money

def calTax ( employ_money ) :
    employ_aftax = employ_money * 7 / 100
    return employ_aftax

def BeaPraGun ( ) :
    PraGun = 500
    return PraGun

def calSutti ( employ_aftax, PraGun ) :
    sutti = employ_aftax - PraGun
    return sutti

def showPaSeeandSutti ( employ_aftax, sutti ) :
    print(f'ภาษีเป็นเงิน : {employ_aftax:.2f} บาท')
    print(f'เงินเดือนสุทธิเป็นเงิน : {sutti:.2f} บาท')

print('----------------------------')
print('-----คำนวณเงินเดือนพนักงาน-----')
print('-----------------------------')
employ_num, employ_name, employ_money = inputData( )
employ_aftax = calTax( employ_money )
PraGun = BeaPraGun( )
sutti = calSutti( employ_aftax, PraGun)
print('----------------------------')
showPaSeeandSutti( employ_aftax, sutti)
print('-----------------------------')