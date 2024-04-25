al =['a','b','c','d','e','f','g','h','i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encrypt(lst,shift):
    sec = []   
    for i in lst:
        if i in al:
            inc = al[(al.index(i)+shift)%26]
            sec.append(inc)        
        else:
            sec.append(i)            
    print("Encoded message is","".join(sec))

def decrypt(lst,shift):
    newlst = []
    for i in lst:
        if i in al:
            dec = al[(al.index(i)-shift)%26]
            newlst.append(dec)
            
        else:
            newlst.append(i)
    print("Decoded message is:","".join(newlst))

while True:
    user = input("Type 'e' to encrypt  your message, or type 'd' to decrypt your message, 'x' to exit\n")
    if user=='x':
        break
    msg = input("Type your message here:\n").lower()
    lst = list(msg.lower())
    shift = int(input('Enter shift number:'))

    if user=="e":
        encrypt(lst,shift)
    elif user=="d":
        decrypt(lst,shift)
            




