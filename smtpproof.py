from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders as Encoders
import os

filepath = "/home/jz36/Документы/chess/bBishop.png"
basename = os.path.basename(filepath)
address = "neo@biksileev.ru"

# Compose attachment
part = MIMEBase('application', "octet-stream")
part.set_payload(open(filepath,"rb").read() )
Encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename)
part2 = MIMEText('how are you?', 'plain')

# Compose message
msg = MIMEMultipart()
msg['From'] = address
msg['To'] = 'texpomruu@yandex.ru'
msg['Subject'] = 'proof'

msg.attach(part2)
msg.attach(part)

# Send mail
smtp = SMTP_SSL()
smtp.connect('smtp.yandex.ru')
smtp.login(address, 'rjcjq12utybq')
smtp.sendmail(address, 'texpomruu@yandex.ru', msg.as_string())
smtp.quit()