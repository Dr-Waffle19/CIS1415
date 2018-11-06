def main ():
    rainfall = rainInput ()
    totalRain = totalRainfall (rainfall)
    average_Rainfall = averageRainfall (totalRain)
    highestMonth, highestMonthly = highestMonthNumber (rainfall)
    print ()#for spacing output
    print ('Total rainfall for the year: +str(totalRain) + ' inche(s)')
    print ()#for spacing output
    print ('Average rainfall for the year: ' +str(average_Rainfall) +\
          ' inche(s)') 
    print ()#for spacing in output
    print ('Highest amount of rain', highestMonthly, 'in' , highestMonth
def highestMonthNumber (rainfall):
    month = ['January','Febuary','March','April','May','June','July','August'\
                ,'September','October','November','December']
    highestMonthly = 0
    for m, n in enumerate(rainfall):
        if n > highestMonthly:
            highestMonthly = n
            highestMonth = m
    return month[highestMonth], highestMonthly
