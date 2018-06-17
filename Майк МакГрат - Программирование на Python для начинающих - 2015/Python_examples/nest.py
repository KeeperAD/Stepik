for i in range(1, 4):
    for j in range(1, 4):
        if i == 1 and j == 1:
            continue

        if i == 2 and j == 1:
            break
        print('Запущено i=', i, 'j=', j)
