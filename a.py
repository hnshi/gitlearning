# # Define new data to create
# import requests
# new_data = {
#     "userID": 1,
#     "id": 1,
#     "title": "Making a POST request",
#     "body": "This is the data we created."
# }

# # The API endpoint to communicate with
# url_post = "https://jsonplaceholder.typicode.com/posts"
# # url_post = "http://localhost:8080/posts"
# # A POST request to tthe API
# post_response = requests.post(url_post, json=new_data)

# # Print the response
# post_response_json = post_response.json()
# print(post_response_json)

# """
# {'userID': 1, 'id': 101, 'title': 'Making a POST request', 'body': 'This is the data we created.'}
# """
# # Print status code from original response (not JSON)
# from requests.auth import HTTPBasicAuth
# from requests.auth import HTTPBasicAuth
# private_url = "http://localhost:8080/user"
# github_username = "username"
# token = "token"

# private_url_response = requests.get(
#     url=private_url,
#     auth=HTTPBasicAuth(github_username, token)
# )

# private_url_response.status_code
# print(private_url_response.status_code)
# A deliberate typo is made in the endpoint "postz" instead of "posts"
# url = "https://jsonplaceholder.typicode.com/postz"

# # Attempt to GET data from provided endpoint
# try:
#     response = requests.get(url)
#     response.raise_for_status()
# # If the request fails (404) then print the error.
# except requests.exceptions.HTTPError as error:
#   print(error)
# import random 
# def generate_code(code_len):
#     all_chars='0123456789asdfghjklpoiuytrewqzxcvbnmASDFGHJKLPOIUYTREWQZXCVBNM~!@#$%^&*()'
#     last_pos = len(all_chars) - 1
#     code = ''
#     for _ in range(code_len):
#         index = random.randint(0,last_pos)
#         code += all_chars[index]
#     return code
# if __name__ == '__main__':
#     c = generate_code(6)
#     #括号内可自定义长度
#     print(c)
from time import sleep
import os


class Clock(object):
    """数字时钟"""
    _hour = 0
    _minute = 0
    _second = 0

    def __init__(self, hour=0, minute=0, second=0):
        """初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self._hour = hour
        self._minute = minute
        self._second = second

    def run(self):
        """走字"""
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0

    def show(self):
        """显示时间"""
        return '%02d:%02d:%02d' % \
               (self._hour, self._minute, self._second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        os.system('cls')
        print(clock.show())
        sleep(1)
        clock.run()


class People():
    sex = "girl"
    age = 20

    def __init__(self , sex:str , age:int):
        self.sex = sex
        self.age = age

    def say(self):
        print("hello.", self.sex,self.age)


class Child(People):
    def __init__(self, sex: str, age: int):
        super().__init__(sex, age)



if __name__ == '__main__':

    # shn = People(age = 27, sex = 'girl')
    # zyc = People('boy',32)
    # shn.say()
    # zyc.say()

    xh = Child("girl",2)
    xh.say()
    # main()