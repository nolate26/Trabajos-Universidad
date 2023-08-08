import random
import string
l1 = random.choice(string.ascii_uppercase)
l2 = random.choice(string.ascii_uppercase)
l3 = random.choice(string.ascii_uppercase)
n1 = str(random.randint(0, 9))
n2 = str(random.randint(0, 9))
print(l1+l2+l3+n1+n2)
