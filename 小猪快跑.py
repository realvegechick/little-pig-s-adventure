import os
import sys

levels=['''墙墙墙墙墙墙墙墙
墙麦          墙
墙            墙
墙            墙
墙            墙
墙          赢墙
墙墙墙墙墙墙墙墙''','''墙墙墙墙墙墙墙墙
墙麦          墙
墙            墙
墙  转        墙
墙            墙
墙        墙赢墙
墙墙墙墙墙墙墙墙''','''墙墙墙墙墙墙墙墙墙
墙转          转墙
墙      墙      墙
墙麦    墙赢    墙 
墙  墙墙墙墙墙  墙
墙      墙      墙
墙      墙      墙
墙转          转墙
墙墙墙墙墙墙墙墙墙墙''','''墙墙墙墙墙墙墙墙墙
墙转      麦    墙
墙  墙墙墙墙墙墙墙
墙  墙转      转墙
墙  墙  墙墙墙  墙
墙  墙赢墙墙墙  墙
墙  墙墙墙墙墙  墙
墙转          转墙
墙墙墙墙墙墙墙墙墙'''
,'''墙墙墙墙墙墙墙
墙麦        墙
墙          墙
墙    转    墙
墙墙墙墙墙墙墙
墙墙墙墙墙墙墙
                赢''','''墙墙墙墙墙墙墙墙墙墙墙墙
墙麦            转转转墙
墙                    墙
墙                    墙
墙转转转              墙
墙墙墙墙墙墙墙墙墙墙墙墙
墙墙墙墙墙墙墙墙墙墙墙墙
墙                  赢墙
墙墙墙墙墙墙墙墙墙墙墙墙''','''墙墙墙墙墙      墙墙墙墙墙
墙赢转  墙墙    墙麦    墙
墙        墙墙墙墙      墙
墙墙                    墙
  墙      墙墙墙墙      墙
  墙墙墙  墙墙墙墙  转  墙
      墙  墙      墙墙墙墙
      墙  墙      墙  墙
      墙  墙      墙  墙
      墙  墙  墙  墙  墙
      墙      墙      墙
      墙      墙      墙
      墙      墙      墙
      墙墙墙墙墙墙墙墙墙''','''刺刺刺刺刺刺刺刺
刺            刺
刺麦      转  刺
刺            刺
刺  刺刺刺刺刺刺刺
刺              刺
刺      刺      刺
刺  转  刺      刺
刺      刺  赢  刺
刺刺刺刺刺刺刺刺刺''',
'''刺刺刺刺刺刺刺
刺麦        刺
刺          刺
刺          刺
刺  转      刺
刺刺墙刺刺刺刺
  刺  刺刺赢刺
  刺  刺刺  刺
  刺  刺刺  刺
  刺转    转刺
  刺刺刺刺刺刺''','''刺刺刺刺刺刺刺刺刺
刺麦    刺      刺
刺      转转    刺
刺      转转    刺
刺          刺赢刺
刺刺刺刺刺刺刺刺刺''','''墙墙墙墙墙墙墙墙
墙麦          墙          
墙坑坑坑      墙          
墙转          墙      
墙坑坑坑坑坑坑墙    
墙          赢墙
墙墙墙墙墙墙墙墙''','''墙墙墙墙墙墙墙墙
墙麦    坑赢坑墙          
墙      坑坑坑墙          
墙      坑坑坑墙      
墙      转坑坑墙    
墙      转坑坑墙
墙墙墙墙墙墙墙墙''',
'''墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙
墙摸墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙
墙  墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙
墙  墙墙墙墙墙墙墙墙墙  墙墙转坑墙转      转墙墙墙
墙  墙墙墙墙转    转墙  墙墙坑墙墙  墙墙墙  墙墙墙
墙  墙墙墙墙  墙墙转墙墙转墙  墙墙  墙墙墙  墙墙墙
墙  墙墙墙墙  墙墙  墙墙      墙墙转麦    转墙墙墙
墙  墙墙墙墙  墙墙  墙墙      墙墙  墙墙墙墙墙墙墙
墙        墙转    转墙墙      墙墙          墙墙墙
墙坑坑坑坑坑坑墙墙墙墙墙墙  墙墙墙墙墙墙墙墙墙墙墙''']
# ,'''墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙
# 墙              墙墙              墙
# 墙              墙墙              墙
# 墙      箱      墙墙      箱      墙
# 墙              墙墙              墙
# 墙麦            墙墙              墙
# 墙刺刺刺刺刺刺刺墙墙墙墙墙墙墙墙墙墙
# 墙刺刺刺刺刺刺刺墙墙墙墙墙墙墙墙墙墙
# 墙赢            墙墙              墙
# 墙              墙墙              墙
# 墙      箱      墙墙      箱      墙
# 墙              墙墙              墙
# 墙              墙墙              墙
# 墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙墙''']

