import matplotlib.pyplot as pyplot
def graph():
    year = [20171,20172,20181,20182,20191]
    Quyet = [2.2, 2.75,2.76,2.87,2.97]
    Truong = [2.65,1.82,2.83,2.5,3.11]
    Dat = [2,1.46,2.71,1.83,3.13]
    Dan = [1.69,2.43,2.45,2.23,3]
    pyplot.plot(year,Quyet, color = 'red',linestyle = '-', marker = 'o')
    pyplot.plot(year,Truong, color = 'blue',linestyle = '-', marker = 'o')
    pyplot.plot(year,Dat, color = 'green',linestyle = '-', marker = 'o')
    pyplot.plot(year,Dan, color = 'yellow',linestyle = '-', marker = 'o')
    pyplot.legend(["Quyet", "Truong", "Dat", "Dan"])
    pyplot.show()