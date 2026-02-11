numbers = {5, 1, 2, 3, 4, 5}
print(numbers)
print(type(numbers))

numbers = {9, 1, 2, 3, 1, 1, 2, 3, 4, 4, 5}
print(numbers)
# print(dir(set))

work_week = {"Mon", "Tue", "Wed", "Thu", "Fri"}
week_end = {"Sat", "Sun"}

# work_week.remove("Mon")
# print(work_week)

# union
week = work_week | week_end
print("week", week)

# difference
week_end = week - work_week
print("Week end", week_end)

team_a = {"John", "Mike", "Dave", "Loki"}
team_b = {"John", "Mike", "Ram", "Felix"}

# intersection
common = team_a & team_b
print(common)

# symmetric difference
unique = team_a ^ team_b
print(unique)


for day in week:
    print(day)


list_num = [1, 2, 3, 4, 4, 3, 3]
print(list_num)

unique_nums = set(list_num)
print(unique_nums)
