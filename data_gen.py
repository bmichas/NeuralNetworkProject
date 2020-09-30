import random
from pandas import DataFrame


def data_gen_gate(gate_type, lines, gen_type):
    # listy do generatora
    # pierwsza kolumna
    row_f_col = []
    # druga kolumna
    row_s_col = []
    # trzecia kolumna finalna
    row_final_col = []

    # tablica do zmiany liczby na bramke
    gate_name_dict = {'1': 'AND', '2': 'OR',
                      '3': 'NAND', '4': 'NOR', '5': 'XOR', '6': 'XNOR'}
    gate_type = str(gate_type)
    # zamiana zmiennej gate type na slowo przedstawiajace bramke
    fin_gate_name = gate_name_dict[gate_type]
    print(fin_gate_name)
    # generowanie dwóch pierwszych kolumn
    for _ in range(0, lines):
        f_col = random.randint(0, 1)
        s_col = random.randint(0, 1)
        # pierwsza kolumna
        row_f_col.append(f_col)
        # druga kolumna
        row_s_col.append(s_col)

    # generator trzeciej kolumny referencyjnej z wynikiem pewnym
    # Dla bramki AND
    if fin_gate_name == 'AND':
        for i in range(len(row_f_col)):
            if row_f_col[i] == 1 and row_s_col[i] == 1:
                final_col = 1
                row_final_col.append(final_col)
            else:
                final_col = 0
                row_final_col.append(final_col)
    # Dla bramki OR
    elif fin_gate_name == 'OR':
        for i in range(len(row_f_col)):
            if row_f_col[i] == 0 and row_s_col[i] == 0:
                final_col = 0
                row_final_col.append(final_col)
            else:
                final_col = 1
                row_final_col.append(final_col)
    # Dla bramki NAND
    elif fin_gate_name == 'NAND':
        for i in range(len(row_f_col)):
            if row_f_col[i] == 1 and row_s_col[i] == 1:
                final_col = 0
                row_final_col.append(final_col)
            else:
                final_col = 1
                row_final_col.append(final_col)
    # Dla bramki NOR
    elif fin_gate_name == 'NOR':
        for i in range(len(row_f_col)):
            if row_f_col[i] == 0 and row_s_col[i] == 0:
                final_col = 1
                row_final_col.append(final_col)
            else:
                final_col = 0
                row_final_col.append(final_col)
    # Dla bramki XOR
    elif fin_gate_name == 'XOR':
        for i in range(len(row_f_col)):
            if row_f_col[i] == 0 and row_s_col[i] == 0:
                final_col = 0
                row_final_col.append(final_col)
            elif row_f_col[i] == 1 and row_s_col[i] == 1:
                final_col = 0
                row_final_col.append(final_col)
            else:
                final_col = 1
                row_final_col.append(final_col)
    # Dla bramki XNOR
    elif fin_gate_name == 'XNOR':
        for i in range(len(row_f_col)):
            if row_f_col[i] == 0 and row_s_col[i] == 0:
                final_col = 1
                row_final_col.append(final_col)
            elif row_f_col[i] == 1 and row_s_col[i] == 1:
                final_col = 1
                row_final_col.append(final_col)
            else:
                final_col = 0
                row_final_col.append(final_col)
    print("Wybrałeś bramkę: ", gate_type)
    # wszystkie bramki logiczne 1 lista
    logic_gate_list = [row_f_col, row_s_col, row_s_col]
    print(row_f_col)
    print(row_s_col)
    print(row_final_col)
    print("====================")
    print(logic_gate_list)
    df = DataFrame(logic_gate_list).transpose()
    df.columns = ['p', 'q', 'final']
    print(df)


def mat_function():
    return 0


def logic_gates():
    print("Wpisz ilość wierszy do wygenerowania: ")
    rows = valInput(1)
    print("Wybierz rodzaj bramki logicznej: ")
    print("1. AND")
    print("2. OR")
    print("3. NAND")
    print("4. NOR")
    print("5. XOR")
    print("6. XNOR")
    print("0. Cofnij")
    gate = valInput(2)
    # liczba na końcu przedstawia czy generowanie dla bramek logicznych "1" czy matematyczne "2"
    data_gen_gate(gate, rows, 1)


def valInput(CheckType):
    pick = input("Wybierz co chesz zrobić: ")
    gates = [1, 2, 3, 4, 5, 6]
    # Wybierranie co chcesz zrobic czy matematyczne czy bramka
    if CheckType == 0:
        while True:
            if pick.isdigit() == False:
                pick = input("Wprowadziałeś znak: ")
                continue
            elif 0 <= int(pick) < 3:
                pick = int(pick)
                break
            else:
                pick = input("Liczba z poza zakresu: ")
                continue
    # Wybieranie ilości wierszy
    elif CheckType == 1:
        while True:
            if pick.isdigit() == False:
                pick = input("Wprowadziłeś znak: ")
                continue
            elif int(pick) > 1000:
                pick = input("Wprowadziłes za duża liczbe: ")
                continue
            elif int(pick) < 1001:
                pick = int(pick)
                break
    # Wybieranie bramki
    elif CheckType == 2:
        while True:
            if pick.isdigit() == False:
                pick = input("Wprowadziałeś znak: ")
                continue
            elif int(pick) in gates:
                pick = int(pick)
                break
            else:
                main()
    return pick


def main():
    print("Generuj dane: ")
    print("1. Bramki logiczne")
    print("2. Rownania matematyczne")
    print("0. Wyjdź z programu")
    x = valInput(0)
    if x == 1:
        logic_gates()
    elif x == 2:
        mat_function()
    else:
        print("Do zobaczenia!")


if __name__ == "__main__":
    main()
