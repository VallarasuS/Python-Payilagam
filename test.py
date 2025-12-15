# print(dir(set))

# print(dir(list))

A = {3, 6, 9, 12, 15, 18}  # Multiples of Three
B = {2, 4, 6, 8, 10, 12}  # Multiples of Two

union = A | B  # -> { 2, 3, 4, 6, 8, 9, 10, 12, 15, 18  }

intersection = A & B  # -> { 6, 12 }

difference = A - B  # { 3, 9, 15, 18 }

difference = B - A  # { 2, 4, 8, 10 }

symmetric_difference = A ^ B  # { 2, 3, 4, 8, 9, 10, 15, 18 }
