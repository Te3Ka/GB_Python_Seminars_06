'''
Проверка на палиндром.
'''

def palindrom(_phrase):
	if len(_phrase) <= 1:
		return True
	elif _phrase[0] == _phrase[-1]:
		palindrom(_phrase[1:-1])
	else:
		return False


_str = str(input("Введите слово для проверки: "))
print(palindrom(_str))