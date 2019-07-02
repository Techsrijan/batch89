import matplotlib.pyplot as plt
team =['INDIA','ENGLAND','PAKISHTAN', 'AUSTRALIA','NEW ZEALAND','SOUTH AFRICA', 'WEST INDIES', 'SRI LANKA', 'BANGLADESH','AFGHANISTAN']
points =[21 , 10 , 9 , 10 , 11 , 5, 3 , 6, 7,2]
plt.axis('equal')
plt.pie(points , labels=team ,radius=1.4,explode=[0.1,0,0,0,0,0,0,0,0,0],autopct='%0.2f%%')
plt.show()