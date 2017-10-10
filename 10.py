arr = ['1', '11', '21', '1211']
iter = 3
while iter < 30:
    string = arr[iter]
    last = 0
    resstr = ''
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            substr = string[last:i+1]
            resstr += str(len(substr)) + string[i]
            last = i+1
    substr = string[last:]
    resstr += str(len(substr)) + string[last]
    print(resstr)
    arr.append(resstr)
    iter += 1

print(len(arr[30]))
#5808
