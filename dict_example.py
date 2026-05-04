employees = {}
print(type(employees))

employees.update({
    "1000" : {
        "name": "Jobs",
        "designation": "CEO"
    }
})

employees.update({
    "1001": {
        "name": "Parithi",
        "designation": "CTO"
    }
})

employees.update({
    "1002": {
        "name": "Sanjay",
        "designation": "CFO"
    }
})

print(employees["1002"])

emp = [["1000","Jobs", "CEO"], ["1001","Parithi", "CTO"], ["1002","Sanjay", "CFO"]]

for e in emp:
   if e[0] == "1000":
        print(e)