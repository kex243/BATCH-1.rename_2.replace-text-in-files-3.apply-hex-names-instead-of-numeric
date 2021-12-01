import os

files = os.listdir("E:\gifs\outjson3 secret")

print (list_of_rows)
for x in range (0,3334):
    os.rename(str(list_of_rows[x][0]),'new'+str(list_of_rows[x][1])+'.gif')
