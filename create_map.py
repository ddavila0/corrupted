import uproot

f = uproot.open("../files/test3_part.root")

tree = f["t3"]
branch_names = tree.keys()

table = dict()
for branch_name in branch_names:
    branch = tree[branch_name]
    num_baskets = branch.numbaskets
    entry_ranges = []
    for i in range(0, num_baskets):
        entry_start = branch.basket_entrystart(i)
        entry_stop  = branch.basket_entrystop(i)
        try:
            array_val = branch.array(entrystart= entry_start, entrystop= entry_stop)
        except:
            entry_ranges.append(3)
        else:
            if(len(array_val)==0):
                entry_ranges.append(2)
            else:
                entry_ranges.append(1)
    table[branch_name]=entry_ranges

for key in table:
    print(key+ " "+str(table[key]))
