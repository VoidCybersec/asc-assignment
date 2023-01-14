import bcrypt

# Hash a password
password = b"admin".encode("utf-8")
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password, salt)
print(salt)
# Check if a password is correct
password_to_check = b"mysecretpassword".encode("utf-8")
if bcrypt.checkpw(password_to_check, hashed_password):
    print("Password is correct")
else:
    print("Password is incorrect")
