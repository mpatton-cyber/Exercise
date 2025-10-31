import matplotlib.pyplot as plt
def avg(ls):
    count=len(ls)
    total=0
    i=0
    for i in ls:
        total=total+i
    return total/count

def median(ls):
    idx_mid=int(len(ls)//2)
    return ls[idx_mid]

def prop_above(ls):
    above=[]
    for hour in ls:
        if hour > avg(ls):
            above.append(hour)
    total=len(ls)
    above_avg=len(above)/total
    return above_avg

def make_hist(counts, n_bins):
    plt.hist(counts, bins=n_bins)
    plt.title("My Histogram")
    plt.show()
        
try:
    fhand=open("StudentExercise.csv")
except:
    print("file not found")
    exit()
next (fhand)
ls=[]
for line in fhand:
    line=line.split(",")
    num=line[0]
    if num != '':
        ls.append(float(num))
ls.sort()
print("Median is:", median(ls))
print("Average is:", avg(ls))
print("Proportion above average is:", prop_above(ls))
print(make_hist(ls, 7))



    

    

    
    
