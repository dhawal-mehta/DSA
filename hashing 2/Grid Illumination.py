"""Grid Illumination


You are given an integer A.
On a A x A grid of cells, each cell (x, y) with 0 <= x < A and 0 <= y < A has a lamp.

Initially, some number of lamps are on. B[i] tells us the location of the i-th lamp that is on. Each lamp that
is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).

For the i-th query C[i] = (x, y), the answer to the query is 1 if the cell (x, y) is illuminated, else 0.

After each query (x, y) [in the order given by queries], we turn off any lamps that are at cell (x, y) or
are adjacent 8-directionally (ie., share a corner or edge with cell (x, y).)

Return an array of D. Each value D[i] should be equal to the answer of the i-th query C[i].



Input Format

The first argument given is the integer A.
The second argument given is the integer matrix B.
The third argument given is the integer matrix C.

Output Format

Return an array of integers D. Each value D[i] should be equal to the answer of the i-th query C[i]

Constraints

1 <= A <= 10^9
1 <= B.length , C.length <= 20000
B[i].length = C[i].length = 2

For Example

Input 1:
    A = 5
    B = [[0,4], [4,4]]
    C = [[1,1], [1,0]]
Output 1:
    D = [1, 0]

Input 2:
    A = 6
    B = [[1,3], [2,4], [5,4]]
    C = [[2,4], [1,2]]
Output 2:
    D = [1, 0]

"""
# @param A : integer
# @param B : list of list of integers
# @param C : list of list of integers
# @return a list of integers
def solve(self, A, B, C):
    
    row = {}
    col = {}
    major = {}
    minor = {}
    lamps = set()
    
    for lamp in B:   # making maps
        x = lamp[0]
        y = lamp[1]
        
        if x*A + y not in lamps:
            if x in row:
                row[x] += 1
            else:
                row[x] = 1
            
            if y in col:
                col[y] += 1
            else:
                col[y] = 1
            
            if x-y in major:
                major[x-y] += 1
            else:
                major[x-y] = 1
            
            if x+y in minor:
                minor[x+y] += 1
            else:
                minor[x+y] = 1
            
            lamps.add(x*A + y)
    
    # print(row)
    # print(col)
    # print(major)
    # print(minor)
    # print(lamps)
    
    ans = []

    def remove(x,y):
        row[x] -= 1
        if row[x] == 0:
            row.pop(x)
        
        col[y] -= 1
        if col[y] == 0:
            col.pop(y)
        
        major[x-y] -= 1
        if major[x-y] == 0:
            major.pop(x-y)
        
        minor[x+y] -= 1
        if minor[x+y] == 0:
            minor.pop(x+y)
        
        # print(row)
        # print(col)
        # print(major)
        # print(minor)
        # print(lamps)
        
        
        
    for i in C:
        queryX = i[0]
        queryY = i[1]
        
        if (queryX in row) or (queryY in col) or (queryX-queryY in major) or (queryX+queryY in minor):
            ans.append(1)
        else:
            ans.append(0)
        
        
        # remove lamps :- 
        
        if queryX - 1 >= 0 and queryY -1 >= 0 and ( (queryX-1)*A + queryY-1 ) in lamps:
            lamps.remove( (queryX-1)*A + queryY-1   )
            remove(queryX-1, queryY-1)
        
        if queryX - 1 >=0 and ( (queryX-1)*A + queryY ) in lamps:
            lamps.remove( (queryX-1)*A + queryY   )
            remove(queryX-1, queryY)
            
        if queryX - 1 >=0 and queryY + 1 < A and ( (queryX-1)*A + queryY+1 ) in lamps:
            lamps.remove( (queryX-1)*A + queryY+1   )
            remove(queryX-1, queryY+1)
            
        if queryY -1 >= 0 and ( queryX*A + queryY-1 ) in lamps:
            lamps.remove( queryX*A + queryY-1   )
            remove(queryX, queryY-1)
        
        if queryX*A + queryY in lamps:
            lamps.remove( queryX*A + queryY )
            remove(queryX, queryY)
            
        if queryY + 1 < A and ( queryX*A + queryY+1 ) in lamps:
            lamps.remove( queryX*A + queryY+1   )
            remove(queryX, queryY+1)
            
        if queryX + 1 < A  and queryY - 1  >= 0 and ( (queryX+1)*A + queryY-1 ) in lamps:
            lamps.remove( (queryX+1)*A + queryY-1   )
            remove(queryX+1, queryY-1)            

        if queryX + 1 < A and ( (queryX+1)*A + queryY ) in lamps:
            lamps.remove( (queryX+1)*A + queryY   )
            remove(queryX+1, queryY)
            
        if queryX + 1 < A and queryY + 1 < A and ( (queryX+1)*A + queryY+1 ) in lamps:
            lamps.remove( (queryX+1)*A + queryY+1   )
            remove(queryX+1, queryY+1)   
    
    return ans
