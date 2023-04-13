import data

def login() :
    username = input("Username : ") #meminta masukkan username
    password = input("Password : ") #meminta masukkan password
    data.usernamee = username
    account_found = False
    # iterate over the rows in the users list
    
    #mengecek apakah akun tersebut ada atau tidak, jika tidak, login gagal
    for i in range(1000):
        # check if the username and password match
        if username == data.users[i][0]:
            if password == data.users[i][1]:
                data.login_status = "true"
                data.role = data.users[i][2]
                account_found = True
                print(f"Selamat datang, {username}!")
                print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
                break
            else:
                account_found = True
                print("Password salah!")
                break
        else :
            account_found = False

    if account_found == False :
        print("Username tidak terdaftar")

    
