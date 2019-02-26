#ab两个递增的数组，合并它们保持递顺序

def rank(a,b)：
       la =len(a)
       lb = len(b)
       if la==0:return b
       if lb ==0 :return a
       i,j,c =0,0,[]
       while True:
        if a<la and a[i]<b[j]:
          c.append(a[i])
          i +=1
        if j<lb and a[i]>=b[j]:
          c.append[b[j])
          j +=1
        elif i==la-1 and j==lb-1:
          return c
