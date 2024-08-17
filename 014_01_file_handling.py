# what is a file?
# file is a named location on disk to store information. It is used to store data permanentaly in non-volatile memory(eg: hard disk).

# the order in which file order take place 
# 1. Open file
# 2. Read or Write (perform operations)
# 3. Close file

# How to open a file?
# Python has a built-in finction to open a file named as open(). This function return a file object.

# I can specify the mode while opening a file. In mode, i specify weather i want to read 'r' , write 'w' or append 'a' to the file.
# I can also specify that i want to open it in text mode or in binary code.
# I can also use statement instead of open() and close():
# with open(`file_name.txt`, 'w') as fileObject:


# 1st the way in which i can access file is: 
file = open('014_02_data.txt', 'r') # vaise by default read he hota hai.
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# now yeh ik bhout long process hai so loop ka use kro
for line in file:
    print(line)

# 1st ko use krne m ik problem hai for example file[14] agr toh present hai so in that case koi problem nhi hoge and program complete hone k baad file close. 
# but what happens if file[14] ho he na so in that case file toh kbhi close he na hoge?  

file.close()

# 2nd way which is better than previous as it solve the problem stated in line 30 and 31:
with open('014_02_data.txt') as f:
    print("the best way to perform read and write operations \n")
    for line in f:
        print(line)

# now let's see some other function which can be performed on files are:
        f.read() # use to read the entire file
        f.read(21) # ab bss starting k 21 characters he read kre jiye ge
        # now ab agr m fir se 
        f.read(21) # ka use kru toh mko next 21 words mile gee because yeh file reading in python by default ik cursor lekr chalta hai and as in line 43 the first '21' character ko read kra and vaha stop and again 45 line m use krne pr apne ko previous position se he reading start kre ga.
        # and agr, i want my cursor to its initial position then just use
        f.seek(0) # 0 se initial position pr gya hai. agr kisi aur position pr send krne hai toh just change the indexing.


# now it's time to see how to perform write operation in the file

# syntax:
# 1. fileObject.write(string)
# 2. fileObject.writelines(sequences)

list = ['Mera\n','goal\n','hai\n','vapas\n','se\n','Godlike Great Emperor\n','ki position\n','vapas lena.\n']

with open('014_03_write_file.txt', 'w') as w:
    w.write('Namaste M Devsa Samrat hu \n') # for single write operation
    w.writelines(list)
    
      now ab yeh sara data 014_03_write_file.txt m save ho chuka hai