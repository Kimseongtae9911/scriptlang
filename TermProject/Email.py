from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mail():
    def sendMail(self):
        import smtplib

        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()

        s.login(self.fromAddr, [self.toAddr], self.msg.as_string())
        s.close()

    def inputMail(self):
        # gui상에서 입력받을 것
        # gui상에서 입력받은 것을 버튼을 누르면 sendInfo
        # 이 함수는 필요없을 것 같다
        # https://www.delftstack.com/ko/howto/python-tkinter/how-to-get-the-input-from-tkinter-text-box/
        self.fromAddr = input("본인 주소 입력: ")
        self.password = input("비밀번호 입력: ")
        self.toAddr = input("받는 사람 입력: ")
        self.msg['Subject'] = '병원 정보'
    
    def sendInfo(self, fromAddr, toAddr, password, msg):
        sendMail(fromAddr, toAddr, msg)