# This use a file stream object to append information ai text to a file
# There are other mode such as (r,w,a,x,b)
# r = read(default)
# w = write
# a = append
# x = read and write
# b = binary


stream = open('todos.txt', 'a')
print('Put out the trash.',file=stream)
print('Feed the cow',file=stream)
print('Prepare tax return',file=stream)
file.close()
tsk = open('todos.txt')
for i in tsk:
    print(i, end="")

# OR
# with statement uses CMP content management protocol to make sure that you use close once your done with your streams.
with open('todos.txt', 'a') as stream:
    for x in stream:
        print(x, end="")
