def valInput(CheckType):
    pick = input("Wybierz co chesz zrobić: ")
    if CheckType == 0:
        while True:
            if pick.isdigit() == False:
                pick = input("Wprowadziałeś znak: ")
                continue
            elif 0 < int(pick) < 3:
                pick = int(pick)
                break
            else:
                pick = input("Liczba z poza zakresu: ")
                continue
        return pick


def main():
    print("Generuj dane: ")
    print("1. Bramki logiczne: ")
    print("2. Rownania matematyczne: ")
    x = valInput(0)
    print(x)


if __name__ == "__main__":
    main()
