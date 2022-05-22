import random
import sys
def key_generator(p, g):
	a = random.randint(2, 100)
	b = random.randint(2, 100)
	print("Число, которое знает только Алиса: ", a)
	print("Число, которое знает только Боб: ", b, "\n")
	A = (g**a)%p
	B = (g**b)%p
	print("Алиса знает: a = ", a, " и A = ", g, "^", a, " mod ", p, " = ", A)
	print("   Не знает: b, но знает B = ", g, "^b mod ", p, " = ", B, "\n")
	print("Боб знает: b = ", b, " и B = ", g, "^", b, " mod ", p, " = ", B)
	print(" Не знает: a, но знает A = ", g, "^a mod ", p, " = ", A, "\n")
	print("Шпион знает: ", "A = ", g, "^a mod ", p, " = ", A)
	print("Шпион знает: ", "B = ", g, "^b mod ", p, " = ", B, "\n")
	print("Не знает: a и b ", "\n")
	Alice_key = (B**a)%p
	Bob_key = (A**b)%p
	if Alice_key == Bob_key:
		print("Алиса знает: p = ", p, ", g = ", g, ", a = ", a, ", A = ", A, ", B = ", B, " и свой ключ s1 = ", Alice_key)
		print("   Не знает: b", "\n")
		print("Боб знает: p = ", p, ", g = ", g, ", b = ", b, ", A = ", A, ", B = ", B, " и свой ключ s2 = ", Bob_key)
		print(" не знает: a", "\n")
		print("Шпион знает: p = ", p, ", g = ", g, ", A = ", A, ", B = ", B)
		print("   не знает: a, b, ключи s1 и s2", "\n")
		print("Таким образом, Алиса и боб получили общий одинаковый ключ, который знают только они и с его помощью Алиса передаст Бобу сообщение через шифр Цезаря", "\n")
		return Alice_key
	else:
		sys.exit("Ключи не совпали")
def to_Bob(message, key):
	message = list(message)
	low_alphabet = " abcdefghijklmnopqrstuvwxyz"
	low_alphabet = list(low_alphabet)
	big_alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	big_alphabet = list(big_alphabet)
	numbers = "0123456789"
	numbers = list(numbers)
	for i in range(0, len(message)):
		if low_alphabet.count(message[i]) == 0:
			if big_alphabet.count(message[i]) == 0:
				if numbers.count(message[i]) == 0:
					sys.exit("В сообщении есть буква не существующая в алфавите!")
				j = numbers.index(message[i])
				message[i] = numbers[(key + j) % len(numbers)]
			else:
				j = big_alphabet.index(message[i]) 
				message[i] = big_alphabet[(key + j) % len(big_alphabet)]
		else:
			j = low_alphabet.index(message[i]) 
			message[i] = low_alphabet[(key + j) % len(low_alphabet)]
	message = "".join(message)
	print("Алиса отправила: ", message, "\n")
	return message
def from_Alice(message, key):
	message = list(message)
	low_alphabet = " abcdefghijklmnopqrstuvwxyz"
	low_alphabet = list(low_alphabet)
	big_alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	big_alphabet = list(big_alphabet)
	numbers = "0123456789"
	numbers = list(numbers)
	for i in range(0, len(message)):
		if low_alphabet.count(message[i]) == 0:
			if big_alphabet.count(message[i]) == 0:
				if numbers.count(message[i]) == 0:
					sys.exit("В сообщении есть буква не существующая в алфавите!")
				j = numbers.index(message[i])
				message[i] = numbers[(j - (key % len(numbers)) + len(numbers)) % len(numbers)]
			else:
				j = big_alphabet.index(message[i])
				message[i] = big_alphabet[(j - (key % len(big_alphabet)) + len(big_alphabet)) % len(big_alphabet)]
		else:
			j = low_alphabet.index(message[i])
			message[i] = low_alphabet[(j - (key % len(low_alphabet)) + len(low_alphabet)) % len(low_alphabet)]
	message = "".join(message)	
	print("Боб получил: ", message)
print("Введите два числа, которые будут известны Алисе, Бобу и шпиону: ")
p,g=map(int,input().split())
print()
key = key_generator(p, g)
print("Введите сообщение, которое Алиса отправит Бобу шифром Цезаря: ")
message = input()
print()
message = to_Bob(message, key)
from_Alice(message, key)
