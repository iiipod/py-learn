import crypt
import optparse

def crackPass(shadow, user_salt, dname):
    passwords = open(dname)
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
    parser = optparse.OptionParser(usage="Crack Linux shadow file encryptd by SHA-512" + '\n' + "Usage: crack_sha512 -d <dictfile> -f <shadowfile>")
    parser.add_option("-d", dest="dname", type="string")
    parser.add_option("-f", dest="fname", type="string")
    (options, args) = parser.parse_args()

    if (options.dname == None) | (options.fname == None):
        print(parser.usage)
        exit()
    else:
        dname = options.dname
        fname = options.fname

    shadowfile = open(fname)
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

            crackPass(shadow, user_salt, dname)

if __name__ == "__main__":
    main()
