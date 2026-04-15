#this file is responsible for input/output only
# all files should be called here rather than this file being called else 

from cli.banner3 import show_banner
def user_inp():
    user_input = input("Enter your statement:- ")
    print(user_input)
show_banner()
user_inp()