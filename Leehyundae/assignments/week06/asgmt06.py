#Standardization
def standardization(a):
    sum_ = sum([(x-(sum(a) / len(a)))**2 for x in a])
    return [(i-(sum(a) / len(a)))/(sum_ / len(a))**0.5 for i in a]