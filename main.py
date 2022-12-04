import json
import pynput
import time
import ctypes
import threading

# 处理windows系统对于坐标读取的误差问题
PROCESS_PER_MONITOR_DPI_AWARE = 2
ctypes.windll.shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)

mouse = pynput.mouse.Controller()
kb = pynput.keyboard.Controller()

addr_head = "https://lexiangla.com/teams/k100094/classes/8797cd0cd5a211ecbc8282db63562d97/courses/"
addr_tail = "?company_from=ac971426fdbc11e8b6e352540005f435"

opr_file = open("./data.json", 'r', encoding='utf-8')
log_file = open("./data.log", 'a', encoding='utf-8')
source = json.loads(opr_file.read())

opr_divid = 0.5

broswer_addr_cord = {
  'x': 265,
  'y': 65
}
play_icon_point = {
  'x': 555,
  'y': 555
}

def url_goto (url):
  mouse.position = (broswer_addr_cord['x'], broswer_addr_cord['y'])
  time.sleep(opr_divid)
  mouse.click(pynput.mouse.Button.left, 3)
  time.sleep(opr_divid)
  kb.type(addr_head + url + addr_tail)
  time.sleep(opr_divid)
  time.sleep(opr_divid)
  key_click(pynput.keyboard.Key.enter, 1)

def scroll_to_center ():
  key_click(pynput.keyboard.Key.up, 8)
  key_click(pynput.keyboard.Key.down, 8)

def key_click (key, times):
  while(times > 0):
    times = times - 1
    kb.press(key)
    kb.release(key)

def record_start():
  time.sleep(opr_divid)
  kb.press(pynput.keyboard.Key.alt)
  kb.press('1')
  kb.release(pynput.keyboard.Key.alt)
  kb.release('1')

def record_end():
  time.sleep(opr_divid)
  kb.press(pynput.keyboard.Key.alt)
  kb.press('2')
  kb.release(pynput.keyboard.Key.alt)
  kb.release('2')

def play_video ():
  mouse.position = (play_icon_point['x'], play_icon_point['y'])
  mouse.click(pynput.mouse.Button.left, 1)
  mouse.position = (150, 150)

def save_log (title):
  time_mark = time.ctime().split(' ')[4].replace(':', '')
  log_sign = time_mark + ' <==> ' + title + '\n'
  log_file.write(log_sign)

def record (item):
  time.sleep(5)
  print('loop start:', item['title'])
  url_goto(item['url']) # 跳转到视频地址
  time.sleep(10) # 等待网页渲染完毕
  scroll_to_center() # 把视频窗口滚动到录屏范围
  record_start() # 录屏器开始工作
  time.sleep(3) # 录屏器开始有3秒倒数
  play_video() # 开始播放视频
  time.sleep(eval(item['times'])) # 等待视频播放完毕
  record_end() # 结束录屏
  save_log(item['title']) # 记录录屏结束时间，并记录标题
  print('loop end:', item['title'])
  time.sleep(5) # 每次循环休息10秒

# thread = threading.Thread(target=record, args=(item,))
# thread.start()

def main (i):
  item = source[i]
  if item is not None:
    record(item)
    return main(i + 1)

# if __name__ == '__main__':
main(0)