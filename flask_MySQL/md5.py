# import md5 # imports the md5 module to generate a hash
import hashlib
password = 'password'
# encrypt the password we provided as 32 character string
# hashed_password = md5.new(password).hexdigest()
hashed_password = hashlib.md5(password).hexdigest()
print hashed_password #this will show you the hashed value
# 5f4dcc3b5aa765d61d8327deb882cf99 -> nice!
