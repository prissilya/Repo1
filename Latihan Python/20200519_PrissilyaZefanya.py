def ascending(x):
    for i in range (len(x)):
        for j in range (i+1,len(x)):
            if x[i] > x[j]:
                x[i],x[j] = x[j],x[i]
    return x

def median (y):
    import math
    if len(y)%2 == 0:
        me_atas = math.ceil((len(y)+1)/2)
        me_bawah = math.floor((len(y)+1)/2)
        mean = (y[me_atas-1]+y[me_bawah-1])/2
    else:
        rumus = (len(y)+1)/2
        mean = y[int(rumus)-1]
    return mean

def modus (z):
    from collections import Counter
    n = len(z)
    data = Counter(z)
    get_mode = dict(data)
    modus = [k for k, v in get_mode.items() if v == max(list(data.values()))]
    if len(modus) == n:
        datamodus = 'No mode found'
    else:
        datamodus = 'Mode is / are : '+str(modus)
    return datamodus

def variance (o):
    total = 0
    ratarata = sum(o)/len(o)
    for i in o:
        kuadrat = (i-ratarata)**2
        total+=kuadrat
    var = total/len(o)
    return var

def stddev (p):
    import math
    deviasi = math.sqrt(variance(p))
    return deviasi

def skewness (q):
    totalskew = 0
    ratarata1 = sum(q)/len(q)
    for i in q:
        kubik = (i-ratarata1)**3
        totalskew+=kubik
    skewatas = totalskew/len(q)
    skewbawah = stddev(q)**3
    skew = skewatas/skewbawah
    return skew

def kurtosis (r):
    kurtatas = 0
    ratarata2 = sum(r)/len(r)
    for i in r:
        atas = (i-ratarata2)**4
        kurtatas += atas
    kurt = ((kurtatas/len(r))/(stddev(r)**4))
    # kiriatas = len(r)*(len(r)+1)
    # kiribawah = (len(r)-1)*(len(r)-2)*(len(r)-3)
    # kiri = kiriatas/kiribawah
    # tengah = totalkurt**4
    # kananatas = 3*((len(r)-1)**2)
    # kananbawah = (len(r)-2)*(len(r)-3)
    # kanan = kananatas/kananbawah
    # kurt = (kiri*totalkurt)-kanan
    return kurt

n = int(input('Masukkan jumlah angka dalam list : '))
a = []
for i in range (n):
    import random
    acak = random.randint(1,10)
    a.append(acak)
b = ascending(a)

print('List random kamu adalah : '+str(b))
print('Median dari list kamu adalah : '+str(median(b)))
print(modus(b))
print('Variance dari list kamu adalah : '+str(variance(b)))
print('Standar deviasi dari list kamu adalah : '+str(stddev(b)))
print('Skewness dari list kamu adalah : '+str(skewness(b)))
print('Kurtosis dari list kamu adalah : '+str(kurtosis(b)))
print('Set dari list kamu adalah : '+str(set(b)))