

'''
replace
'''
s='http://shp.qpic.cn/ishow/2735012211/1516590356_84828260_8310_sProdImgNo_2.jpg/200'

ss=s.replace('/200','/0')

print(s)
print(ss)
print(s[:-3]+'0')