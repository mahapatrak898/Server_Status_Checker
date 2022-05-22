import socket
import datetime
import time
import pickle
import socket
import smtplib

def is_running(site):
    """This function attempts to connect to the given server using a socket.
        Returns: Whether or not it was able to connect to the server."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((site, 80))
        return True
    except:
        return False

def log_report(log):
    file="logs.pkl"
    fileobj=open(file,'wb')
    pickle.dump(log,fileobj)
    fileobj.close()

def email(email,password,receiver):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.login(email,password)
    server.sendmail(email,receiver,"Server down at :"+str(datetime.datetime.now()))


if __name__ == '__main__':

    log = []

    site = input('Website to check: ')

    receiver= input('Enter the email you want to receive alerts in : ')
    Email = input('Enter your email : ')
    password = input ('Enter your password : ')
    
    while True:
        time.sleep(5)
        if is_running(f'{site}.com'):
            log.append(str(datetime.datetime.now())+": UP TIME")
            print(log)
        else:
            log_report(log)
            email(Email,password,receiver)