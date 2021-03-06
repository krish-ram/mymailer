#!/usr/bin/env python

import smtplib
 
def sendemail(from_addr, to_addr_list,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message
 
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems
 
sendemail(from_addr    = 'trilaciousexps@gmail.com', 
          to_addr_list = ['thoufeeq.mohd@gmail.com'],
          subject      = 'Email from Raspberry Pi', 
          message      = 'Hello, this is Raspberry Pi sending you this email....', 
          login        = 'trilaciousexps@gmail.com', 
          password     = 'experiments@tlabs')    
