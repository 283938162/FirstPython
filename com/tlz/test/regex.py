
import re
var = '欧文 阅读278,95次 '

var1 = '						国内世面上的下载工具，迅雷可谓一家独大，不过迅雷害怕步了快播的后尘，所以很多违规的资源并不敢再离线存放到自己的服务器。其他小众的下载工具...'

reg = r'\w+\d+\w'
pi = re.findall(reg,var)
print(var1)
print(var1.strip())
