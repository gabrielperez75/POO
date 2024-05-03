import random
import secrets
import string


# for _ in range(10):
#     long = random.randint(4,8)
#     cvu = ''.join(random.choice(string.digits)for _ in range(long))
#     print(cvu)
    
    
caracteres = string.ascii_letters + string.digits + string.hexdigits + string.punctuation  + string.ascii_uppercase

contrasenia = ''.join(secrets.choice(caracteres)for _ in range(18))

print(contrasenia)