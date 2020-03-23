import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_stata('C:/Users/林子晴/Desktop/dataset.dta')

df = df[df.taxeringsvrde > 0]
df = df[df.pris > 0]
df = df[df.taxr == 2006]
df = df[df.fakod == 1]
df = df.sort_values("kontraktsdatum", ascending=True)

month = df.groupby(df['month'])

year = df.groupby(df['year_nr'])


def get_year_price(i):
    return year.get_group(i)['pris']


def get_year_day(i):
    return year.get_group(i)['kontraktsdatum']


def get_day(k):
    return month.get_group(k)['day_nr']


def get_date(k):
    return month.get_group(k)['kontraktsdatum']


def get_pris(k):
    return month.get_group(k)['pris']


def get_tax(k):
    return month.get_group(k)['taxeringsvrde']


# (year) date v.s. price------------------
plt.scatter(get_year_day(2006), get_year_price(2006), sizes=[0.5])
plt.title("2006 date v.s. price")
new_ticks = np.linspace(0, 327, 5)
plt.xticks(new_ticks)
plt.xlabel("date")
plt.ylabel("price")
plt.ylim(0, 10000000)
plt.show()

plt.scatter(get_year_day(2007), get_year_price(2007), sizes=[0.5])
plt.title("2007 date v.s. price")
new_ticks = np.linspace(0, 340, 5)
plt.xticks(new_ticks)
plt.xlabel("date")
plt.ylabel("price")
plt.ylim(0, 10000000)
plt.show()

plt.scatter(get_year_day(2008), get_year_price(2008), sizes=[0.5])
plt.title("2008 date v.s. price")
new_ticks = np.linspace(0, 340, 5)
plt.xticks(new_ticks)
plt.xlabel("date")
plt.ylabel("price")
plt.ylim(0, 10000000)
plt.show()

# 2006 date v.s. price-----------------------------------------------------
plt.figure()
plt.subplot(3, 4, 1)
plt.scatter(get_day(13.0), get_pris(13.0), sizes=[1.3])
plt.title("January 2006")
plt.ylabel("price")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 2)
plt.scatter(get_day(14.0), get_pris(14.0), sizes=[1.3])
plt.title("February 2006")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 3)
plt.scatter(get_day(15.0), get_pris(15.0), sizes=[1.3])
plt.title("March 2006")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 4)
plt.scatter(get_day(16.0), get_pris(16.0), sizes=[1.3])
plt.title("April 2006")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 5)
plt.scatter(get_day(17.0), get_pris(17.0), sizes=[1.3])
plt.title("May 2006")
plt.ylabel("price")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 6)
plt.scatter(get_day(18.0), get_pris(18.0), sizes=[1.3])
plt.title("June 2006")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 7)
plt.scatter(get_day(19.0), get_pris(19.0), sizes=[1.3])
plt.title("July 2006")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 8)
plt.scatter(get_day(20.0), get_pris(20.0), sizes=[1.3])
plt.title("August 2006")
plt.ylim(0,10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 9)
plt.scatter(get_day(21.0), get_pris(21.0), sizes=[1.3])
plt.title("September 2006")
plt.xlabel("date")
plt.ylabel("price")
plt.ylim(0, 10000000)
plt.xlim(0, 32)

plt.subplot(3, 4, 10)
plt.scatter(get_day(22.0), get_pris(22.0), sizes=[1.3])
plt.title("October 2006")
plt.xlabel("date")
plt.ylim(0, 10000000)
plt.xlim(0, 32)

plt.subplot(3, 4, 11)
plt.scatter(get_day(23.0), get_pris(23.0), sizes=[1.3])
plt.title("November 2006")
plt.xlabel("date")
plt.ylim(0, 10000000)
plt.xlim(0, 32)

plt.subplot(3, 4, 12)
plt.scatter(get_day(24.0), get_pris(24.0), sizes=[1.3])
plt.title("December 2006")
plt.xlabel("date")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.show()

