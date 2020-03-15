""""Write the following city names sequentially to the file “sehir.txt” with plate sign belong to each.
cities=['Kayseri' ,'Istanbul', 'Izmir', 'Konya','Kars', 'Kastamonu',  'Kirklareli','Icel', 'Kirsehir', 'Kocaeli' ]"""
cities=['Kayseri','Istanbul','Izmir','Konya','Kars','Kastamonu', 'Kirklareli','Icel','Kirsehir','Kocaeli']
#We define cities list and we sort it
cities.sort()
plate=[33,34,35,36,37,38,39,40,41,42]  #We define sort of plate
z=zip(cities,plate)      #We use zip for finding plate of cities
file=open("sehir.txt","a") #We open a file
for li in z:     #We set for loop  for writeing all cities in file
    file.write("*li+\n")  #We write cities and their plates
file.close()    #We have to close file
