import math
B = 101325 #大气压力Pa
v = 3 #空气流速
C = [-5674.5359,6.392547,-0.009677843,6.22157E-07,2.07478E-09,-9.48402E-12,4.1635019
    ,-5800.2206,1.3914993,-0.04860239,4.17648E-05,-1.44521E-08,6.5459673]
A = 0.00001*(65 + 6.75/v)
def tts():
    t = eval(input("干球温度为：")) 
    ts = eval(input("湿球温度为："))
    T = 273.15+t 
    Ts = 273.15+ts
    pqb = math.exp(C[7]/T + C[8] + C[9]*T + C[10]*pow(T,2) + C[11]*pow(T,3) + C[12]*math.log(T))
    # 饱和水蒸气分压力
    pqbs = math.exp(C[7]/Ts + C[8] + C[9]*Ts + C[10]*pow(Ts,2) + C[11]*pow(Ts,3) + C[12]*math.log(Ts))
    pq = pqbs - A*(t -ts)*B #湿空气水蒸气分压力
    fi = pq/pqb*100 # 相对湿度
    d = 0.622*pq/(B + pq) # 含湿量d,单位：kg/kg
    i = 1.01*t + d*(2501 + 1.84*t) #焓值，单位：kj/kg
    p = 0.00348*B/T - 0.00132*pq/T #密度，单位kg/m³
    v1 = 1/p #比容，单位：m³/kg
    tl = 8.22 +12.4*math.log(pq/1000) + 1.9*pow(math.log(pq/1000),2)
    print("含湿度量：{:.4}g/kg;焓值：{:.4}kj/kg;露点温度为：{:.4}℃,相对湿度：{:.4}%".format(d*1000,i,tl,fi))

def td():
    t = eval(input("干球温度为：")) 
    d = eval(input("含湿量为："))
    d=d/1000
    T = 273.15+t 
    pqb = math.exp(C[7]/T + C[8] + C[9]*T + C[10]*pow(T,2) + C[11]*pow(T,3) + C[12]*math.log(T))
    pq = B*d/(0.622+d)
    for i in range(200):
        Ts = i+273.15
        pqbs = math.exp(C[7]/Ts + C[8] + C[9]*Ts + C[10]*pow(Ts,2) + C[11]*pow(Ts,3) + C[12]*math.log(Ts))
        pqbs1 = A*(T - Ts)*B+pq
        if pqbs/pqbs1 < 1.05 and pqbs/pqbs1 > 0.95:
            pq = pqbs - A*(T-Ts)*B
            ts = Ts-273.15
    fi = pq/pqb*100
    i = 1.01*t + d*(2501 + 1.84*t)
    p = 0.00348*B/T - 0.00132*pq/T
    tl = 8.22 +12.4*math.log(pq/1000) + 1.9*pow(math.log(pq/1000),2)
    print("焓值：{:.4}kj/kg;露点温度为：{:.4}℃,相对湿度：{:.4}%;湿球温度：{:.4}".format(i,tl,fi,ts))

def ti():
    t = eval(input("干球温度为：")) 
    i = eval(input("焓值为："))
    T = 273.15+t 
    pqb = math.exp(C[7]/T + C[8] + C[9]*T + C[10]*pow(T,2) + C[11]*pow(T,3) + C[12]*math.log(T))
    d = (i -1.01*t)/(2501+1.84*t) #g/kg
    pq = B*d/(0.622+d)
    for i in range(200):
        Ts = i+273.15
        pqbs = math.exp(C[7]/Ts + C[8] + C[9]*Ts + C[10]*pow(Ts,2) + C[11]*pow(Ts,3) + C[12]*math.log(Ts))
        pqbs1 = A*(T - Ts)*B+pq
        if pqbs/pqbs1 < 1.05 and pqbs/pqbs1 > 0.95:
            pq = pqbs - A*(T-Ts)*B
            ts = Ts-273.15
    tl = 8.22 +12.4*math.log(pq/1000) + 1.9*pow(math.log(pq/1000),2)
    fi = pq/pqb*100
    p = 0.00348*B/T - 0.00132*pq/T
    print("含湿量：{:.4} g/kg;露点温度为：{:.4} ℃,相对湿度：{:.4} %;湿球温度：{:.4} ℃".format(d*1000,tl,fi,ts))

