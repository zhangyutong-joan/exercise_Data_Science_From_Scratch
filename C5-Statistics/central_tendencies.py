from collections import Counter

def mean(x):
    '''平均值'''
    return sum(x)/len(x)

def median(v):
    '''中位数'''
    n=len(v)
    sorted_v=sorted(v)
    midpoint=n//2
    if n%2==1:
        # n为奇数
        return sorted_v[midpoint]
    else:
        lo=midpoint-1
        hi=midpoint
        return(sorted_v[lo]+sorted_v[hi])/2

def quantile(x,p):
    '''分位数'''
    p_index=int(p*len(x))
    return sorted(x)[p_index] #returns the pth-percentile value in x

def mode(x):
    '''众数？'''
    counts=Counter(x)
    max_count=max(counts.values())
    return [x_i for x_i,count in counts.items() if count==max_count]

if __name__ == '__main__':
    a=[3,2,1,6,7,3]
    print(mean(a))
    print(median(a))
    print(quantile(a,0.1))
    print(mode(a))
