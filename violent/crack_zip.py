import zipfile
import optparse
from threading import Thread

def extractall(zfile, password):
    for line in password.readlines():
        password = line.strip()
        try:
            zfile.extractall(pwd=password)
            print '[+] password = ' + password + "\n"
            return
        except:
            pass

    print '[-] password not found'
    return

def main():
    parser = optparse.OptionParser("Zip file password cracker" + "\n" + "usage:crack_zip.py -d <dict> -f <zipfile>")
    parser.add_option("-d", dest="zdict", type='string')
    parser.add_option("-f", dest="zfile", type='string')
    (options, args) = parser.parse_args()

    if (options.zdict == None) | (options.zfile == None):
        print parser.usage
        exit(0)

    else:
        zfile = options.zfile
        zdict = options.zdict

    zfile = zipfile.ZipFile(zfile)
    passfile = open(zdict)
    t = Thread(target=extractall, args=(zfile, passfile))
    t.start()

if __name__ == '__main__':
    main()


