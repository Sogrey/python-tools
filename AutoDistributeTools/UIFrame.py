# -*- coding:utf-8 -*-
import os
import os.path
import datetime
import wx
from ui.MainFrame import MyFrame1

# pip install openpyxl
from openpyxl import load_workbook

# smtplib 用于邮件的发信动作
import smtplib
# email 用于构建邮件内容
from email.mime.text import MIMEText
# 构建邮件头
from email.header import Header

from configparser import ConfigParser

version = '1.0.2'

class UiFrame(MyFrame1):
    def __init__(self, parent):
        MyFrame1.__init__(self, parent)

        current_path = os.getcwd()
        # print(current_path)

        today = datetime.datetime.today()#today = datetime.datetime.today()
        year = today.year#2022
        month = today.month-1 # 上月
        if(today.month==1): # 去年12月
            year = year-1
            month = 12

        year_month = "{}年{}月".format(year,month)
        self.m_textCtrl6.SetValue(year_month)

        configPath= current_path + '/' + 'config.ini'

        if not os.path.exists(configPath):
 
            config_ini = open(configPath, 'w', encoding='utf-8')    
            # 注意如果是在WIN系统，在写入中文时，需要设置编码格式;如果不是WIN系统，则不需要设置编码格式
            
            config_ini.write('''
[Sender]
from_addr=
password=

[Excel]
JiXiaoSheetLabel=绩效表
GongZiSheetLabel=工资表
JiXiaoSheetHeaderLineNum=2
GongZiSheetHeaderLineNum=3

[Email]
EmailSubject={}工资条
            '''.format(year_month))
            config_ini.close()

        # 读取上次配置
        config_ini = ConfigParser()
        config_ini.read(configPath, encoding='utf-8')
        # print(config_ini.items("Sender"))  # 获取cmd节点下的所有键值对
        # print(config_ini.sections())  # 获取所有的节点
        # print(config_ini.get("Email", "EmailSubject"))  # 获取platformName的值

        self.m_textCtrl1.SetValue(config_ini.get("Sender", "from_addr"))
        self.m_textCtrl2.SetValue(config_ini.get("Sender", "password"))

        self.m_textCtrl3.SetValue(config_ini.get("Excel", "JiXiaoSheetLabel"))
        self.m_textCtrl4.SetValue(config_ini.get("Excel", "GongZiSheetLabel"))

        self.m_spinCtrl1.SetValue(config_ini.get("Excel", "JiXiaoSheetHeaderLineNum"))
        self.m_spinCtrl2.SetValue(config_ini.get("Excel", "GongZiSheetHeaderLineNum"))

        self.m_textCtrl7.SetValue(config_ini.get("Email", "EmailSubject"))

    def m_spinCtrl1OnSpinCtrlText( self, event ):
        lineNum = self.m_spinCtrl1.GetValue()
        self.m_staticText101.SetLabel("即从第{}行起读数据".format(lineNum+1))

    def m_spinCtrl2OnSpinCtrlText( self, event ):
        lineNum = self.m_spinCtrl2.GetValue()
        self.m_staticText11.SetLabel("即从第{}行起读数据".format(lineNum+1))

    def m_menuItem1OnMenuSelection( self, event ):
        wx.MessageBox('当前版本：'+version, '帮助',
            wx.OK | wx.ICON_INFORMATION)

    # 整理数据
    def OnStartDistributeEvent(self, event):

        try:

            # 获取文件路径
            excelPath = self.m_filePicker1.GetPath()  # 获取当前选中文件的路径
            if ("xls" in excelPath or "xlsx" in excelPath) == 0 or (not os.path.isfile(excelPath)):
                wx.MessageBox("路径错误", "提示", wx.ICON_ERROR)
                return
            # else:
            #     wx.MessageBox('输入成功!', "提示", wx.ICON_INFORMATION)
            #     event.Skip()

            # 读Excel文件

            # 加载Excel
            wb = load_workbook(excelPath, read_only=True, data_only=True)

            # 获取绩效表和工资表Sheet名称
            JXSheetLabel = self.m_textCtrl3.GetValue()
            GZSheetLabel = self.m_textCtrl4.GetValue()

            JXSheetHeaderLineNum = self.m_spinCtrl1.GetValue()
            GZSheetHeaderLineNum = self.m_spinCtrl2.GetValue()

            # 获取绩效工作簿
            ws_JX = wb[JXSheetLabel]

            # 绩效数据
            JX_datas = {}

            lineNum = 0
            colStart = 3
            colEnd = 10
            for row in ws_JX.rows:  # 获取每一行的数据
                if lineNum < int(JXSheetHeaderLineNum):
                    lineNum = lineNum+1
                    continue

                jx = []

                for index in range(colStart, colEnd, 1):
                    jx.append(row[index].value)

                JX_datas[row[3].value+row[9].value] = jx  # key: 名字+Email

            print('绩效表数据')
            print(JX_datas)

            # 获取薪资工作簿
            ws_GZ = wb[GZSheetLabel]

            # 工资数据
            GZ_datas = {}

            lineNum = 0
            colStart = 0
            colEnd = 47
            for row in ws_GZ.rows:  # 获取每一行的数据
                if lineNum < int(GZSheetHeaderLineNum):
                    lineNum = lineNum+1
                    continue

                gz = []

                for index in range(colStart, colEnd, 1):
                    gz.append(row[index].value)

                GZ_datas[row[2].value+row[46].value] = gz # key: 名字+Email

            print('工资表数据')
            print(GZ_datas)

            Comprehensive_data = {}

            keys_jx = []
            keys_gz = []
            for key in JX_datas.keys():
                keys_jx.append(key)
            for key in GZ_datas.keys():
                keys_gz.append(key)

            print(keys_jx)
            print(keys_gz)

            chaJi = list(set(keys_gz)-set(keys_jx))
            print(chaJi)
            
            for key in keys_jx:
                if key in keys_gz:
                    Comprehensive_data[key] = [JX_datas[key][0],JX_datas[key][6],JX_datas[key],GZ_datas[key]]
                else:
                    Comprehensive_data[key] = [JX_datas[key][0],JX_datas[key][6],JX_datas[key],[]]

            for key in chaJi:
                Comprehensive_data[key] = [GZ_datas[key][2],GZ_datas[key][46],[],GZ_datas[key]]

            print(Comprehensive_data)

            # 分发数据

            # 发件人
            from_addr = self.m_textCtrl1.GetValue()
            # 授权码
            password = self.m_textCtrl2.GetValue()
            # 邮件标题
            subject = self.m_textCtrl7.GetValue()

            config_ini = ConfigParser()
            config_ini.read("config.ini", encoding="utf-8")
            config_ini.set("Sender", "from_addr", from_addr)  # 修改数据            
            config_ini.set("Sender", "password", password)  # 修改数据  

            config_ini.set("Excel", "JiXiaoSheetLabel", JXSheetLabel)  # 修改数据
            config_ini.set("Excel", "GongZiSheetLabel", GZSheetLabel)  # 修改数据
            config_ini.set("Excel", "JiXiaoSheetHeaderLineNum", str(JXSheetHeaderLineNum))  # 修改数据
            config_ini.set("Excel", "GongZiSheetHeaderLineNum", str(GZSheetHeaderLineNum))  # 修改数据

            config_ini.set("Email", "EmailSubject", subject)  # 修改数据

            config_ini.write(open("config.ini", "w", encoding="utf-8"))

            SendEmail(from_addr, password, subject, Comprehensive_data, self)

        except OSError as reason:

            print('出错了T_T')
            print('出错原因是%s' % str(reason))

            self.m_staticText1.SetLabel('出错原因是%s' % str(reason))

