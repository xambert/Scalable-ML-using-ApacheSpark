# your code goes here
import math
l1 = list(map(int,input().split(",")))
l2 = list(map(int,input().split(",")))
mean1 = 1.0 * sum(l1)/len(l1)
mean2 = 1.0 * sum(l2)/len(l2)
bias1 = [x-mean1 for x in l1] 
bias2 = [x-mean2 for x in l2]
var1 = sum([pow(x,2)/len(l1) for x in bias1])
var2 = sum([pow(x,2)/len(l2) for x in bias2])
std1 = pow(var1,0.5)
std2 = pow(var2, 0.5)
cov = 1.0 * sum([x*y for x,y in zip(bias1, bias2)])/len(l1)
print(cov, var1, var2)
corr = round(cov/ (std1 * std2),3)
print(corr)

l = sorted(l1)
n = len(l)
mean = 1.0 * sum(l)/n
print(l,n)
median = 1.0 * (l[n//2] + l[n//2+1])/2
bias = [1.0 * (x - mean) for x in l]
stdlst = [pow(x,2)/(n-1) for x in bias]
kurtlist = [pow(x,4) for x in bias]
skewlist = [pow(x,3) for x in bias]
kurt = sum(kurtlist)
skew = sum(skewlist)
std = math.sqrt(abs(sum(stdlst)))
stdround = round(std,3)
kurt = kurt/(1*n*pow(std,4))
skew = skew/(1*n*pow(std,3))
kurtround = round(kurt,3)
skewround = round(skew, 3)
print(mean,median,stdround,kurtround, skewround)
