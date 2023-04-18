
#file=open("numbers.txt",'r') #r-read only mode
#lines=file.readlines()
#print(lines)
#
#for line in lines:
 #   if int(line) % 2==0:
  #      print(line.strip())
#file.close()

file=open("numbers.txt",'r') #r-read only mode
lines=file.readlines()

file_to_write=open("evens.txt",'w')

for line in lines:
    if int(line) % 2==0:
        file_to_write.write(line.strip())
        file_to_write.write("\n")
      
file.close()
file_to_write.close()

