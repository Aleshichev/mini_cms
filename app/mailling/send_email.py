from email.message import EmailMessage

import aiosmtplib


# from app.config import settings
async def send_email(
    recipient: str,
    subject: str,
    body: str,
):
    admin_email = "admin@site.com"
    message = EmailMessage()
    message["From"] = admin_email
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    await aiosmtplib.send(
        message,
        sender=admin_email,
        recipients=[recipient],
        hostname="maildev",
        port=1025,
    )
