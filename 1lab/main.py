

if __name__ == "__main__":

  import random

rows = int(input("Введите количество рядов:"))
cols = int(input("Введите количество столбцов:"))
table = []

print()
print("Таблица:")

for r in range(rows):
    row = []
    for c in range(cols):
        row.append(random.randint(1, 9))
    table.append(row)

for row in table:
    print(*row)

print() 

print("Максимумы в строках:")
for row in table:
    row_max = row[0]
    for num in row:
        if num > row_max:
            row_max = num
    print(row_max)

print()  

print("Максимумы в столбцах:")
for c in range(cols):
    col_max = table[0][c]
    for r in range(rows):
        if table[r][c] > col_max:
            col_max = table[r][c]
    print(col_max)

print()  


if rows == cols:
    main_sum = 0
    side_sum = 0
    for i in range(rows):
        main_sum += table[i][i]
        side_sum += table[i][rows - 1 - i]
    print("Cумма главной диагонали:", main_sum)
    print("Cумма побочной диагонали:", side_sum)
else: 
  print("Нельзя посчитать суммы диагоналей, так как количество строк не совпадает с количеством столбцов")

print()  

best_row_idx = 0
best_row_sum = 0
for r in range(rows):
    current_sum = 0
    for c in range(cols):
        current_sum += table[r][c]
    if current_sum > best_row_sum:
        best_row_sum = current_sum
        best_row_idx = r
print("Строка с наибольшей суммой:", best_row_idx)
print("Сумма:", best_row_sum)  
