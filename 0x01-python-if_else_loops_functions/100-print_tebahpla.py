
#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        flag = 0
    else:
        flag = 32
    print('{}'.format(chr(i - flag)), end='')
