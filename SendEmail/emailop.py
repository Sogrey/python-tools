import smtplib
from email.mime.text import MIMEText
from email.header import Header


class EmailOP:
    def __init__(self, host, port, user, password):
        """
        host：邮件服务器地址
        port：邮件服务器端口
        user：自己邮箱账户名
        password：自己邮箱账户的密码（注意是授权码，不是邮箱官网的登录密码）
        """
        self.user = user
        self.password = password
        self.smtp = smtplib.SMTP()  # 创建 SMTP 对象
        self.smtp.connect(host=host, port=port)  # 链接到服务器
        self.smtp.login(user=self.user, password=self.password)  # 登录自己邮箱账号

    def send(self, From, To, Subject, Context, to_addrs):
        """
        Context：邮件正文
        From：发送者昵称（随便取）
        To：接收者昵称（随便取）
        Subject：邮件主题
        to_addrs: 收件人邮箱地址
        """
        message = MIMEText(Context, 'plain', 'utf-8')
#         message['From'] = Header(From, 'utf-8')
        message['From'] = Header(From)
#         message['To'] = Header(To, 'utf-8')
        message['To'] = Header(To)
#         message['Subject'] = Header(Subject, 'utf-8')
        message['Subject'] = Header(Subject)
        self.smtp.sendmail(from_addr=self.user, to_addrs=to_addrs, msg=message.as_string())

# 连接服务器并登录自己的邮箱账户
emailop = EmailOP(host="smtp.qq.com", port=465, user="408270653@qq.com", password="s0712090114S")
# 发送一封邮件
emailop.send(From="hyj", To="qq", Subject="test", Context="python test", to_addrs="408270653@qq.com")