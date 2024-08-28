# Chapter02-03
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 기본 인스턴스 메소드

# 클래스 선언
class Car(object):
    '''
    Car Class
    Author : Me
    Date : 2019.11.08
    Description : Class, Static, Instance Method
    '''

    # Class Variable
    price_per_raise_before = 1.0
    price_per_raise_after = 1.2

    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method1
    # self : 객체의 고유한 속성 값 사용 
    # self가 들어가면 instance method 라고 생각하면 됨. 
    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
    
    # Instance Method2
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))
    
    # Instance Method3 
    def get_price_cal(self): 
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') *Car.price_per_raise_after)
        
    
    
# 자동차 인스턴스    
car1 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car2 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# 인스턴스 매소드 써보기 
# 전체정보 접근 
car1.detail_info()

# 가격정보 (직접 접근)
print(car1._details.get('price'))

# 가격정보 (인상 전)
print(car1.get_price())
print(car2.get_price())

# 가격정보 (인상 후)
print(car1.get_price_cal())
print(car2.get_price_cal())

# 가격 인상 (클래스 매소드 미사용) 
Car.price_per_raise_after = 1.5
print(car1.get_price_cal())
print(car2.get_price_cal())
