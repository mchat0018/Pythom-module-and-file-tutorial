with open('test_file.txt','r') as f:
    #f_contents=f.read() reads all of the contents of the file into memory
    #f_lines=f.readlines()   returns a list of all the lines(each line ends with newline character)
    #f_nextLine=f.readline() returns the current line. If we assign again it will return the next line, and so on...
    
    #for line in f:  takes up lesser memory space than read() and readlines().
        #print(line,end=' ')

    #to control the amount of data from the file being read
    size_to_read=15 #no. of characters to be read in one chunk
    f_contents=f.read(size_to_read) #reads data chunk-by-chunk

    print(f.tell()) #prints the current position of the file read pointer

    while len(f_contents)>0:    #will loop until it reaches end of the file
        print(f_contents, end='-')
        f_contents=f.read(size_to_read)

    f.seek(0)   #sets the position of the read pointer 
    f_contents=f.read(size_to_read) 
    print(f_contents)


print(f.closed) #still have access to the file object, but it is closed (cannot be read from)

with open('test_file2.txt','w') as f: #will create a new file if doesn't exist, otherwise it will overwrite it
    f.write("Testing 1,2,3...\n") #writes all the data to the file
    f.seek(0)   #sets the write pointer to the start of the file
    f.write("R")    #Overwrites the first character

with open('test_file.txt','r') as rf:   #file to be read from...
    with open('test_file2.txt','a') as wf:  #file to be appended to...
        #for line in rf:
            #wf.write(line)
        wf.seek(0)
        chunk_size=15
        read_chunk=rf.read(chunk_size)

        while len(read_chunk)>0:
            wf.write(read_chunk)
            read_chunk=rf.read(chunk_size)

#use binary mode('rb','wb' etc for image file types)