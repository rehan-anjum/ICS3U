a = 'this is my string'
b = '.'
c = 0

# 17
# this
# t 
# is my 
# this is my string 
# False 
# This is my string 
# thXs Xs my strXng 
# 3
# 8
# ['this', 'is', 'my', 'string']
# **this is my string**
# t.h.i.s. .i.s. .m.y. .s.t.r.i.n.g
# THIS IS MY STRING

print(len(a))
print(a[c:5])
print(a[0])
print(a[5:10])
print(a)
print(a.__contains__('ign'))
print(a.capitalize())
print(a.replace('i','X'))
print(a.count('i'))
print(a.find('m'))
print(a.split(' '))
print(a.center(21, '*'))
print(b.join(a))
print(a.upper())