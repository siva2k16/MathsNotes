import math
import matplotlib.pyplot as plt

def computevaluesnewtonraphson(initval):
    f_ = {}
    f_x = {}
    f_xx = {}
    result = {}
    iterate = 1
    val1 = 0.0
    val2 = 0.0    
    val3 = 0.0
    i = 0.0
    initloop = True
    i = initval
    currentval = 0.00
    prevval = 0.00
    while(i<10):
        try:
            val1 = (4.0/i) - (6.0/(1-i))
            val2 = (-4.0/(i*i)) - (6.0/((1-i)*(1-i)))
            val3 = 4*math.log(i) + 6*math.log(1-i)
            if(initloop):
                result[iterate] = initval
                currentval = initval-((val1)/(val2))
                prevval = currentval
                initloop = False
                i = currentval
                f_x[iterate] = val1
                f_xx[iterate] = val2
                f_[iterate] = val3
                iterate = iterate+1
            else:
                result[iterate] = currentval
                currentval = prevval-((val1)/(val2))
                i = currentval
                f_x[iterate] = val1
                f_xx[iterate] = val2
                f_[iterate] = val3
                if(abs(currentval-prevval)<0.0001):
                    break
                prevval = currentval
                iterate = iterate+1
        except Exception: 
            initloop = False            
            pass
    return f_,f_x,f_xx,result
    
f_ = {}
f_x = {}
f_xx = {}
result = {}

f_, f_x, f_xx, result = computevaluesnewtonraphson(0.03)

#plot graphs
print 'v values'
x = result.values()
print x
y = f_.values()
print y
plt.plot(x,y,'-o', color = 'g')
plt.xlabel("X obtained values")
plt.ylabel("F(x) Value")
plt.title("Newton Raphson - X obtained vs F(x) for Start value .03")
plt.show()
   
f_, f_x, f_xx, result = computevaluesnewtonraphson(0.75)

#plot graphs
print 'v values'
x = result.values()
print x
y = f_.values()
print y
plt.plot(x,y,'-o', color = 'g')
plt.xlabel("X obtained values")
plt.ylabel("F(x) Value")
plt.title("Newton Raphson - X obtained vs F(x) for Start value 0.75")
plt.show()

def computegradientdescent(initval, learningrate,tolerancerate):
    f_ = {}
    f_x = {}
    result = {}
    iterate = 1 
    val1 = 0.0
    val2 = 0.0    
    val3 = 0.0
    i = 0.0
    initloop = True
    i = initval
    currentval = 0.00
    prevval = 0.00
    while(i<10):
        try:
            val1 = (4.0/i) - (6.0/(1-i))
            val2 = (learningrate)*val1
            val3 = i - val2
            val4 = 4*math.log(i) + 6*math.log(1-i)
            if(initloop):
                result[iterate] = initval                
                currentval = val3
                prevval = currentval
                initloop = False
                i = currentval
                f_[iterate] = val4
                f_x[iterate] = val2
                iterate = iterate+1
            else:
                result[iterate] = currentval
                currentval = val3
                i = currentval
                f_x[iterate] = val2
                f_[iterate] = val4                
                result[iterate] = currentval
                if(abs(currentval-prevval)<tolerancerate):
                    break
                prevval = currentval
                iterate = iterate+1
        except Exception: 
            initloop = False            
            pass
    return f_,f_x,result


f_ = {} 
f_x = {}
result = {}

f_,f_x, result = computegradientdescent(0.03,-0.001,0.0001)

#plot graphs
print 'v values'
x = result.values()
y = f_.values()
print 'Start Value - 0.03'
print 'Learning Rate - .001'
print len(x)
print len(y)
print x
print y
plt.plot(x,y,'-o', color = 'g')
plt.xlabel("X obtained values")
plt.ylabel("F(x) Value")
plt.title("Gradient Descent - X obtained vs F(x) for Start value 0.03, Learning Rate 0.001")
plt.show()

f_,f_x, result = computegradientdescent(0.03,-.0005,0.0001)

