def inputData( ) :
    ka_x = float(input('ป้อนค่า X : '))
    return ka_x

def calSummagan( ka_x ) :
    ka_y = 2 * ka_x * ka_x + 2 * ka_x + 1
    return ka_y

def showSolu( ka_y ) :
    print(f'ได้ผลลัพธ์ค่า y เป็น {ka_y}')

print('------------------------')
print('คำนวณสมการ 2x^2 + 2x + 1')
print('-------------------------')
ka_x = inputData( )
ka_y = calSummagan( ka_x )
print('-------------------------')
showSolu(ka_y)
print('-------------------------')