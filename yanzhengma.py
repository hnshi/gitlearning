import random 
def generate_code(code_len):
    all_chars='0123456789asdfghjklpoiuytrewqzxcvbnmASDFGHJKLPOIUYTREWQZXCVBNM~!@#$%^&*()'
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = random.randint(0,last_pos)
        code += all_chars[index]
    return code
if __name__ == '__main__':
    c = generate_code(6)
    #括号内可自定义长度
    print(c)