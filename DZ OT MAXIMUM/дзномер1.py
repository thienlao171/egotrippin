x = input("введите слово: ")
def palindromSsss(x):
    return x[::-1] == x
while True:
    if palindromSsss(x):
        print(f"{x} 'это палиндромом'")
        break
    else:
        print('это не палиндромом')
        break