hints=["麦小猪冲冲冲鸭！！！","麦小猪开始旋转！！！","麦小猪晕头转向！！！","麦小猪蜿蜒前行！！！","麦小猪破墙而出！！！","麦小猪势不可挡！！！","麦小猪舍近求远！！！","麦小猪小心尖刺！！！","麦小猪辗转腾挪！！！","麦小猪开动脑筋！！！","麦小猪路遇不平！！！","麦小猪注意脚下！！！","麦小猪陷入爱河！！！"]
# 获取单字符输入，根据平台选择对应实现
def get_key_linux():
    import termios
    import tty
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def get_key_windows():
    import msvcrt
    return msvcrt.getch().decode('utf-8')

if sys.platform == "win32":
    get_key = get_key_windows
else:
    get_key = get_key_linux

class Game:
    def __init__(self, height=15, width=30):
        self.end=False
        self.level=0
        self.original_name="麦小猪"
        self.height=height
        self.width=width
        self.is_vertical=False
        self.load_map(levels[self.level])

    def clear_screen(self):
        if sys.platform == "win32":
            os.system("cls")
        else:
            os.system("clear")

    def load_map(self, level):
        """
        从外部文件加载地图，文件中每一行代表地图的一行。
        空格将转换为"  "（空白单元），其他字符原样保存。
        """
        self.is_vertical=False
        self.name=self.original_name
        map_data = [["  "]*self.width]
        lines = level.split("\n")
        for line in lines:
            row = ["  "]
            idx=0
            while idx<len(line):
                ch=line[idx]
                if ch == "麦":
                    row.append("  ")
                    self.x=len(row)-1
                    self.y=len(map_data)
                elif ch == " ":
                    row.append("  ")
                    idx+=1
                else:
                    row.append(ch)
                idx+=1
            row+=["  "]*(self.width-len(row))
            map_data.append(row[:self.width])
            if len(map_data)==self.height:
                break
        for i in range(self.height-len(map_data)):
            map_data.append(["  "]*self.width)
        self.map_data=map_data


    def draw_map(self):
        """
        根据当前地图数据和玩家位置绘制地图：
         - 若玩家所在区域内有内容，则覆盖地图原有字符（不影响地图数据）
         - 玩家在横向排列时占据同一行连续3个单元，
           竖向排列时占据同一列连续3个单元。
        """
        out = ""
        for i in range(self.height):
            for j in range(self.width):
                # 判断该位置是否应显示玩家
                is_hero=False
                if self.end:
                    name_color='\033[101m\033[33m'
                else:
                    name_color='\033[33m'
                if self.is_vertical:
                    for k in range(3):
                        if (i == self.y + k and j == self.x):
                            if self.map_data[i][j]=="刺":
                                out += "\033[101m"
                            elif self.map_data[i][j]=="坑":
                                out += "\033[104m"
                            out += name_color+self.name[k]+"\033[0m"
                            is_hero=True
                else:
                    for k in range(3):
                        if (i == self.y and j == self.x + k):
                            if self.map_data[i][j]=="刺":
                                out += "\033[101m"
                            elif self.map_data[i][j]=="坑":
                                out += "\033[104m"
                            out += name_color+self.name[k]+"\033[0m"
                            is_hero=True
                if is_hero:
                    continue
                # 为字体上色
                if self.map_data[i][j]=="墙":
                    out += "\033[100m"+self.map_data[i][j]+"\033[0m"
                elif self.map_data[i][j]=="赢":
                    out += "\033[32m"+self.map_data[i][j]+"\033[0m"
                elif self.map_data[i][j]=="摸":
                    out += "\033[33m"+self.map_data[i][j]+"\033[0m"
                elif self.map_data[i][j]=="转":
                    out += "\033[96m"+self.map_data[i][j]+"\033[0m"
                elif self.map_data[i][j]=="刺":
                    out += "\033[41m\033[30m"+self.map_data[i][j]+"\033[0m"
                elif self.map_data[i][j]=="坑":
                    out += "\033[44m"+self.map_data[i][j]+"\033[0m"
                else:
                    out += self.map_data[i][j]
            out += "\n"
        return out

    def remove_obstacles(self):
        """旋转时清除‘麦小猪’所在区域的墙"""
        if self.is_vertical:
            for dy in range(3):
                if 0 <= self.y + dy < self.height and 0 <= self.x < self.width and self.map_data[self.y + dy][self.x] == "墙":
                    self.map_data[self.y + dy][self.x] = "  "
        else:
            for dx in range(3):
                if 0 <= self.y < self.height and 0 <= self.x + dx < self.width and self.map_data[self.y][self.x + dx] == "墙":
                    self.map_data[self.y][self.x + dx] = "  "

    def check_collision(self, new_y, new_x, target="墙"):
        """
        检测以 (new_y, new_x) 为左上角时，'麦小猪'所在区域是否发生碰撞：
        - target=="墙"：检查是否撞墙（包括超出边界）
        - target=="赢"：检测是否达到目标点
        - target=="转"：检测是否吃到道具T
        """
        if self.is_vertical:
            for dy in range(3):
                if new_y + dy < 0 or new_y + dy >= self.height or new_x < 0 or new_x >= self.width:
                    return True
                if self.map_data[new_y + dy][new_x] in target:
                    return True
        else:
            for dx in range(3):
                if new_x + dx < 0 or new_x + dx >= self.width or new_y < 0 or new_y >= self.height:
                    return True
                if self.map_data[new_y][new_x + dx] == target:
                    return True
        return False
    
    def check_cover(self, new_y, new_x, target="坑"):
        """
        检测以 (new_y, new_x) 为左上角时，'麦小猪'所在区域是否全为目标：
        - target=="坑"：摔死了
        """
        if self.is_vertical:
            for dy in range(3):
                if new_y + dy < 0 or new_y + dy >= self.height or new_x < 0 or new_x >= self.width:
                    return False
                if self.map_data[new_y + dy][new_x] != target:
                    return False
        else:
            for dx in range(3):
                if new_x + dx < 0 or new_x + dx >= self.width or new_y < 0 or new_y >= self.height:
                    return False
                if self.map_data[new_y][new_x + dx] != target:
                    return False
        return True

    def run(self):
        d_msg = hints[self.level]
        msg = d_msg
        while True:
            
            self.clear_screen()
            print(f"第{self.level+1}/{len(levels)}关")
            print(self.draw_map())
            print("wasd移动，q退出，r重来")
            print(msg)
            if msg != d_msg:
                msg = d_msg
                
            if self.check_collision(self.y, self.x, target="刺"):
                print("呜呜呜麦小猪被刺扎鼠了")
                input("按回车重来哦！")
                d_msg = hints[self.level]
                msg = d_msg
                self.load_map(levels[self.level])
                continue
            if self.check_cover(self.y, self.x, target="坑"):
                print("呜呜呜麦小猪掉进坑里摔鼠了")
                input("按回车重来哦！")
                d_msg = hints[self.level]
                msg = d_msg
                self.load_map(levels[self.level])
                continue
            
            while True:
                try:
                    key = get_key()
                    break
                except:
                    continue
            if key.lower() == 'q':
                break
            elif key.lower() == 'r':
                self.load_map(levels[self.level])
                continue

            # 根据按键计算候选新位置，并利用 check_collision 检测是否会撞墙
            if key.lower() == 'w':
                new_y, new_x = self.y - 1, self.x
            elif key.lower() == 's':
                new_y, new_x = self.y + 1, self.x
            elif key.lower() == 'a':
                new_y, new_x = self.y, self.x - 1
            elif key.lower() == 'd':
                new_y, new_x = self.y, self.x + 1
            else:
                continue

            if self.check_collision(new_y, new_x, "墙"):
                msg = "撞到墙了，痛痛QAQ"
            elif self.check_collision(new_y, new_x, "刺"):
                msg = "麦小猪才不往刺上撞！"
            elif self.check_collision(self.y, self.x, "坑")==False and self.check_collision(new_y, new_x, "坑"):
                msg = "麦小猪才不往坑里跳！"
            else:
                self.y = new_y
                self.x = new_x
             

            # 检测是否吃到道具T（利用 check_collision 检查 "转"）
            if self.check_collision(self.y, self.x, target="转"):
                msg = "麦小猪转起来啦！"
                if not self.is_vertical:
                    if self.map_data[self.y][self.x]=="转":
                        self.map_data[self.y][self.x]="  "
                    elif self.map_data[self.y][self.x+1]=="转":
                        self.map_data[self.y][self.x+1]="  "
                        self.y-=1
                        self.x+=1
                    elif self.map_data[self.y][self.x+2]=="转":
                        self.map_data[self.y][self.x+2]="  "
                        self.y-=2
                        self.x+=2
                else:
                    self.name=self.name[::-1]
                    if self.map_data[self.y][self.x]=="转":
                        self.map_data[self.y][self.x]="  "
                        self.x-=2
                    elif self.map_data[self.y+1][self.x]=="转":
                        self.map_data[self.y+1][self.x]="  "
                        self.y+=1
                        self.x-=1
                    elif self.map_data[self.y+2][self.x]=="转":
                        self.map_data[self.y+2][self.x]="  "
                        self.y+=2
                    
                self.is_vertical = not self.is_vertical
                self.remove_obstacles()
            
            

            # 检测是否达到目标点（利用 check_collision 检查 "赢"）
            if self.check_collision(self.y, self.x, target="赢"):
                self.clear_screen()
                print(f"第{self.level+1}/{len(levels)}关")
                print(self.draw_map())
                print("wasd移动，q退出，r重来")
                print("过关啦！")
                self.level+=1
                if self.level >= len(levels):
                    print("恭喜通关！你真是一只聪明的小猪！")
                    exit(0)
                input("按回车继续哦！")
                
                d_msg = hints[self.level]
                msg = d_msg
                self.load_map(levels[self.level])
            elif self.check_collision(self.y, self.x, target="摸"):
                # 增加一点通关的演出
                self.clear_screen()
                self.name="摸♥歪"
                self.end=True
                print(f"第{self.level+1}/{len(levels)}关")
                print(self.draw_map())
                print("wasd移动，q退出，r重来")
                print("过关啦！")
                self.level+=1
                if self.level >= len(levels):
                    print("从此，两头小猪过上了幸福的生活！")
                    exit(0)
                input("按回车继续哦！")
                
                d_msg = hints[self.level]
                msg = d_msg
                self.load_map(levels[self.level])

            

if __name__ == "__main__":
    game = Game()
    game.run()
