import random
import pandas as pd
import matplotlib.pyplot as plt

#Part I
#Data Generation
dict_for_df = {}
val = 1
a0 = random.uniform(-5,5)
a1 = random.uniform(-5,5)
delta = random.uniform(-1,1)
for i in range(1,6,1):
    for j in range(1,11,1):
        for a in range(1,101,1):
           xreal = random.uniform(-10,10) 
           e=random.uniform((i*delta),(-i*delta))
           y = a0+(a1*xreal)+e
           dict_for_df[val] = [xreal,y]
           val = val+1

##print len(dict_for_df.keys())

#Part II
#m and b value computation
loop = 0
result = {}
sx = 0
sxx = 0
sy = 0
sxy = 0
iterate = 0

for key, value in dict_for_df.iteritems():
    sx += value[0]
    sxx += (value[0]*value[0])
    sy += value[1]
    sxy += (value[0]*value[1])
    loop += 1
    if(loop==100):
        m1 = float((100*sxy)-(sy*sx))
        m2 = float((100*sxx)-(sx*sx))
        m = float(m1/m2)
        b1 = float((sxx*sy)-(sxy*sx))
        b2 = float((100*sxx)-(sx*sx))
        b = float(b1/b2)
        loop = 0
        sx = 0
        sxx = 0
        sy = 0
        sxy = 0
        result[iterate] = [b,m]
        iterate = iterate+1

print 'm and b values for each 100 data sets'
for key, value in result.iteritems():
    print key
    print value[0]
    print value[1]


#Part III
iterate = 0
errorvalues = {}
for key, value in result.iteritems():
#Where is this mapped in code
    a0observed = value[0]
    a1observed = value[1]
    error1 = ((a0observed-a0)*(a0observed-a0))+((a1observed-a1)*(a1observed-a1))
    errorvalues[iterate] = [error1]
    iterate = iterate+1

print 'Error Value Computation Results'
for key, value in errorvalues.iteritems():
    print key
    print value[0]
    plt.plot(key, value[0],'-o',color = 'g')
    plt.xlabel("i values")
    plt.ylabel("Error Value")
plt.title("Ei vs i ")
plt.show()

print 'Number of values'
print len(errorvalues.keys())

iterate = 0
valuecount = 0
predicterrors = {}
avgerror = 0.0
avgerrorvalue = 0.00
for key, value in errorvalues.iteritems():
    avgerror= avgerror+float(value[0])
    iterate = iterate+1
    if(iterate==10):
        avgerrorvalue=float(avgerror/10.0)
        #print avgerrorvalue
        predicterrors[valuecount] = avgerrorvalue
        valuecount = valuecount+1
        iterate=0

for key, value in predicterrors.iteritems():
    print key
    print 'Prediction Errors'
    print value


#Plot the bar chart of errors
plt.bar(range(len(predicterrors)), predicterrors.values(), align='center',color = 'g')
plt.xticks(range(len(predicterrors)), predicterrors.keys())
plt.xlabel("i values")
plt.ylabel("Error Value")
plt.title("bar chart of errors")
plt.show()


#PLot 100 values (x,y)    
#Plot line from m and b values
#Repeat for 5 Sets of data
#Fetch 

def plotgraphs(result,dict_for_df,iterate,startpos):
    [b,m] = result[iterate]
    endpos = startpos+100
    for i in range(startpos,endpos,1):
        (key,value) = dict_for_df[i]
        x = key
        y = m*x+b
        plt.plot(key,value,'-o',color = 'r')
        plt.plot(x,y,'-o', color = 'g')
        i = i+1
    plt.title("Points (red), Predicted Line - Green")
    plt.show()

    
plotgraphs(result,dict_for_df,0,1)
plotgraphs(result,dict_for_df,10,1001)
plotgraphs(result,dict_for_df,20,2001)
plotgraphs(result,dict_for_df,30,3001)
plotgraphs(result,dict_for_df,40,4001)


