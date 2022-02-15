check_result = 100

oprs = ['+','-','']


formular = [("1",o1,"2",o2,"3",o3,"4",o4,"5",o5,"6",o6,"7",o7,"8",o8,"9")   
            for o1 in oprs 
            for o2 in oprs 
            for o3 in oprs 
            for o4 in oprs
            for o5 in oprs
            for o6 in oprs 
            for o7 in oprs 
            for o8 in oprs]


n = len(formular)

results = [0] * n

formular_m = [""] * n

for i in range(n):
    formular_m[i] = formular_m[i].join(formular[i])
    results[i] = eval(formular_m[i])
    for ans in range(10):
        if results[i] == ans:
            print(formular_m[i],"=", results[i])