# 分发数据
def SendEmail(from_addr, password, subject, Comprehensive_data, self):

    try:

        # 发信服务器
        smtp_server = 'smtp.qq.com'

        # 邮箱正文内容，第一个参数为内容，第二个参数为格式(plain 为纯文本)，第三个参数为编码

        css = '<style>.scrolling-wrapper{overflow-x:scroll;overflow-y:hidden;white-space:nowrap;padding:20px;}table{border-collapse:collapse;table-layout:fixed;border-radius:5px;overflow:hidden;margin:10px 5px;border:2px solid #70aefb;background-color:#328ef4;color:#c7dafb;box-shadow:10px 10px 10px #000;}table caption{background-color:#323232;padding:7px;font-size:21px;}table td,th{padding:5px;text-align:center;border:1px solid #70aefb;vertical-align:middle;font-size:15px;white-space: nowrap !important;}</style>'

        text="""
        {name}，你好：<br />
        &emsp;&emsp;以下是{date}绩效考核及薪资组成，请查收！<br />

        <div class="scrolling-wrapper">
        <table class="">
            <caption>{JX_Table_Header}</caption>
            <tr>
            <td>姓名</td>
            <td>考核基数</td>
            <td>工作时间投入度</td>
            <td>产出质量</td>
            <td>按期交付能力</td>
            <td>加权累计%</td>
            </tr>
            <tr>
            {JX_Table_Datas}
            </tr>
        </table>
        </div>
        <div class="scrolling-wrapper">
        <table class="">
            <caption>{GZ_Table_Header}</caption>
            <tr style="mso-height-source:userset;">
                <td rowspan="3">部门</td>
                <td rowspan="3">序号</td>
                <td rowspan="3">姓名</td>
                <td rowspan="3">出勤天数</td>
                <td rowspan="3">缺勤天数</td>
                <td rowspan="3">基本工资</td>
                <td rowspan="3">基本绩效</td>
                <td rowspan="3">绩效奖金</td>
                <td rowspan="3">缺勤扣工资</td>
                <td colspan="5">补助</td>
                <td rowspan="3">其他扣款</td>
                <td rowspan="3">应发工资</td>
                <td colspan="16">社保及公积金</td>
                <td rowspan="3">应税工资</td>
                <td colspan="8">专项扣除</td>
                <td rowspan="3">累计应缴预缴所得额</td>
                <td rowspan="3">累计税额</td>
                <td rowspan="3">本月应扣缴税额</td>
                <td rowspan="3">实发工资</td>
                <td rowspan="3">冲销后实发</td>
                <td rowspan="3">Email</td>
            </tr>
            <tr style="mso-height-source:userset;">
                <td rowspan="2">午餐补助</td>
                <td rowspan="2">其他各项补助</td>
                <td rowspan="2">社保及其他补助</td>
                <td rowspan="2">设备补助</td>
                <td rowspan="2">出差补助（加班、提成）</td>
                <td rowspan="2">养老保险基数</td>
                <td colspan="2">养老</td>
                <td rowspan="2">医疗基数</td>
                <td colspan="2">医疗</td>
                <td colspan="2">失业</td>
                <td >工伤</td>
                <td colspan="2">大病</td>
                <td rowspan="2">公积金基数</td>
                <td colspan="2">公积金</td>
                <td rowspan="2">个人合计</td>
                <td rowspan="2">公司合计</td>
                <td rowspan="2">子女教育</td>
                <td rowspan="2">赡养老人</td>
                <td rowspan="2">住房贷款</td>
                <td rowspan="2">房租费用</td>
                <td rowspan="2">继续教育</td>
                <td rowspan="2">大病医疗</td>
                <td rowspan="2">婴幼儿照护费用</td>
                <td rowspan="2">小计</td>
            </tr>
            <tr style="mso-height-source:userset;">
                <td >个人8%</td>
                <td >单位16%</td>
                <td >个人2%</td>
                <td >单位8%</td>
                <td >个人0.3%</td>
                <td >单位0.7%</td>
                <td >单位0.2%</td>
                <td >0.20<span style="mso-spacerun:yes;">&nbsp;</span></td>
                <td >0.80<span style="mso-spacerun:yes;">&nbsp;</span></td>
                <td >个人5%</td>
                <td >单位5%</td>
            </tr>
            <tr>
            {GZ_Table_Datas}
            </tr>
        </table>
        </div>
        以上数据如有疑问，请及时反馈！
        """

        date = self.m_textCtrl6.GetValue()

        smtpobj = smtplib.SMTP_SSL(smtp_server)
        # 建立连接--qq邮箱服务和端口号（可百度查询）
        smtpobj.connect(smtp_server, 465)    
        # 登录--发送者账号和口令
        smtpobj.login(from_addr, password)  

        count = 0
        total = len(Comprehensive_data)

        self.m_gauge1.SetRange(total)

        for key in Comprehensive_data.keys():

            to_name = Comprehensive_data[key][0]
            to_addr = Comprehensive_data[key][1]

            print(Comprehensive_data[key][2])

            jx= Comprehensive_data[key][2]
            gz= Comprehensive_data[key][3]

            gz_text_array = []

            for item in gz:
                gz_text_array.append("<td>{}</td>".format(item))

            gz_text = "".join(gz_text_array)

            content = text.format(name = to_name,date = date, JX_Table_Header = "{}绩效表".format(date), JX_Table_Datas = """
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            """.format(jx[0],
            str('%.2f' % (float(jx[1])*100))+'%',
            str('%.2f' % (float(jx[2])*100))+'%',
            str('%.2f' % (float(jx[3])*100))+'%',
            str('%.2f' % (float(jx[4])*100))+'%',
            str('%.2f' % (float(jx[5])*100))+'%'),
            GZ_Table_Header = "{}工资表".format(date),GZ_Table_Datas = gz_text)

            msg = MIMEText(css+content, 'html', 'utf-8')

            # 邮件头信息
            msg['From'] = Header(from_addr)  # 发送者
            msg['To'] = Header(to_addr)  # 接收者Email
            # subject = 'Python SMTP 邮件测试'
            msg['Subject'] = Header(subject, 'utf-8')  # 邮件主题

            try:
                # 发送邮件
                smtpobj.sendmail(from_addr, to_addr, msg.as_string()) 
                print("邮件发送成功")
                self.m_staticText1.SetLabel('分发到 %s (%s) 成功' % (str(to_name),str(to_addr)))

                count = count+1
                self.m_gauge1.SetValue(count)

            except smtplib.SMTPException as reason:
                print("无法发送邮件")
                self.m_staticText1.SetLabel('无法发送邮件 %s (%s) ,原因是：%s' % (str(to_name),str(to_addr),str(reason)))

        # 关闭服务器
        smtpobj.quit()

    except OSError as reason:

        print('出错了T_T')
        print('出错原因是%s' % str(reason))

        self.m_staticText1.SetLabel('出错原因是%s' % str(reason))
