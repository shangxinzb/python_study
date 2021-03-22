"""
研究一下smtplib
"""

import smtplib


s = smtplib.SMTP()
s.connect('smtp.qq.com', 25)
print(s.help())