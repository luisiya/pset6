

import cs50

def main():
    while True:
        print("Приветик! Напиши любую сумму и узнаешь сколько это монет ", end = "")
        money = cs50.get_float()
        if money <= 0:
            break

        coins = 0
        cents = int(round(money  * 100))

        first25 = cents // 25
        cents %= 25

        second10 = cents // 10
        cents %= 10

        third5 = cents // 5
        cents %= 5

        coins = first25 + second10 + third5 + cents

        print("Итого монеток ", coins)
        break

if __name__ == "__main__":
    main()