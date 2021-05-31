import smtplib
import csv
from string import Template
import re

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import datetime
from email import encoders
import imaplib
import time


CREDENTIALS_USER ="bkumar4@internal.colt.net"
CREDENTIALS_PASS = "Password"
EMAIL_FROM_DEFAULT = "bhupender.kumar@colt.net"

EMAIL_SUBJECT = "Goodbye! Until we meet again... | अलविदा! फिर मिलेंगे..."
EMAIL_CC_DEFAULT = ""
EMAIL_BCC_DEFAULT = ""




# Set your Email Template here
def getEmailContent(first_name):
    email_content='';
    email_content ="""<!DOCTYPE html>

<head>

    <style>
   
        .body{
            color:white;
            padding: 2em !important;
            color:black

        }
        .space{
            margin-top:3px;
        }
        </style>
</head>
<script>

</script>

<body class="body">

Dear """ + first_name.capitalize() + """,<br><br>
As you might already know,31st May is my last day at work with COLT. <br><br>
It was not an easy decision to make because I truly enjoy working with you here at Colt.<br><br>
I would like to take this opportunity to thank you for your support and help, it has helped my career to blossom. I have learned a great deal from you and will miss your company.
It has been a great pleasure working with you.<br>
<br>
Regards,<br>
Bhupender Kumar<br>
<a href="https://linkedin.com/in/bhupender-sharma-51b7b0174/"><button>Linkedin</button></a><br>
<a href="mailto:sharmakbhupender@gmail.com"><button class="space">Gmail</button></a><br>
<a href="https://api.whatsapp.com/send?phone=+91-9717267473"><button class="space">Whatsapp</button></a><br>
</body>

</html>""";

    return email_content

# Loops your contacts list (csv file)
def loop_contacts(contacts):
    print('looping contacts')
        #name logic 
    username = contacts.split('@')[0]
    name = username.split('.')[0]
   
    # Set up the SMTP server
    print('Sending emails')
    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    s.starttls()
    s.login(CREDENTIALS_USER, CREDENTIALS_PASS)
    email = contacts
    msg = MIMEMultipart()
    print("Sending email to", name)
    msg['From']=EMAIL_FROM_DEFAULT
    msg['To']='sharmakbhupender@gmail.com'
    msg['Bcc'] = email
    msg['Subject']=  EMAIL_SUBJECT
    msg.attach(MIMEText(getEmailContent(name), 'html'))
    print(type(msg))
    s.send_message(msg)
    del msg
    s.quit()
arr=['madhvi.arora@colt.net',
'saurabh.arora@colt.net',
'mayur.bhagat@colt.net',
'hem.chandra@colt.net',
'jyothish.chandran1@colt.net',
'abhijit.dutta@colt.net',
'pradeep.gupta@colt.net',
'mudit.jain2@colt.net','Kiran.Vellanki@colt.net',
'girish.jally@colt.net',
'ashish.jaspal@colt.net',
'ashish.kaw@colt.net',
'ankush.khare@colt.net',
'bhupender.kumar@colt.net',
'dharmendra.kumar@colt.net',
'pawan.kumar2@colt.net',
'arunabha.mukhopadhyay@colt.net',
'ajit.pandey@colt.net',
'prabhat.pandey@colt.net',
'divya.pulikonda@colt.net',
'prasanna.ramamoorthy@colt.net',
'chintala.reddy@colt.net',
'lokesh.sahni@colt.net',
'shivangi.saxena@colt.net',
'somya.sharma@colt.net',
'dinesh.shaw@colt.net',
'angad.singh@colt.net',
'deovrat.singh@colt.net',
'srishti.srivastava@colt.net',
'satyavan.yadav@colt.net',
'anshul.bansal@colt.net',
'shailesh.goel1@colt.net',
'praveen.kumar@colt.net',
'santhosh.kumare@colt.net',
'madanbasoor.mahadevan@colt.net',
'satish.sharma2@colt.net',
'diksharatan.sharma@colt.net',
'avishka.agarwal@colt.net',
'ankita.bansal2@colt.net',
'mahesh.bhakuni@colt.net',
'surya.bhushan@colt.net',
'arya.gairola@colt.net',
'gaurangi.gaurangi@colt.net',
'vibhash.jain@colt.net',
'madhavan.kv@colt.net',
'janardan.mondal@colt.net',
'sekar.palaniyappan@colt.net',
'divya.poda2@colt.net',
'kishan.sahu@colt.net',
'selvaraja.savarimuthu@colt.net',
'eliza.sethi@colt.net',
'shubham.shukla@colt.net',
'ragubir.singh@colt.net',
'alok.verma@colt.net',
'vipul.verma@colt.net',
'chaitra.lakshminarayan@colt.net',
'pylyp.fomyn@colt.net',
'andre.antunes@colt.net',
'shyama.alfred@colt.net',
'wolfgang.martin@colt.net',
'galaxy.gupta@colt.net',
'satheesh.kumarcinnasamy@colt.net',
'chetana.nt@colt.net',
'alagappan.ramasamy@colt.net',
'richa.sharma3@colt.net',
'ramniwas.khod4@gmail.com',
'ramniwasiitb@gmail.com', 'kaur.sarbpreet@gmail.com','Harshitgoel96@yahoo.com','mdshahbaz310@gmail.com','amankgupta92@gmail.com','abhishek.oct20@hotmail.com',]
temp =['rajus9231@gmail.com','sharmakbhupender@gmail.com','bhupender.kumar@colt.net'];

for name in temp:
    loop_contacts(name)