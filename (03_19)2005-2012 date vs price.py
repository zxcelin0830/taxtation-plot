//testing
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_stata('C:/Users/user/Desktop/dataset.dta')
county = df["fakod"]
price = df["pris"]
date = df["kontraktsdatum"]
tax = df["taxeringsvrde"]
s_price = []
s_date = []
s_tax = []

for i in range(len(county)):
    if county[i] == 1:
        s_price.append(price[i])
        s_date.append(date[i])
        s_tax.append(tax[i])

data = sorted(zip(s_date, s_price, s_tax))

data_list = np.array(data).tolist()
year_list = []
for i in range(len(data_list)):
    year_list.append(data_list[i][0][:4])

year_code = []


def assign(args):
    for k in range(len(args)):
        if args[k] == '2005':
            year_code.append(0)
        elif args[k] == '2006':
            year_code.append(1)
        elif args[k] == '2007':
            year_code.append(2)
        elif args[k] == '2008':
            year_code.append(3)
        elif args[k] == '2009':
            year_code.append(4)
        elif args[k] == '2010':
            year_code.append(5)
        elif args[k] == '2011':
            year_code.append(6)
        elif args[k] == '2012':
            year_code.append(7)


assign(year_list)

year05 = []
price05 = []
tax05 = []
year06 = []
price06 = []
tax06 = []
year07 = []
price07 = []
tax07 = []
year08 = []
price08 = []
tax08 = []
year09 = []
price09 = []
tax09 = []
tax10 = []
year10 = []
price10 = []
tax11 = []
price11 = []
year11 = []
year12 = []
price12 = []
tax12 = []

for j in range(len(data_list)):
    if year_code[j] == 0:
        year05.append(data_list[j][0])
        price05.append(int(data_list[j][1]))
        tax05.append(int(data_list[j][2]))
    elif year_code[j] == 1:
        year06.append(data_list[j][0])
        price06.append(int(data_list[j][1]))
        tax06.append(int(data_list[j][2]))
    elif year_code[j] == 2:
        year07.append(data_list[j][0])
        price07.append(int(data_list[j][1]))
        tax07.append(int(data_list[j][2]))
    elif year_code[j] == 3:
        year08.append(data_list[j][0])
        price08.append(int(data_list[j][1]))
        tax08.append(int(data_list[j][2]))
    elif year_code[j] == 4:
        year09.append(data_list[j][0])
        price09.append(int(data_list[j][1]))
        tax09.append(int(data_list[j][2]))
    elif year_code[j] == 5:
        year10.append(data_list[j][0])
        price10.append(int(data_list[j][1]))
        tax10.append(int(data_list[j][2]))
    elif year_code[j] == 6:
        year11.append(data_list[j][0])
        price11.append(int(data_list[j][1]))
        tax11.append(int(data_list[j][2]))
    elif year_code[j] == 7:
        year12.append(data_list[j][0])
        price12.append(int(data_list[j][1]))
        tax12.append(int(data_list[j][2]))


plt.scatter(year05, price05, sizes=[1.3])
new_ticks = np.linspace(0, 2800, 6)
plt.xticks(new_ticks)
plt.scatter(year06, price06, sizes=[1.3])
plt.xticks(new_ticks)
plt.scatter(year07, price07, sizes=[1.3])
plt.xticks(new_ticks)
plt.scatter(year08, price08, sizes=[1.3])
plt.xticks(new_ticks)
plt.scatter(year09, price09, sizes=[1.3])
plt.xticks(new_ticks)
plt.scatter(year10, price10, sizes=[1.3])
plt.xticks(new_ticks)
plt.scatter(year11, price11, sizes=[1.3])
plt.xticks(new_ticks)
plt.scatter(year12, price12, sizes=[1.3])
plt.xlabel("date")
plt.ylabel("price")
plt.title("2005-2012 date vs price")
plt.show()










