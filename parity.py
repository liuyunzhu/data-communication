#parity.py
# use an even parity system to implement error detection

def paritycheck(message):
    paritybit = message[-1]
    parity = 0
    for i in range(0,len(message)-1):
        if message[i] == '1':
            parity = parity + 1

    if parity % 2 == int(paritybit):
        print("no error")
    else:
        print("transmission error")
        
paritycheck('10011')
