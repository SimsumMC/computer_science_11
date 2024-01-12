liste = ["a", "m", "n", "l", "e", "p"]


def bubble_sort(liste):
    n = len(liste)            # n = 8 Länge der Liste
    for i in range(n - 1):    # for mit 1.L = 8-1 = 7
        print(f"i: {i}")
        for j in range(n - i - 1):  # n -
            print(f"J: {j}")
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]

bubble_sort(liste)


print(liste)
