def pal(n):
    if n==0:
        print("YES")
    elif n<100:
        print("NO")
    elif n<1000 and (n%100=0 or (n%10=0 and n%11=0)):
        print("YES")
    elif n==n//1000+((n-((n//1000)*1000))//100)*10+((n-((n-((n//1000)*1000))//100)*100-(n//1000)*1000)//10)*100+n%10*1000:
        print("YES")
    else:
        print("NO")
    
