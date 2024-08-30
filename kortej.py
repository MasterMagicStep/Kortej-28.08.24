#
ImmutableVar = 1, 2, True, 'Ka-boom'
mutated = [1, 2.2, "Ice", True]
#
print(mutated)
#закомментировал и попытку изменения кортежа и нижние функции которые не входят в задание
#mutated.append(False)
#mutated.remove(1)
#mutated.extend('fly')
#
mutated[1]= 'string'
mutated[3]= 4
print(mutated)
#
print(ImmutableVar)
#ImmutableVar[2] = False
#print(ImmutableVar)
#Кортежи не поддерживают обращение по элементам, в моем понимании это как
#строгая библиотека в которой есть определенное кол-во книг. Мы можем их брать и читать, но
# вносить или убрать нам как бы запрещено
