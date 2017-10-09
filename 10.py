arr = ['1', '11', '21', '1211']
iter = 3
while iter < 30:
    string = arr[iter]
    last = 0
    resstr = ''
    for i in range(len(string)):
        print(string[i], string[i+1], i)
        if string[i] != string[i+1]:
            resstr += str(len(string[last:i])) + string[i]
            last = i+1
            print(resstr)
    iter += 1