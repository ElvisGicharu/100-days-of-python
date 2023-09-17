file_write= open('file1.txt','w')

def file_open(file_write):
    file_write.write('This is the new one\n')
    file_write.write("Today's\n")

file_open(file_write)
# file_write.close()


file_open=open('file1.txt','r')
# print(file_open.read())

file_append= open('file1.txt','a')
def append_fun(file_append):
    file_append.write('the girl is focused...nothing can distract the girl')
    
append_fun(file_append)
file_append.close()

# file_open=open('file1.txt','r')
print(file_open.read())
