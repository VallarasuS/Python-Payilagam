# ---------------------------------
# Print following pattern with loop
# ---------------------------------

# ---
# one
# ---

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

rows = 5

for i in range(rows):
    print("* " * rows)

print("-----------------")

# ---
# two
# ---

# *
# * *
# * * *
# * * * *
# * * * * *

rows = 5

for i in range(1, rows + 1):
    print("* " * i)

print("-----------------")

# -----
# three
# -----

# * * * * *
# * * * *
# * * *
# * *
# *

rows = 5

for i in range(5, 0, -1):
    print("* " * i)
