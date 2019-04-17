def string_():
    str=open("SOLUTION.txt",'r')
    str1 = 'String com="'
    str2 = '";'
    str3 = str.readlines()
    str.close()
    str5 = ""
    for i in str3:
        str5 += i 
    str4 = str1+str5+str2
 #   print(str4)
    #print(str.readlines())
    in_ = open("test.h",'w')
    in_.writelines(str4)
    in_.close()
string_()
