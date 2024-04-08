import random
import os
import msvcrt


ABSOLUTE_PATH = 'D:/pass.txt'


def Create_Password(number_quantity):
  SECRET_SYMBOLS = 'abcdefgiklmnoprqstABCDEFGIKLMNOPRQST!@#$%^&*()123456789'
  temp = ''.join(random.sample(SECRET_SYMBOLS, number_quantity))
  return temp
  
def Text_File(pw, reason):
  full_str = '\n\n' + str(reason) + '\n' + str(pw)
  with open(ABSOLUTE_PATH, mode='a') as file:
      file.write(full_str)



def main():
  numbers = int(input("Введите число символов для пароля: "))
  reason = str(input("Для чего вам необходим пароль: "))
  pw: str = str(Create_Password(numbers))
  print(f'СГЕНЕРИРОВАННЫЙ ПАРОЛЬ: {pw}')
  Text_File(pw=pw,reason=reason)
  
while True:
  if __name__ == '__main__':
    main()
    print('Следующий пароль ------------ Enter \n Конец ------------------- Любая клавиша \n')
    while True:
      if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'\r':
          break
        else:
          exit()
    
  
    