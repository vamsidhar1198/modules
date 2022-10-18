def AM(x):
    return sum(x)/len(x)
def GM(x):
    prod=1
    for i in x:
        prod*=i
    return pow(prod,1/len(x))
def HM(x):
    sum=0
    for i in x:
        sum=sum+(1/i)
    return len(x)/sum
def means(x):
    return 'AM={} , GM={} , HM={}'.format(AM(x),GM(x),HM(x))
def maxi(x):
    c=x[0]
    for i in x[1:]:
        if c<i:
            c=i
    return c
def mini(x):
    c=x[0]
    for i in x[1:]:
        if c>i:
            c=i
    return c  
def sorting(x):
    while True:
        i=0
        count=0
        while True:
            if x[i]>x[i+1]:
                a=x[i]
                x[i]=x[i+1]
                x[i+1]=a
                count+=1
            i+=1
            if i==len(x)-1: break
        if count==0:break
    return x
def medi(x):
    a=sorting(x)
    if len(a)%2!=0:
        return (a[len(a)//2])
    else:
        return ((a[len(a)//2]+a[(len(a)//2)-1])/2)
def modes(x):
    a={}
    for i in x:
        a.update({i:0})
    for i in x:
        a[i]+=1
    count=maxi(list(a.values()))
    mode=[i for i,j in a.items() if a[i]==count]
    return mode,count
def varaince(x):
    var=0
    xbar=AM(x)
    for i in x:
        var=var+pow((i-xbar),2)
    return var/(len(x)-1)
def std(x):
    return pow(varaince(x),0.5)
def MAD(x):
    a=[abs(i-medi(x)) for i in x]
    return medi(a)
def covaraince(x,y):
    cov=0
    xbar=AM(x)
    ybar=AM(y)
    for i,j in zip(x,y):
        cov=cov+((i-xbar)*(j-ybar))
    return cov/(len(x))
def pearson(x,y):
    return covaraince(x,y)/(std(x)*std(y))
def spearman(x,y):
    sx=list(enumerate(sorting(x.copy()),1))
    sy=list(enumerate(sorting(y.copy()),1))
    dx={}
    for k in x:
        for i,j in sx:
            if j==k:dx.update({k:i})
    dy={}
    for k in y:
        for i,j in sy:
            if j==k:dy.update({k:i})
    a,b=list(dx.values()),list(dy.values())
    return pearson(a,b)
def skewness1(x):
    return (AM(x)-maxi(modes(x)[0]))/std(x)
def skewness2(x):
    return 3*(AM(x)-medi(x))/std(x)
def descriptive(x):
    import pandas as pd
    mean=[]
    median=[]
    variance=[]
    stdevi=[]
    mad=[]
    skewness=[]
    index=[]
    minis=[]
    maxis=[]
    for i in list(x.columns):
        if type(x[i].loc[0])==str:pass
        else:
            datalist=x[i].to_list()
            index.append(i)
            mean.append(AM(datalist))
            median.append(medi(datalist))
            variance.append(varaince(datalist))
            stdevi.append(std(datalist))
            mad.append(MAD(datalist))
            skewness.append(skewness2(datalist))
            maxis.append(maxi(datalist))
            minis.append(mini(datalist))
    return pd.DataFrame({'min':minis,'max':maxis,'mean':mean,'median':median,'variance':variance,'std':stdevi,'mad':mad,'skewness':skewness},index=index).transpose()                   
            