# 2007 date v.s. price------------------------------------------------------
plt.figure()
plt.subplot(3, 4, 1)
plt.scatter(get_day(25.0), get_pris(25.0), sizes=[1.3])
plt.title("January 2007")
plt.ylabel("price")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 2)
plt.scatter(get_day(26.0), get_pris(26.0), sizes=[1.3])
plt.title("February 2007")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 3)
plt.scatter(get_day(27.0), get_pris(27.0), sizes=[1.3])
plt.title("March 2007")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 4)
plt.scatter(get_day(28.0), get_pris(28.0), sizes=[1.3])
plt.title("April 2007")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 5)
plt.scatter(get_day(29.0), get_pris(29.0), sizes=[1.3])
plt.title("May 2007")
plt.ylabel("price")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 6)
plt.scatter(get_day(30.0), get_pris(30.0), sizes=[1.3])
plt.title("June 2007")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 7)
plt.scatter(get_day(31.0), get_pris(31.0), sizes=[1.3])
plt.title("July 2007")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 8)
plt.scatter(get_day(32.0), get_pris(32.0), sizes=[1.3])
plt.title("August 2007")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 9)
plt.scatter(get_day(33.0), get_pris(33.0), sizes=[1.3])
plt.title("September 2007")
plt.xlabel("date")
plt.ylabel("price")
plt.ylim(0, 10000000)
plt.xlim(0, 32)

plt.subplot(3, 4, 10)
plt.scatter(get_day(34.0), get_pris(34.0), sizes=[1.3])
plt.title("October 2007")
plt.xlabel("date")
plt.ylim(0, 10000000)
plt.xlim(0, 32)

plt.subplot(3, 4, 11)
plt.scatter(get_day(35.0), get_pris(35.0), sizes=[1.3])
plt.title("November 2007")
plt.xlabel("date")
plt.ylim(0, 10000000)
plt.xlim(0, 32)

plt.subplot(3, 4, 12)
plt.scatter(get_day(36.0), get_pris(36.0), sizes=[1.3])
plt.title("December 2007")
plt.xlabel("date")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.show()

# 2008 date v.s.price--------------------------------------------------
plt.figure()
plt.subplot(3, 4, 1)
plt.scatter(get_day(37.0), get_pris(37.0), sizes=[1.3])
plt.title("January 2008")
plt.ylabel("price")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 2)
plt.scatter(get_day(38.0), get_pris(38.0), sizes=[1.3])
plt.title("February 2008")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 3)
plt.scatter(get_day(39.0), get_pris(39.0), sizes=[1.3])
plt.title("March 2008")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 4)
plt.scatter(get_day(40.0), get_pris(40.0), sizes=[1.3])
plt.title("April 2008")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 5)
plt.scatter(get_day(41.0), get_pris(41.0), sizes=[1.3])
plt.title("May 2008")
plt.ylabel("price")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 6)
plt.scatter(get_day(42.0), get_pris(42.0), sizes=[1.3])
plt.title("June 2008")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 7)
plt.scatter(get_day(43.0), get_pris(43.0), sizes=[1.3])
plt.title("July 2008")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 8)
plt.scatter(get_day(44.0), get_pris(44.0), sizes=[1.3])
plt.title("August 2008")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.xticks([])

plt.subplot(3, 4, 9)
plt.scatter(get_day(45.0), get_pris(45.0), sizes=[1.3])
plt.title("September 2008")
plt.xlabel("date")
plt.ylabel("price")
plt.ylim(0, 10000000)
plt.xlim(0, 32)

plt.subplot(3, 4, 10)
plt.scatter(get_day(46.0), get_pris(46.0), sizes=[1.3])
plt.title("October 2008")
plt.xlabel("date")
plt.ylim(0, 10000000)
plt.xlim(0, 32)

plt.subplot(3, 4, 11)
plt.scatter(get_day(47.0), get_pris(47.0), sizes=[1.3])
plt.title("November 2008")
plt.xlabel("date")
plt.ylim(0, 10000000)
plt.xlim(0, 32)

plt.subplot(3, 4, 12)
plt.scatter(get_day(48.0), get_pris(48.0), sizes=[1.3])
plt.title("December 2008")
plt.xlabel("date")
plt.ylim(0, 10000000)
plt.xlim(0, 32)
plt.show()
