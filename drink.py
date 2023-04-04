# class parrot:
#     species='птица'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def sing(self,song):
#         return '{} поет {}'.format(self.name,song)
#     def dance(self):
#         return '{} танцует'.format(self.name)
# kesha=parrot('Кеша',10)
# cookie=parrot('Куки',15)
# print('Кеша - {}'.format(kesha.__class__.species))
# print('Куки тоже {}'.format(cookie.__class__.species))
# print('{} - {}-летний попугай'.format(kesha.name,kesha.age))
# print('{} - {}-летний попугай'.format(cookie.name,cookie.age))
# print(kesha.sing('песенки'))
# print(kesha.dance())
class soda:
    def __init__(self,dob=None):
        self.dob=dob
    def show_my_drink(self):
        if self.dob==None:
            return 'Обычная газировка'
        else:
            return 'Газировка и {}'.format(self.dob)
limon=soda()
print(limon.show_my_drink())