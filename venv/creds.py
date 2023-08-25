def get_creds():
    f = open("mod.txt","r");
    rno = f.readline()
    pas = f.readline().lstrip()
    crs = f.readline().lstrip()

    f.close()

    return rno,pas,crs
