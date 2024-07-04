# Arithmetic Operators
print("Arithmetic Operators")
n1 = 6
n2 = 9
print(n1+n2)
print(n1-n2)
print(n1*n2)
print(n1/n2)
print(n1%n2)
print(n1//n2)
print(n1**n2)

# Assignment Operators
print("Assignment Operators")
n1=2
n1+=3
print(n1)
n1=3
n1-=4
print(n1)
n1=4
n1*=5
print(n1)
n1=5
n1/=6
print(n1)
n1=7
n1//=8
print(n1)
n1=8
n1**=9
print(n1)

# Relational Operators
print("Relational Operators")
n1=65
n2=32
print(n1>n2)
print(n1<n2)
print(n1==n2)
print(n1!=n2)
print(n1>=n2)
print(n1<=n2)

# Logical Operators
print("Logical Operators")
x=5
print(x>3 and x<10)
print(x>3 or x<10)
print(not(x>3 and x<10))
print(not(x>6 and x<3))

# Membership Operators
print("Membership Operators")
ok_list = ["Vaibhav", "Hello", "World", "Hello World"]
print("Vaibhav" in ok_list)
print("yo" in ok_list)
print("Vaibhav" not in ok_list)

# Operators Precedence
print("Operators Precedence")
x=20
y=30
z=40
print(20+30*40) # Solves in the form of BODMAS: (20+30)*40
