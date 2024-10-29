def grade_calc ():
# Use of function alows this to be used in a wider programe, defined dicts at the start
    weight = {}
    grades = {}
# The next line asks for the module name which can be used later on for a visual summary of the computed results
    module = ((str(input('Please input the module name: '))).lower()).title()
    stu_num = int(input('Please input the number of students: '))
    cw_num = int(input('Please input how many courseworks there are in this module: '))
# This first for loop gathers the weighting of coursework in its correct order and saves it to a dict called weight
    for i in range(cw_num):
        n = i+1
        weight[n] = int(input(f'Please input the weight (%) of Coursework {n}: '))
#This next loop has a nested loop, the first loop is for each student number, and orders the data in the grades dict
#The nested loop ensures that this coursework is not going to be skipped and needs to be inputed
    for i in range(1, (stu_num +1)):
        grades[i] = []
        for q in weight:
            temp = str(input(f"Does student {i} qualify for EC in coursework {q} (y/n): "))
            if temp.lower() == 'y':
                continue
            elif temp.lower() == 'n':
                grades[i].append(int((input(f"Please input student {i}'s grade (out of 100) for coursework {q}: "))))
#This section checks whether we need to use min() to remove the lowest grade (special circumstances), and then calculate overall module grade 
        ec = str(input(f"Is student {i} elegible for EC where the lowest mark is dropped? (y/n): "))
        if ec.lower() == 'y':
            grades[i].pop(grades[i].index(min(grades[i])))
            print(grades)
        elif ec.lower() == 'n':
            continue
    for i in grades:
        temp = 0
        for q in range(len(grades[i])):
            temp += (grades[i][q])*(int(weight[(q+1)])/100)
        grades[i] = [temp]
        if int(temp) <= 49:
            grades[i].append('Grade: F')
        elif int(temp) <= 59:
            grades[i].append('Grade: D')
        elif int(temp) <= 69:
            grades[i].append('Grade: C')
        elif int(temp) <= 79:
            grades[i].append('Grade: B')
        elif int(temp) <= 89:
            grades[i].append('Grade: A')
        elif int(temp) <= 100:
            grades[i].append('Grade: A*')
    print(grades)     
grade_calc()
