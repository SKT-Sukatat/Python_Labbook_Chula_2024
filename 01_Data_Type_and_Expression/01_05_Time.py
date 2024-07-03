import math

# Take time input for t1 and t2
h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

# Calculate seconds for t1 and t2
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2

# Calculate time differences based on second in a day
s_in_day = 24 * 60 * 60
dt  = (t2 - t1 + s_in_day) % (s_in_day)

# Calculate diff. hours, diff. minutes, diff. seconds
dh = dt // (60*60)
dt -= (dh*60*60)
dm = dt // 60
dt -= dm*60
ds = dt

#Print the result
print(str(dh) + ":" + str(dm) + ":" + str(ds))

