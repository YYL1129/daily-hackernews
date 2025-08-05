import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail credentials
GMAIL_USER = 'zeusyee1247@gmail.com'
GMAIL_APP_PASSWORD = 'Arthur52425708$$@2307'
TO_EMAIL = 'zeusyee1247@gmail.com'

# Scrape headlines
def get_headlines():
    url = 'https://thehackernews.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.select('.body-post h2 a')[:10]

    headlines = []
    for article in articles:
        title = article.text.strip()
        link = article['href']
        headlines.append(f'<li><a href="{link}">{title}</a></li>')
    return '<ul>' + ''.join(headlines) + '</ul>'

# Send email
def send_email(content):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'Top 10 Hacker News Headlines'
    msg['From'] = GMAIL_USER
    msg['To'] = TO_EMAIL

    html = f"""\
    <html>
      <body>
        <h3>Top 10 Headlines from The Hacker News</h3>
        {content}
      </body>
    </html>
    """
    msg.attach(MIMEText(html, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
    server.sendmail(GMAIL_USER, TO_EMAIL, msg.as_string())
    server.quit()

# Run
if __name__ == '__main__':
    headlines_html = get_headlines()
    send_email(headlines_html)
