import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Gmail credentials
GMAIL_USER = 'zeusyee1247@gmail.com'
GMAIL_APP_PASSWORD = 'gydy ihxl bcmp kisr'
TO_EMAIL = 'zeusyee1247@gmail.com'

# Scrape headlines
def get_headlines():
    url = 'https://thehackernews.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', class_='story-link')[:10]

    headlines = []
    for article in articles:
        title_tag = article.find('h2')
        if title_tag:
            title = title_tag.text.strip()
            link = article['href']
            headlines.append(f'<li><a href="{link}">{title}</a></li>')
    
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
