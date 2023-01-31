# smtplib 用于邮件的发信动作
import smtplib
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 构建邮件头
from email.header import Header


# 发信方的信息：发信邮箱，QQ 邮箱授权码
from_addr = '22222@qq.com'
password = 'nimdvxdtsbvhbgbd'
# 收信方邮箱
to_addr = '111111@qq.com'
# 发信服务器
smtp_server = 'smtp.qq.com'

# 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码

text= '''
<style>.scrolling-wrapper{overflow-x:scroll;overflow-y:hidden;white-space:nowrap;padding:20px;}table{border-collapse:collapse;table-layout:fixed;border-radius:5px;overflow:hidden;margin:10px 5px;border:2px solid #70aefb;background-color:#328ef4;color:#c7dafb;box-shadow:10px 10px 10px #000;}table caption{background-color:#323232;padding:7px;font-size:21px;}table td,th{padding:5px;text-align:center;border:1px solid #70aefb;vertical-align:middle;font-size:15px;}</style>

张三，你好：<br />
&emsp;&emsp;以下是上月绩效考核及薪资组成，请查收！<br />

<div class="scrolling-wrapper">
  <table class="">
    <caption>2023年01月 绩效考核表</caption>
    <tr>
      <td>姓名</td>
      <td>考核基数</td>
      <td>工作时间投入度</td>
      <td>产出质量</td>
      <td>按期交付能力</td>
      <td>加权累计%</td>
      <td>姓名</td>
      <td>考核基数</td>
      <td>工作时间投入度</td>
      <td>产出质量</td>
      <td>按期交付能力</td>
      <td>加权累计%</td>
      <td>姓名</td>
      <td>考核基数</td>
      <td>工作时间投入度</td>
      <td>产出质量</td>
      <td>按期交付能力</td>
      <td>加权累计%</td>
      <td>姓名</td>
      <td>考核基数</td>
      <td>工作时间投入度</td>
      <td>产出质量</td>
      <td>按期交付能力</td>
      <td>加权累计%</td>
    </tr>
    <tr>
      <td>张三</td>
      <td>100%</td>
      <td>104%</td>
      <td>110%</td>
      <td>100%</td>
      <td>106%</td>
      <td>张三</td>
      <td>100%</td>
      <td>104%</td>
      <td>110%</td>
      <td>100%</td>
      <td>106%</td>
      <td>张三</td>
      <td>100%</td>
      <td>104%</td>
      <td>110%</td>
      <td>100%</td>
      <td>106%</td>
      <td>张三</td>
      <td>100%</td>
      <td>104%</td>
      <td>110%</td>
      <td>100%</td>
      <td>106%</td>
    </tr>
    <tr>
      <td colspan=6>时间：2023-02-11 15:34:24</td>
    </tr>
  </table>
</div>
以上数据如有疑问，请及时反馈！
'''

msg = MIMEText(text, 'html', 'utf-8')
# 邮件头信息
msg['From'] = Header('张三')  # 发送者
msg['To'] = Header('李四')  # 接收者
subject = 'Python SMTP 邮件测试'
msg['Subject'] = Header(subject, 'utf-8')  # 邮件主题

try:
    smtpobj = smtplib.SMTP_SSL(smtp_server)
    # 建立连接--qq邮箱服务和端口号（可百度查询）
    smtpobj.connect(smtp_server, 465)    
    # 登录--发送者账号和口令
    smtpobj.login(from_addr, password)   
    # 发送邮件
    smtpobj.sendmail(from_addr, to_addr, msg.as_string()) 
    print("邮件发送成功")
except smtplib.SMTPException:
    print("无法发送邮件")
finally:
    # 关闭服务器
    smtpobj.quit()

