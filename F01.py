import data

def login() :
    username = input("Username : ")
    password = input("Password : ")
    u_found = False
    p_found = False
    # iterate over the rows in the users list
    
    for i in range(1000):
        # check if the username and password match
        if username == data.users[i][0]:
            if password == data.users[i][1]:
                u_found = True  
                p_found = True
                data.login_status = "true"
                data.role = data.users[i][2]
                break
            else:
                u_found = True  
                p_found = False
                break
        i += 1

    if u_found == True and p_found == True :
        print(f"Selamat datang, {username}!")
        print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
    elif u_found == True and p_found == False :
        print("Password salah!")
    elif u_found == False :
        print("Username tidak terdaftar")
