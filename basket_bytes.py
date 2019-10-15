import uproot

f = uproot.open("../files/test3_part.root")

tree = f["t3"]

branch = tree["ba"]
num_baskets = branch.numbaskets
# For each basket
for i in range(0, num_baskets):
    entry_start = branch.basket_entrystart(i)
    entry_stop  = branch.basket_entrystop(i)
    print("basket: "+str(i))
    print("starts: "+str(entry_start))
    print("stops: "+str(entry_stop))
    try:
        array_val = branch.array(entrystart= entry_start, entrystop= entry_stop)
    except:
        print("not found")
    else:
        if(len(array_val)==0):
            print("empty")
        else:
            print("found")
