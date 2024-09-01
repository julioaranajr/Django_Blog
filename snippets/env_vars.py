import os

secret_key = os.environ.get('SECRET_KEY')
email_user = os.environ.get('EMAIL_USER')
email_pass = os.environ.get('EMAIL_PASS')
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')


print(secret_key)
print(email_user)
print(email_pass)
print(db_user)
print(db_password)
