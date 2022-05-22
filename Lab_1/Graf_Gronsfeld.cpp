#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
using namespace std;
int find_letter(char letter, string alphabet) {
	for (int j = 0; j < alphabet.size(); j++) {
		if (letter == alphabet[j]) return j;
	}
	return -1;
}
string read_key(int len) {
	string key;
	cout << "Введите ключ длинной не более " << len << " цифр\n";
	cin >> key;
	if (key.size() > len) {
		cout << endl << "Длина ключа превышает длину сообщения, перезапустите программу и введите верный ключ";
		exit(0);
	}
	string alhpabet = "0123456789";
	int flag = 0;
	for (int i = 0; i < key.size(); i++) {
		flag = find_letter(key[i], alhpabet);
		if (flag == -1) {
			cout << endl << "Ключ должен состоять только из цифр, перезапустите программу и введите верный ключ";
			exit(0);
		}
	}
	string new_key;
	for (int i = 0; i < (len / key.size()); i++) new_key += key;
	for (int i = 0; i < (len % key.size()); i++) new_key += key[i];
	return new_key;
}
void encryption(string key, string message, int len) {
	string low_alphabet = " abcdefghijklmnopqrstuvwxyz";
	string big_alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	string numbers = "0123456789";
	cout << endl << "Исходное сообщение: " << message << endl;
	int j;
	for (int i = 0; i < len; i++) {
		j = find_letter(message[i], low_alphabet);
		if (j == -1) {
			j = find_letter(message[i], big_alphabet);
			if (j == -1) {
				j = find_letter(message[i], numbers);
				if (j == -1) {
					cout << endl << "В сообщении есть буква не существующая в алфавите!";
					exit(0);
				}
				message[i] = numbers[(key[i] - '0' + j) % numbers.size()];
			}
			else message[i] = big_alphabet[(key[i] - '0' + j) % big_alphabet.size()];
		}
		else message[i] = low_alphabet[(key[i] - '0' + j) % low_alphabet.size()];
	}
	cout << "Ключ: " << key << endl;
	cout << "Результат: " << message << endl;
	exit(0);
}

void decryption(string key, string message, int len) {
	string low_alphabet = " abcdefghijklmnopqrstuvwxyz";
	string big_alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	string numbers = "0123456789";
	cout << endl << "Зашифрованное сообщение: " <<message <<endl;
	int j;
	for (int i = 0; i < len; i++) {
		j = find_letter(message[i], low_alphabet);
		if (j == -1) {
			j = find_letter(message[i], big_alphabet);
			if (j == -1) {
				j = find_letter(message[i], numbers);
				if (j == -1) {
					cout << endl << "В сообщении есть буква не существующая в алфавите!";
					exit(0);
				}
				message[i] = numbers[(j - (key[i] - '0') + numbers.size()) % numbers.size()];
			}
			else message[i] = big_alphabet[(j - (key[i] - '0') + big_alphabet.size()) % big_alphabet.size()];
		}
		else message[i] = low_alphabet[(j - (key[i] - '0') + low_alphabet.size()) % low_alphabet.size()];
	}
	cout << "Ключ: " << key << endl;
	cout << "Результат: " << message << endl;
	exit(0);
}
int main()
{
	setlocale(0, "");

	ifstream in("in.txt");

	string message;
	if (in.is_open()) while (getline(in, message))
		in.close();
	if (message == "") {
		cout << "СООБЩЕНИЕ ДЛЯ ШИФРОВАНИЯ/ДЕШИФРОВАНИЯ ОТСУТВУЕТ В ТЕКСТОВОМ ФАЙЛЕ 'in.txt', заполните файл и перезапустите программу";
		exit(0);
	}
	int len = message.size();
	string key = read_key(len);
	int choice;
	cout << endl << "Выберите зашифровать сообщение(1) или дешифровать(2): ";
	cin >> choice;
	if (choice == 1) encryption(key, message, len);
	if (choice == 2) decryption(key, message, len);
	else {
		cout << endl << "ВВЕДЕНО НЕВЕРНОЕ ЗНАЧЕНИЕ! Перезапустите программу";
		exit(0);
	}
}