# Your Sales by Match submission got 8.57 points out of 10

def match(x:list,a:int):
    x.sort
    count = 0
    for i in x:
        if i==a:
            count = count+1
    mapp[a]=count
    return mapp

def count(i):
    count = 0
    for i in range(1,i+1):
        if i%2==0:
            count=count+1
    return count 

def sockMerchant(n, x):
    
    for i in range(1,n):
        mapp = match(x,x[i])



    for i,j in mapp.items():
        if mapp[i] >=2:
            data = count(mapp[i])
            app.append(data)
    return app


if __name__ == '__main__':
     
    mapp = {}
    app = []
    n = int(input())

    ar = list(map(int, input().strip().split()))
    
    go = sockMerchant(n, ar)

    print(sum(go))
