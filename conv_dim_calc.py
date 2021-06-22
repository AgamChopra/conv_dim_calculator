def calc_conv_dim():  
    in_sz = int(input('input size: '))
    p = int(input('padding: '))#0
    d = int(input('dialation: '))#1
    k = int(input('kernel: '))#3
    s = int(input('stride: '))#1
    tr = input('transpose?(Y/N): ')
    if tr in ['y','Y','Yes','yes','YES']:
        op = int(input('output padding: '))
        out_sz = int((in_sz-1)*s - (2*p) + (d*(k-1)) + op + 1)
    elif tr in ['n','N','no','No','NO']:
        out_sz = int(((in_sz + (2*p) - (d*(k-1))-1)/s) + 1)
    else:
        print('NO')
        return 0
    print('\n---OUTPUT---\noutput size =', out_sz)
    print('Δ =', abs(in_sz-out_sz))
    return 1

if __name__ == "__main__":
    flag = True
    while(flag):
        calc_conv_dim()
        temp = input('\nExit? ')
        if temp in ['y','Y','Yes','yes','YES']:
            flag = False
        elif temp not in ['n','N','no','No','NO']:
            print('NO')
            flag = False
