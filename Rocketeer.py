#import schedule
import smtplib
import requests
from bs4 import BeautifulSoup
  
  
def LaunchReminder():
      
    # creating url and requests instance
    url = "https://spacecoastlaunches.com/launch-list/"
    html = requests.get(url).content
      
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')
    info = soup.find('div',attrs={'class':'three_fourth et_column_last'}).text

      
    # formatting data

    #smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        
    # start TLS for security
   #smtp_object.starttls()
        
    # Authentication

    subject = "Rocketeer Launch Reminder"
    body = f"Today the reminder is about {info}."
    msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nGeeksforGeeks".encode('utf-8')

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login('jaiswaljohn32@gmail.com', 'Abc@12345')
        server.sendmail("jaiswaljohn32@gmail.com","sarangjaiswal22@gmail.com", msg)
        server.close()
        print('successfully sent the mail')
    except:
        print("failed to send mail")

 
        
    # sending the mail
    #smtp_object.sendmail("jaiswaljohn32@gmail.com","sarangjaiswal22@gmail.com", msg)
        
    # terminating the session
    #smtp_object.quit()
    #print("Email Sent!")


# Every day at 06:00AM time LaunchReminder() is called.
#schedule.every().day.at("06:00").do(LaunchReminder)

#while True:
   # schedule.run_pending()