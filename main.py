# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def Testencryption(user_name, pass1):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {user_name}')  # Press Ctrl+F8 to toggle the breakpoint.
    new_user=''
    for i in user_name:
        x = ord(i)
        x = x + 3
        new_user = new_user + chr(x)

    print("old user=", user_name)
    print("new user=", new_user)
# Press the green button in the gutter to run the script.

if __name__ == '__main__':

    user1="ABCD"
    password1="hello"
    Testencryption(user1, password1)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
