import smtplib
from info import from_email, to_email, password

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=from_email, password=password)
    connection.sendmail(from_addr=from_email,
                        to_addrs=to_email, 
                        msg="Subject: Am reusit\n\nBuna seara, vreau sa te anunt ca am reusit!")