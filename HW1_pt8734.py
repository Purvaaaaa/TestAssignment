# File Name: HW1_pt8734.py
# Programmer Name: Purva Tiwari (EID: pt8734)
# Problem Description: Create custom encryption function to convert plain text string into a ciphertext,
#                      encoding using custom encryption algorithm.
#
# Algorithm:
#   1. Convert input string to reverse order
#   2. Shift ASCII characters based on the value of N
#   3. Shifting direction left if D = -1 or shift right if D = 1
#   4. Print Encrypted string characters
###################################################################################################################
def reverse_string(str):
    string1 = ""
    for i in str:
        string1 = i + string1
    return string1

#TASK 1: Custom Encrption Function
def customEncrypt(user_id, password, N, D):
     reverse_user = reverse_string(user_id)
     reverse_pass=reverse_string(password)

     new_user=""
     new_pass=""
     for i in reverse_user:
         ascii_val = ord(i)
         if (D ==1):
             rev_char = (ascii_val + N)
         else:
             rev_char = (ascii_val - N)

         if (rev_char == 32) or (rev_char == 33):  #ASCII 32 = space and ASCII 33 = !
             rev_char = ascii_val
         new_user = new_user + chr(rev_char)

     for i in reverse_pass:
         ascii_val = ord(i)
         if (D == 1):
             rev_char = (ascii_val + N)
         else:
             rev_char = (ascii_val - N)
         if (rev_char == 32) or (rev_char == 33):
             rev_char = ascii_val
         new_pass = new_pass + chr(rev_char)

     return new_user, new_pass

#TASK 2: Test Custom Encrption function
def testCustomEncrypt():
    #read user ID
    while True:
        try:
            user=input("Enter UserID as text:")
            if (user.find(" ") != -1) or (user.find("!") != -1):
                raise NameError
        except NameError:
            print("Invalid input string, space and ! are now allowed.")
            print("try again!")
            continue
        else:
            break

    #password
    while True:
        try:
            password = input("Enter Password as text:")
            if (password.find(" ") != -1) or (password.find("!") != -1):
                raise NameError
        except NameError:
            print("Invalid input string, space and ! are now allowed.")
            print("try again!")
            continue
        else:
            break

    # input N
    while True:
        try:
            N = int(input("Enter value of N:"))
            if (N < 1):
                raise NameError
        except NameError:
            print("Invalid input N, N must integer and greater than or equal to 1.")
            print("try again!")
            continue
        else:
            break

        # input D
    while True:
        try:
            D = int(input("Enter value of D:"))
            if (D != -1) and (D != 1):
                raise NameError
        except NameError:
            print("Invalid input D, D must be +1 or -1.")
            print("try again!")
            continue
        else:
            break

    new_user, new_pass = customEncrypt(user, password, N, D)
    print("Encrypted user ID: ", new_user)
    print("Encrypted password: ", new_pass)

#main method
if __name__ == '__main__':
    testCustomEncrypt()


#TASK 3: Answeres:-
# Answer 1:
#
# Answer 2: