import random
def prn(*a,**k):
    try:

        if k['color']=='red':
            print(f"\x1b[{random.randint(0,8)};{30};{41}m",a,k ,'\x1b[0m')
        elif k['color']=='blue':
            print(f"\x1b[{random.randint(0,8)};{30};{44}m",a,k ,'\x1b[0m')
        elif k['color']=='green':
            print(f"\x1b[{random.randint(0,8)};{30};{42}m",a,k ,'\x1b[0m')
        elif k['color']=='yellow':
            print(f"\x1b[{random.randint(0,8)};{30};{43}m",a,k ,'\x1b[0m')
        elif k['color']=='pink':
            print(f"\x1b[{random.randint(0,8)};{30};{45}m",a,k ,'\x1b[0m')
        elif k['color']=='light_blue':
            print(f"\x1b[{random.randint(0,8)};{30};{46}m",a,k ,'\x1b[0m')
        elif k['color']=='white':
            print(f"\x1b[{random.randint(0,8)};{30};{47}m",a,k ,'\x1b[0m')
            print('worn')
    except:
        #print('\x1b[6;35;42m' + 'except!' + '\x1b[0m')
        print(f"\x1b[{random.randint(0,8)};{30};{random.randint(43,48)}m",a,k ,'\x1b[0m')

prn('d',2)
