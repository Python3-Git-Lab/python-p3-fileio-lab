def write_file(file_name, file_content):
    #"""Write the given content to a new file with the specified name.\
    #If the file already exists, it will be overwritten.
    #filename can be a combined file_path/name
    #Example: "mydir/textfile.txt"
    with open(f'{file_name}.txt' , mode= 'w', encoding='utf-8') as textfile:
        textfile.write(file_content)
write_file('logfile' , 'This is a test content')

def append_file(file_name, append_content):
    #Append content to a file
    #The file and the content are the parameters

    with open(f'{file_name}.txt' , mode= 'a', encoding='utf-8') as logfile:
        logfile.write(append_content)
append_file("logfile" , "Log 2: 3 bananas subtracted")

def read_file(file_name):
    with open(f'{file_name}.txt' , mode= 'r', encoding='utf-8') as logfile:
        return logfile.read()
