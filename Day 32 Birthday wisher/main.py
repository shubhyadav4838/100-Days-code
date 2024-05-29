import smtplib

password = ""
my_email = "shubhyadav753@gmail.com"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() #Transport Layer Security

    connection.login(user = my_email, password = password) #Login to the email account using a secure connection (TLS/SSL).
    connection.sendmail(
        from_addr = my_email, 
        to_addrs = "shubhyadav4838@gmail.com",
        msg="Subject:Hello\n\nThis is the body of my email")
    