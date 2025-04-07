from textblob import TextBlob
from deep_translator import GoogleTranslator
from colorama import Fore, Style, init

init(autoreset=True)

text = """手机短信是指通过移动通信网络发送的简短文本消息。手机短信通常由字母、数字和符号组成，
长度限制在70个字符以内。手机短信可以用于个人之间的交流，也可以用于商业营销、通知和提醒等目的。
手机短信的发送和接收通常需要使用移动电话或其他支持短信功能的设备。"""

translated_hi = GoogleTranslator(source='auto', target='hi').translate(text)
print(Fore.RED + translated_hi)

translated_or = GoogleTranslator(source='auto', target='or').translate(text)
print(Fore.YELLOW + translated_or)