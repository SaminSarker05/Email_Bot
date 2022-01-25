import smtplib

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.login("#############", "######")
    
    subject = "SPAM EMAIL"
    body = "It WORKS!"
    
    msg = f'Subject: {subject}\n\n{body}'
    
    x = 0;
    while x < 20:
        smtp.sendmail("#############", "#############", msg)