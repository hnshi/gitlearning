import os
import time
def main():
    content = '今天是个好日子......'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]
if __name__ =='__main__':
    main()
