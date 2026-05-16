data = "all operations will return a copy of the string"

pos = data.find("copy")
print(pos)

# Logic / Algo

# split word by word
# search = match = compare
# Found = True
# Not Found False

# Sudo

# search term -> copy
# string op split -> by ' ' -> words
# word == search term
# if found print True exit
# if not found repeat step 3 until end of words Exit

data = "all operations will return a copy of the string"
search_term = "will"

words = data.split()
found = False
index = -1

# ["all" "operations" "will" "return" "a" "copy" "of" "the" "string"]
for w in words:
    index = index  + 1
    if search_term == w:
        found = True
        break

if found:
    print(search_term, "found in pos", index)
else:
    print(search_term, "not found")





data = "all operations will return a copy of the string"
search_term = "will"

words = data.split()
found = False

index = -1

i = 0
while i < len(words):
    w = words[i] 

    if search_term == w:
        found = True
        index = i 

    i = i + 1

if found:
    print(search_term, "found in ", index)
else:
    print("word not found")