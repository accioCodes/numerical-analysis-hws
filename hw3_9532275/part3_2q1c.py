x=[0.1,0.2,0.3,0.4]
w, h = 4, 4;
Matrix = [[0 for x in range(w)] for y in range(h)]
#  khune aval baraye height khune dovom baraye width
Matrix[0][0] = float(0.62049958)
Matrix[1][0] = float(-0.28398668)
Matrix[2][0] = float(0.00660095)
Matrix[3][0] = float(0.24842440)
unknown=float(0.25)
i=1
while(i<4):
    j=1
    while(j<=i):
        Matrix[i][j]=float(float(unknown-x[i-j])*float(Matrix[i][j-1])-float(unknown-x[i])*float(Matrix[i-1][j-1]))/float(x[i]-x[i-j])
        print(str(i)+" , "+str(j)+" is    "+str(Matrix[i][j]))
        j=j+1
    i=i+1
print(Matrix)
