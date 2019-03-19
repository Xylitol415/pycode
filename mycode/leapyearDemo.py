"""
#print leap_years in a range
leaps = []
for year in range(2000,2050):
	if(year%4==0 and year%100 != 0) or (year%400==0):
		leaps.append(year)
print(leaps)
"""

leaps = [y for y in range(2000,2050) if(y%4 == 0 and y%100 != 0) or (y%400 == 0)]
print(leaps)