from hashlib import sha512
import crypt

def crackPass(shadow, user_hash, user_salt):
    passwords = open('password', 'r')
    for line in passwords.readlines():
        line = line.strip()
        cryptWord = crypt.crypt(line, '$6$' + user_salt)
        hashs = cryptWord.strip()
        try:
            if (hashs == shadow):
                print "[+] Found Password: [" + line + "]"
                return
        except:
            pass

    print "[-] Password Not Found"
    return

def main():
    shadowfile = open('shadowfile', 'r')
    for line in shadowfile.readlines():
        if ":"in line:
            user = line.split(':')[0]
            print "[*] Cracking Password For: " + user
            shadow = line.split(':')[1]
            try:
                user_salt = shadow.split('$')[2]
                #print user_salt
                user_hash = shadow.split('$')[3]
                #print user_hash
            except:
                continue
            crackPass(shadow, user_hash, user_salt)

if __name__ == "__main__":
    main()

