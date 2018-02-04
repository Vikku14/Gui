import sys
from collections import OrderedDict
try:
    p = open(sys.argv[1],'r+')
    print(p.read())
except:
    print("file doesnt exists")
    print("we are creating the "+ sys.argv[1]+".......")
    p = open(sys.argv[1],'w')
finally:
    response = input("press e for edit\tpress q for quit\n")
    if response =='q':
        p.close()
    elif response == 'e':
        d= OrderedDict()
        i = 1
        ans0 = ""
        while True:
            d['ans'+ str(i)]= input("> ")
            if d['ans'+ str(i)] == ":sq":
                for item in d.values():
                    if item != ":sq":
                        p.writelines(item)
                        p.write("\n")

                p.close()
                break
            elif d['ans'+ str(i)] ==":!q":
                p.close()
                break
            else:
                i+=1

    else:
        print("wrong Input")
