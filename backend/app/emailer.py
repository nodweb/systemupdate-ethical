import os
import smtplib
from email.message import EmailMessage
from typing import Optional


def _smtp_settings():
    host = os.getenv("SMTP_HOST")
    port = int(os.getenv("SMTP_PORT", "587"))
    user = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASS")
    use_tls = os.getenv("SMTP_USE_TLS", "true").lower() in ("1", "true", "yes")
    from_addr = os.getenv("EMAIL_FROM", user)
    to_addr = os.getenv("EMAIL_REPORT_TO")
    return host, port, user, password, use_tls, from_addr, to_addr


def send_email_report(subject: str, body: str) -> Optional[str]:
    host, port, user, password, use_tls, from_addr, to_addr = _smtp_settings()
    if not host or not to_addr:
        return "SMTP or recipient not configured"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_addr or user
    msg["To"] = to_addr
    msg.set_content(body)

    with smtplib.SMTP(host, port, timeout=10) as server:
        if use_tls:
            server.starttls()
        if user and password:
            server.login(user, password)
        server.send_message(msg)
    return None
