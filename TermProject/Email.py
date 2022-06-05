import Server as server
from tkinter import *
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Mail():
    # 메일 전송
    def sendMail(msg):
        import smtplib

        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()

        s.login(Mail.fromAddr, Mail.password)
        s.sendmail(Mail.fromAddr, Mail.toAddr, msg.as_string())
            
        s.close()

    # 메일 입력받기
    def inputMail():
        from typing import Iterable

        Mail.fromAddr = Mail.inputEmail.get()
        Mail.password = Mail.inputEmail2.get()
        # Mail.password = 'vzgshxkajhlygayw'
        Mail.toAddr = Mail.inputEmail3.get()

        msg = MIMEMultipart()
        msg['Subject'] = '병원 및 약국 정보' # 이메일 제목
        msg['From'] = Mail.fromAddr
        msg['To'] = Mail.toAddr

        interface1 = MIMEText("==============================병원정보==============================")
        interface2 = MIMEText("==============================약국정보==============================")
        msg.attach(interface1)

        # 병원정보 msg에 넣기
        if isinstance(Mail.hospitalList, Iterable):
            for hospital in Mail.hospitalList:
                name = MIMEText('병원 이름 : ' + hospital.yadmNm)
                cldNm = MIMEText('병원 종류 : ' + hospital.clCdNm)
                addr = MIMEText('병원 주소 : ' + hospital.addr)
                telno = MIMEText('병원 전화번호 : ' + hospital.telno + '\n')
                msg.attach(name)
                msg.attach(cldNm)
                msg.attach(addr)
                msg.attach(telno)
        else:
            name = MIMEText('병원 이름 : ' + Mail.hospitalList.yadmNm)
            cldNm = MIMEText('병원 종류 : ' + Mail.hospitalList.clCdNm)
            addr = MIMEText('병원 주소 : ' + Mail.hospitalList.addr)
            telno = MIMEText('병원 전화번호 : ' + Mail.hospitalList.telno + '\n')
            msg.attach(name)
            msg.attach(cldNm)
            msg.attach(addr)
            msg.attach(telno)

        # 약국정보 msg에 넣기
        if Mail.pharmacyList != []:
            msg.attach(interface2)
            for pharmacy in Mail.pharmacyList:
                name = MIMEText('약국 이름 : ' + pharmacy.yadmNm)
                addr = MIMEText('약국 주소 : ' + pharmacy.addr)
                telno = MIMEText('약국 전화번호 : ' + pharmacy.telno)
                distance = round(pharmacy.distance, 2)
                dis = MIMEText('병원으로부터 거리 : ' + str(distance) + 'm' + '\n')
                msg.attach(name)
                msg.attach(addr)
                msg.attach(telno)
                msg.attach(dis)


        Mail.sendMail(msg)

        server.puwindow.destroy()
        server.puwindow = None

    # X버튼 눌렀을 때
    def exit_popup():
        server.puwindow.destroy()
        server.puwindow = None

    # 팝업창
    def popupInput(hospitalList, pharmacyList):
        Mail.hospitalList = hospitalList
        Mail.pharmacyList = pharmacyList
        server.puwindow = Toplevel(server.window)
        server.puwindow.geometry("300x450")
        server.puwindow.title("이메일 정보 입력")

        frameMyEmailText = Frame(server.puwindow, padx=10, pady=25)
        frameMyEmail = Frame(server.puwindow, padx=10, pady=10)
        frameMyPasswText = Frame(server.puwindow, padx=10, pady=25)
        frameMyPassw = Frame(server.puwindow, padx=10, pady=10)
        frameToEmailText = Frame(server.puwindow, padx=10, pady=25)
        frameToEmail = Frame(server.puwindow, padx=10, pady=10)
        frameButton = Frame(server.puwindow, padx=10, pady=10)
        frameMyEmailText.pack(side='top', fill='x')
        frameMyEmail.pack(side='top', fill='x')
        frameMyPasswText.pack(side='top', fill='x')
        frameMyPassw.pack(side='top', fill='x')
        frameToEmailText.pack(side='top', fill='x')
        frameToEmail.pack(side='top', fill='x')
        frameButton.pack(side='bottom', fill='x')

        Label(frameMyEmailText, font=("나눔고딕코딩", 13), text='보낼 이메일 주소입력').pack(side='left')
        Mail.inputEmail = Entry(frameMyEmail, width=200)
        Mail.inputEmail.pack(fill='x', padx=10, expand=True)

        Label(frameMyPasswText, font=("나눔고딕코딩", 13), text='비밀번호 입력').pack(side='left')
        Mail.inputEmail2 = Entry(frameMyPassw, width=200, show='*')
        Mail.inputEmail2.pack(fill='x', padx=10, expand=True)

        Label(frameToEmailText, font=("나눔고딕코딩", 13), text='받을 이메일 주소입력').pack(side='left')
        Mail.inputEmail3 = Entry(frameToEmail, width=200)
        Mail.inputEmail3.pack(fill='x', padx=10, expand=True)

        Mail.btnOkay = Button(frameButton, text='확인', command=Mail.inputMail)
        Mail.btnOkay.pack(anchor='s', padx=10, pady=10)

        server.puwindow.protocol('WM_DELETE_WINDOW', Mail.exit_popup)

if __name__ == '__main__':
    Mail().sendMail(msg)