from pathlib import Path 

files = []
path = Path('test-file.txt') # Change the path to have a file be created elewhere.

if (path.is_file()):
    for i in range(10000):
        files.append(open('test-file.txt', 'r'))
        print(i)
        
else:
    print("Creating File")
    f = open('test-file.txt', 'w')
    f.write("Testing File text")
    f.close()
    print("File Created")