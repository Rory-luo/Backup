#发送邮件模块
import smtplib
#写邮件模块
import email
#定义邮件类型及内容
"""
邮件体为多组件类型（如果不是单一发送文本或者图片或者附件，那么就需要这个多组件类型将
其它元素打包进来）
"""
from email.mime.multipart import MIMEMultipart
#邮件中的文本信息
from email.mime.text import MIMEText
#邮件中的图片信息
from email.mime.image import MIMEImage
#定义邮件标题
from email.header import Header
#################################################################################################
#设置服务器所需信息
#邮件发送方邮箱地址
sender='2420039119@qq.com'
#这个是163邮箱里面POP3/SMTP开启后的授权码，一定注意不是163邮箱的登录密码
#第一次做的时候设置成邮箱登录密码反而邮件不能发送，改成授权码之后才可以
password='hqlonkoiesgqdiib'
#邮件接收方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers=['2863153168@qq.com']
###############################################################################################
#邮件基本信息输入
#设置总的邮件体对象，对象类型为mixed
mix_part=MIMEMultipart('mixed')
#发送者邮箱地址
mix_part['From']='Manager<2420039119@qq.com>'
#接收者邮箱地址
mix_part['To']='2863153168@qq.com'
#邮件标题
subject='网址文件即将删除提醒'
mix_part['subject']=Header(subject,'utf-8')
#################################################################################################
#构造文本内容，也就是邮件中正文部分的内容
"""
三个参数：
第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
"""
message_info='Happy New Year in 2021, \n\nThanks for visiting the Web,\n\nAnd the Web Will close at 2021/01/12 12:00 a.m.\n\nEnjoy your life!! See ya~\n\nMore Info: \nhttp://47.96.230.28/Xia \nhttp://47.96.230.28/夏子琛'
message=MIMEText(message_info,'plain','utf-8')
#通过多组件类型将文本内容打包进来
mix_part.attach(message)
###############################################################################################
#邮件中附件文本的构造
#设置附件文本的路径，除了改路径，其它几行代码基本不需要改动
##txt_path=r'C:\Users\Desktop\测试文件.pdf'
##txt_file = open(txt_path, 'rb').read()
##txt = MIMEText(txt_file, 'base64', 'utf-8')
##txt["Content-Type"] = 'application/octet-stream'
# 命名发送的附件名称
##txt.add_header('Content-Disposition', 'attachment', filename='测试报告.pdf')
#通过多组件类型将文本附件打包进来
##mix_part.attach(txt)
####################################################################################
# 邮件中图片附件的构造
#设置附件图片的路径，除了改路径，其它几行代码基本不需要改动
##image_path=r'C:\Users\Desktop\images\test.png'
##image_file = open(image_path, 'rb').read()
##image = MIMEImage(image_file)
##image.add_header('Content-ID', '<image1>')
#filename需要改成上传的图片名称
##image["Content-Disposition"] = 'attachment; filename="test.png"'
#通过多组件类型将图片附件打包进来
##mix_part.attach(image)
###################################################################################################
try:
   smtpObj=smtplib.SMTP('smtp.qq.com')
   smtpObj.login(sender,password)
   smtpObj.sendmail(sender,receivers,mix_part.as_string())
   smtpObj.quit()
   print('邮件发送成功')
except smtplib.SMTPException:
   print('Error:无法发送邮件')
