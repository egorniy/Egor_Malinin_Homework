names=['dede frf vrf','dede ff rff']
def initials(name):
    l=name.split()
    return l[0] +' ' + l[1][0:1] + '. ' + l[2][0:1] + '.'
def initials_more(names):
    return [initials(name)for name in names]
print(initials_more(names))