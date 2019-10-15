import uproot

print("===================================================================")
print("=================Open =============================================")
print("===================================================================")
f = uproot.open("../files/test3_part.root")
#f = uproot.open("test2.root")

print("===================================================================")
print("==================Tree =============================================")
print("===================================================================")
tree = f["t3"]

print("===================================================================")
print("==================Branch===========================================")
print("===================================================================")
branch = tree["ba"]
num_baskets = branch.numbaskets

print("num baskets: "+str(num_baskets))
print("===================================================================")
print("===================================================================")

print("===================================================================")
print("=================Basket 0===========================================")
print("===================================================================")
entry_start = branch.basket_entrystart(0)
entry_stop  = branch.basket_entrystop(0)
array_val = branch.array(entrystart= entry_start, entrystop= entry_stop)

print("===================================================================")
print("=================Basket 1===========================================")
print("===================================================================")
entry_start = branch.basket_entrystart(1)
entry_stop  = branch.basket_entrystop(1)
array_val = branch.array(entrystart= entry_start, entrystop= entry_stop)

#f = uproot.open("../files/test3_part.root")

#tree = f["t1"]
#
#tree.numentries()
#branches = tree.keys()
#b = t["mynum"]
#num_baskets = b.numbaskets
#
