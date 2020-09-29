lista1 = [1, 0, 1, 0, 0, 1]
lista2 = [1, 0, 1, 0, 1, 1]
lista3 = []
slowo = "AND"


if slowo == "AND":
    for i in range(len(lista1)):
        if lista1[i] == 1 and lista2[i] == 1:
            final_col = 1
            lista3.append(final_col)
        else:
            final_col = 0
            lista3.append(final_col)
print(lista3)
