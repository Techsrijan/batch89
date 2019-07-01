import matplotlib.pyplot as plt
days = [1,2,3,4,5,6,7]
max_t = [54 ,35,45,33,27,50,39]
min_t = [56,55,34,44,45,65,20]
#plt.plot( days , max_t,"+b--",markersize='30' )
#plt.plot( days , max_t,"+r--",markersize='30' )
plt.plot( days , max_t, color='yellow',label='max')
plt.plot(days, min_t , color='black',label='min')
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather Information')
plt.legend(loc='best' ,shadow='true' ,fontsize='large')
plt.grid()
plt.savefig('weather.png')
plt.show()
