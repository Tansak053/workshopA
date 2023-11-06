def inputData ( ) :
    product_name = input('ป้อนชื่อสินค้า : ')
    product_price = float( input('ป้อนราคาสินค้า : ') )
    return product_name, product_price

def Tax ( ) :
    tax = 7 / 100
    return tax

def calTax ( product_price, tax ) :
    all_prod_price = product_price * tax
    return all_prod_price

def showAllPrice ( all_prod_price ) :
    print('ภาษีคิดเป็นร้อยละ 7 ของราคาสินค้า')
    print(f'ราคาสินค้าที่ต้องชำระ {all_prod_price} บาท')

print('--------------------------')
print('------คำนวณราคาสินค้า-------')
print('--------------------------')
product_name, product_price = inputData( )
tax = Tax( )
all_prod_price = calTax( product_price, tax )
print('--------------------------')
showAllPrice( all_prod_price )
print('--------------------------')