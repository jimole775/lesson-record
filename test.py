import time
import json
# log_file = open("./data.log", 'a', encoding='utf-8')
# log_file.write('dasdasd\n')
# log_file.write('dasdasd\n')
print(eval("24 * 60 + 17") + 15)
time_mark = time.ctime().split(' ')[4].replace(':', '')
log_sign = time_mark + ' <==> ' + "dawdawd" + '\n'
print(log_sign)
opr_file = open("./data.json", 'r', encoding='utf-8')
log_file = open("./data.log", 'a', encoding='utf-8')
source = json.loads(opr_file.read())
for item in source:
  # save_log(item['title']) # 记录录屏结束时间，并记录标题
  print(eval(item['times']) + 5)
  time.sleep(1)
