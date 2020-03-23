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
def get_year_tax(i):
    return year.get_group(i)['taxeringsvrde']
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


# (year) date v.s. tax------------------

plt.scatter(get_year_day(2006), get_year_tax(2006), sizes=[1.3])
plt.title("2006 date v.s. tax")
new_ticks = np.linspace(0, 350, 5)
plt.xticks(new_ticks)
plt.xlabel("date")
plt.ylabel("tax")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_year_day(2007), get_year_tax(2007), sizes=[1.3])
plt.title("2007 date v.s. tax")
new_ticks = np.linspace(0, 185, 5)
plt.xticks(new_ticks)
plt.xlabel("date")
plt.ylabel("tax")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_year_day(2008), get_year_tax(2008), sizes=[1.3])
plt.title("2008 date v.s. tax")
new_ticks = np.linspace(0, 350, 5)
plt.xticks(new_ticks)
plt.xlabel("date")
plt.ylabel("tax")
plt.ylim((0, 10000000))
plt.show()


# 2006 date v.s. price-----------------------------------------------------

plt.scatter(get_day(13.0), get_tax(13.0), sizes=[1.3])
plt.title("January 2006")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(14.0), get_tax(14.0), sizes=[1.3])
plt.title("February 2006")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(15.0), get_tax(15.0), sizes=[1.3])
plt.title("March 2006")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(16.0), get_pris(16.0), sizes=[1.3])
plt.title("April 2006")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(17.0), get_tax(17.0), sizes=[1.3])
plt.title("May 2006")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(18.0), get_tax(18.0), sizes=[1.3])
plt.title("June 2006")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(19.0), get_tax(19.0), sizes=[1.3])
plt.title("July 2006")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(20.0), get_tax(20.0), sizes=[1.3])
plt.title("August 2006")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(21.0), get_tax(21.0), sizes=[1.3])
plt.title("September 2006")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(22.0), get_tax(22.0), sizes=[1.3])
plt.title("October 2006")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(23.0), get_tax(23.0), sizes=[1.3])
plt.title("November 2006")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(24.0), get_tax(24.0), sizes=[1.3])
plt.title("December 2006")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

# 2007 date v.s. tax------------------------------------------------------

plt.scatter(get_day(25.0), get_tax(25.0), sizes=[1.3])
plt.title("January 2007")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(26.0), get_tax(26.0), sizes=[1.3])
plt.title("February 2007")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(27.0), get_tax(27.0), sizes=[1.3])
plt.title("March 2007")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(28.0), get_tax(28.0), sizes=[1.3])
plt.title("April 2007")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(29.0), get_tax(29.0), sizes=[1.3])
plt.title("May 2007")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(30.0), get_tax(30.0), sizes=[1.3])
plt.title("June 2007")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(31.0), get_tax(31.0), sizes=[1.3])
plt.title("July 2007")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(32.0), get_tax(32.0), sizes=[1.3])
plt.title("August 2007")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(33.0), get_tax(33.0), sizes=[1.3])
plt.title("September 2007")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(34.0), get_tax(34.0), sizes=[1.3])
plt.title("October 2007")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(35.0), get_tax(35.0), sizes=[1.3])
plt.title("November 2007")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(36.0), get_tax(36.0), sizes=[1.3])
plt.title("December 2007")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

# 2008 date v.s.tax--------------------------------------------------
plt.scatter(get_day(37.0), get_tax(37.0), sizes=[1.3])
plt.title("January 2008")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(38.0), get_tax(38.0), sizes=[1.3])
plt.title("February 2008")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(39.0), get_tax(39.0), sizes=[1.3])
plt.title("March 2008")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(40.0), get_tax(40.0), sizes=[1.3])
plt.title("April 2008")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(41.0), get_tax(41.0), sizes=[1.3])
plt.title("May 2008")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(42.0), get_tax(42.0), sizes=[1.3])
plt.title("June 2008")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(43.0), get_tax(43.0), sizes=[1.3])
plt.title("July 2008")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(44.0), get_tax(44.0), sizes=[1.3])
plt.title("August 2008")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(45.0), get_tax(45.0), sizes=[1.3])
plt.title("September 2008")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(46.0), get_tax(46.0), sizes=[1.3])
plt.title("October 2008")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(47.0), get_tax(47.0), sizes=[1.3])
plt.title("November 2008")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()

plt.scatter(get_day(48.0), get_tax(48.0), sizes=[1.3])
plt.title("December 2008")
plt.xlabel("date")
plt.ylabel("tax value")
plt.ylim((0, 10000000))
plt.show()
