# Import Modul
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def kirim_email(pengirim, penerima, subject, html_content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(pengirim,'rirw zfly cztc fuxz')

# Membuat project email
    msg = MIMEMultipart()
    msg['From'] = pengirim
    msg['To'] = penerima
    msg['Subject'] = subject

    msg.attach(MIMEText(html_content, 'html'))

    server.send_message(msg)
    server.quit()

html_template = """
<html>
<head>
    <title>Sistem Email Otomatis</title>
    <style>
       body {
       font-family: Arial, sans-serif;
       color:  #333;
       margin: 0;
       padding: 0;
       background-color: #f4f4f4;
       }
       .container {
         width: 100%;
         max-width: 600px;
         margin: 0 auto;
         background-color: #fff;
         padding: 20px;
         border-radius: 8px;
         box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
         border: 1px solid #ddd;
         }
         h1{
            font-size:: 24px;
            color: #333;
            margin-bottom: 10px;
            text-align: center;
        }
        hr{
          border: 0;
          border-top: 1px solid #ddd;
          margin: 20px 0;
        }
        p {
            font-size: 16px;
            line-height: 1.5;
            margin: 0 0 20px;
        }
        .button-container {
        text-align: center;
        margin-top: 20px ;
        }
        .button-container a {
        color: white;
        }
        .button{
            background-color: #6a0dad;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 16px;
            display: inline-block;
            }
        .button:hover {
         background-color: #5a0bb5;
        }
        .footer {
            font-size: 14px;
            text-align: center;
            margin-top: 20px;
            }
   </style>
</head>
<body>
  <div class="container">
    <h1>Mencoba Sistem email otomatis</h1>
    <p>ini adalah pengirim email otomatis menggunakan phyton ^^</p>
</body>
</html>
"""
pengirim = 'jslovveme@gmail.com'
penerima = 'sadiyah.rpl@gmail.com'
subject = 'silvia putri ramadani/34'
kirim_email(pengirim, penerima, subject, html_template)
print('Email berhasil terkirim!')