import smtplib

my_email = "horinha04@gmail.com"
password = "senha única google"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="fhora93@gmail.com",
    msg="hello"
    )
connection.close()