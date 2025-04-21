#Standardization
def standardization(a):
    mean = sum(a) / len(a)
    sum_ = sum([(x-mean)**2 for x in a])
    return [(i-mean)/(sum_ / len(a))**0.5 for i in a]