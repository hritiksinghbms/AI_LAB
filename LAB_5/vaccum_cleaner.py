def clean(floor,row,col):
    cost=0
    i,j,m,n=row,col,len(floor),len(floor[0])
    right=down=True
    cleaned=[not any(f) for f in floor]
    while not all(cleaned):
        while any(floor[i]):
            print_floor(floor,i,j)
            if floor[i][j]:
                cost+=1  
                floor[i][j]=0
                print_floor(floor,i,j)
            if not any(floor[i]):
                cleaned[i]=True
                break
            if j==n-1:
                cost+=1  
                j-=1
                right=False
            elif j==0:
                cost+=1  
                j+=1
                right=True
            else:
                if right:
                    cost+=1  
                    j+=1
                else:
                    cost+=1  
                    j-=1
        if all(cleaned):
            break
        if i==m-1:
            cost+=1  
            i-=1
            down=False
        elif i==0:
            cost+=1  
            i+=1
            down=True
        else:
            if down:
                cost+=1  
                i+=1
            else:
                cost+=1  
                i-=1
        if cleaned[i]:
            print_floor(floor,i,j)
    print("TOTAL COST TAKEN IS " + str(cost))
    
                
def print_floor(floor, row, col):
    for r in range(len(floor)):
        for c in range(len(floor[r])):
            if r == row and c == col:
                print(f" >{floor[r][c]}< ", end = '')
            else:
                print(f"  {floor[r][c]}  ", end = '')
        print(end = '\n')
    print(end = '\n')
    
a = int(input('Enter value of n : '))

floor = []
print('Enter the rows ')
for i in range(a):
    row = list(map(int, input().split()))
    floor.append(row)
   
start_row = int(input('Enter starting row '))
start_col = int(input('Enter starting column '))
clean(floor, start_row, start_col)