#plot graphs
print 'v values'
x = result.values()
y = f_.values()
print 'Start Value - 0.03'
print 'Learning Rate - .0005'
print len(x)
print len(y)
plt.plot(x,y,'-o', color = 'g')
plt.xlabel("X obtained values")
plt.ylabel("F(x) Value")
plt.title("Gradient Descent - X obtained vs F(x) for Start value 0.01, Learning Rate 0.0005")
plt.show()


f_,f_x, result = computegradientdescent(0.03,-0.0001,0.0001)

#plot graphs
print 'v values'

x = result.values()
y = f_.values()
print 'Start Value - 0.03'
print 'Learning Rate - 0.0001'
print len(x)
print len(y)
plt.plot(x,y,'-o', color = 'g')
plt.xlabel("X obtained values")
plt.ylabel("F(x) Value")
plt.title("Gradient Descent - X obtained vs F(x) for Start value 0.03, Learning Rate 0.0001")
plt.show()

f_,f_x, result = computegradientdescent(0.03,-0.00005,0.0001)

#plot graphs
print 'v values'
x = result.values()
y = f_.values()
print 'Start Value - 0.03'
print 'Learning Rate - 0.00005'
print len(x)
print len(y)
plt.plot(x,y,'-o', color = 'g')
plt.xlabel("X obtained values")
plt.ylabel("F(x) Value")
plt.title("Gradient Descent - X obtained vs F(x) for Start value 0.03, Learning Rate 0.00005")
plt.show()


f_,f_x, result = computegradientdescent(0.03,-0.00001,0.0001)

#plot graphs
print 'v values'
x = result.values()
y = f_.values()
print 'Start Value - 0.03'
print 'Learning Rate - 0.00001'
print len(x)
print len(y)
plt.plot(x,y,'-o', color = 'g')
plt.xlabel("X obtained values")
plt.ylabel("F(x) Value")
plt.title("Gradient Descent - X obtained vs F(x) for Start value 0.03, Learning Rate 0.00001")
plt.show()

f_,f_x, result = computegradientdescent(0.77,-.001,0.0001)

#plot graphs
print 'v values'
x = result.values()
y = f_.values()
print 'Start Value - 0.77'
print 'Learning Rate --.001'
print len(x)
print len(y)
plt.plot(x,y,'-o', color = 'g')
plt.xlabel("X obtained values")
plt.ylabel("F(x) Value")
plt.title("Gradient Descent - X obtained vs F(x) for Start value 0.77, Learning Rate 0.00001")
plt.show()

f_,f_x, result = computegradientdescent(0.77,-0.0005,0.0001)

#plot graphs
print 'v values'
x = result.values()
y = f_.values()
print 'Start Value - 0.77'
print 'Learning Rate - 0.0005'
print len(x)
print len(y)

f_,f_x, result = computegradientdescent(0.77,-0.0001,0.0001)

#plot graphs
print 'v values'
x = result.values()
y = f_.values()
print 'Start Value - 0.77'
print 'Learning Rate - 0.0001'
print len(x)
print len(y)

f_,f_x, result = computegradientdescent(0.77,-0.00005,0.0001)

#plot graphs
print 'v values'
x = result.values()
y = f_.values()
print 'Start Value - 0.77'
print 'Learning Rate - 0.00005'
print len(x)
print len(y)

f_,f_x, result = computegradientdescent(0.77,-0.00001,0.0001)

#plot graphs
print 'v values'
x = result.values()
y = f_.values()
print 'Start Value - 0.77'
print 'Learning Rate - 0.00001'
print len(x)
print len(y)

#plot values iterations for 0.01, learning rates
x = [-.001,-0.0005,-0.0001,-0.00005,-0.00001]
y = [103,178,523,738,880]
plt.xlabel("Learning Rate")
plt.ylabel("Iterations Count")
plt.plot(x,y,'-o', color = 'g')
plt.title("Gradient Descent - Learning Rate vs Iterations, Start value 0.03")
plt.show()

#plot values iterations for 0.9, learning rates
x = [-.001,-0.0005,-0.0001,-0.00005,-0.00001]
y = [120,208,653,960,977]
plt.xlabel("Learning Rate")
plt.ylabel("Iterations Count")
plt.plot(x,y,'-o', color = 'g')
plt.title("Gradient Descent - Learning Rate vs Iterations, Start value 0.77")
plt.show()
