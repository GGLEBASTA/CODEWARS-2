def likes(names):
    count = 0
    for i in names:
        count = count + 1
        continue
    if (count == 0):
        m = "no one likes this"
        return m
    elif(count == 1):
        ddr = names[0]
        n = str(ddr) + ' '+ 'likes this'
        return n
    elif(count == 2):
        ddr = names[0]
        ddr1 = names[1]
        z = str(ddr) + ' '+ 'and' + ' '+ str(ddr1) + ' '+ 'like this'
        return z
    elif(count == 3):
        ddr = names[0]
        ddr1 = names[1]
        ddr2 = names[2]
        zz =  str(ddr)+','+' '+ str(ddr1) + ' '+ 'and' + ' '+ str(ddr2) + ' '+ 'others like this'
        return zz
    elif(count > 3):
        ddr = names[0]
        ddr1 = names[1]
        zzz = str(ddr)+','+' '+ str(ddr1) + ' '+ 'and' + ' '+ str(count-2) + ' '+'like this'
        return zzz


ss = likes(["Alex", "Jacob", "Mark", "Max"])
print(ss)