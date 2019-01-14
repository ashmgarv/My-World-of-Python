def abc(matrix):
    if(len(matrix)==0):
        return
    if(len(matrix)==1):
        return matrix[0][0]
    queue=[(matrix[0][i],i) for i in range(0,len(matrix))]
    h=1
    while(h<len(matrix)):
        temp=[]
        while(queue):
            a,b=queue.pop(0)
            if(b==0):
                sum=matrix[h][b]+a
                sumr=matrix[h][b+1]+a
                temp.append((sum,b))
                temp.append((sumr,b+1))
            elif(b==len(matrix)-1):
                sum = matrix[h][b] + a
                suml = matrix[h][b-1] + a
                temp.append((sum, b))
                temp.append((suml, b-1))
            else:
                sum = matrix[h][b] + a
                suml = matrix[h][b - 1] + a
                sumr = matrix[h][b + 1] + a
                temp.append((sum, b))
                temp.append((suml, b - 1))
                temp.append((sumr, b + 1))
        queue=temp[:]
        h=h+1
    return min(queue)[0]

matrix = [[1,5,3,8],
          [4,5,6,5],
          [7,0,1,3],
          [7,0,1,2]]

min = abc(matrix);
print(min);



