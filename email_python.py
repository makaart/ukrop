import smtplib

fromaddr = 'artmak1990@gmail.com'
toaddrs  = 'makarov.artyom1@gmail.com'
msg = 'Mesagge to be reducted:'


# Credentials (if needed)
username = 'artmak1990@gmail.com'
password = '380951214135'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()