def tfi():
    t = eval(input("干球温度为：")) 
    fi = eval(input("相对湿度为："))
    T = 273.15+t 
    pqb = math.exp(C[7]/T + C[8] + C[9]*T + C[10]*pow(T,2) + C[11]*pow(T,3) + C[12]*math.log(T))
    pq = pqb*fi/100
    for i in range(200):
        Ts = i+273.15
        pqbs = math.exp(C[7]/Ts + C[8] + C[9]*Ts + C[10]*pow(Ts,2) + C[11]*pow(Ts,3) + C[12]*math.log(Ts))
        pqbs1 = A*(T - Ts)*B+pq
        if pqbs/pqbs1 < 1.05 and pqbs/pqbs1 > 0.95:
            pq = pqbs - A*(T-Ts)*B
            ts = Ts-273.15
    d = 0.622*pq/(B + pq)
    i = 1.01*t + d*(2501 + 1.84*t)
    tl = 8.22 +12.4*math.log(pq/1000) + 1.9*pow(math.log(pq/1000),2)
    p = 0.00348*B/T - 0.00132*pq/T
    print("含湿度量：{:.4} g/kg;焓值：{:.4} kj/kg;露点温度为：{:.4}℃,湿球温度：{:.4} ℃".format(d*1000,i,tl,ts))

def ttl():
    t = eval(input("干球温度为：")) 
    tl = eval(input("露点温度为："))
    T = 273.15+t 
    pqb = math.exp(C[7]/T + C[8] + C[9]*T + C[10]*pow(T,2) + C[11]*pow(T,3) + C[12]*math.log(T))
    if tl > 0 and tl < 65:
        pq = math.exp((-6.35+math.sqrt(9.71 + 4*tl))/2)
        for i in range(200):
            Ts = i+273.15
            pqbs = math.exp(C[7]/Ts + C[8] + C[9]*Ts + C[10]*pow(Ts,2) + C[11]*pow(Ts,3) + C[12]*math.log(Ts))
            pqbs1 = A*(T - Ts)*B+pq
            if pqbs/pqbs1 < 1.05 and pqbs/pqbs1 > 0.95:
                pq = pqbs - A*(T-Ts)*B
                ts = Ts-273.15
    fi = pq/pqb*100
    d = 0.622*pq/(B - pq)
    i = 1.01*t + d*(2501 + 1.84*t)
    print("含湿度量：{:.4} g/kg;焓值：{:.4} kj/kg;相对湿度为：{:.4} %,湿球温度：{:.4}℃".format(d*1000,i,fi,ts))
    
def ifi():
    i = eval(input("焓值为：")) 
    fi = eval(input("相对湿度为："))

def itl():
    i = eval(input("焓值：")) 
    tl = eval(input("露点温度："))

def itsd():
    i = eval(input("焓值：")) 
    ts = eval(input("湿球温度："))

def tstl():
    ts = eval(input("湿球温度：")) 
    tl = eval(input("露点温度："))

def tsfi():
    ts = eval(input("湿球温度：")) 
    fi = eval(input("相对湿度："))

def tlfi():
    tl = eval(input("露点温度：")) 
    fi = eval(input("相对湿度："))

def main():
    """print("请根据已知参数，选择对应的序号，在将已知参数数值输入即可获得其他状态参数结果\n\
    1、输入数字1代表已知干球温度、湿球温度\n\
    2、输入数字2代表已知干球温度、含湿量\n\
    3、输入数字3代表已知干球温度、焓值\n\
    4、输入数字4代表已知干球温度、相对湿度\n\
    5、输入数字5代表已知干球温度、露点温度\n\
    6、输入数字6代表已知焓值、相对湿度\n\
    7、输入数字7代表已知焓值、露点温度\n\
    8、输入数字8代表已知焓值、湿球温度\n\
    9、输入数字9代表已知湿球温度、露点温度\n\
    10、输入数字10代表已知湿球温度、相对湿度\n\
    11、输入数字11代表已知露点温度、相对湿度\n\
    q、输入q代表结束")"""
    while True:
        n = input("请输入数字选择需要求解的参数:")
        if n == "1":
            tts()
        elif n == "2":
            td()
        elif n == "3":
            ti()
        elif n == "4":
            tfi()
        elif n == "5":
            ttl()
        elif n == "q":
            break

main()
