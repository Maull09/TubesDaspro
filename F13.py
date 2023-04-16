import os
import save

def reload(folder_name,file_name, var, jk):
    file_path = os.path.join(folder_name, file_name)
    var = loading(file_path, var, jk)

def loading(file,var,jk):
    with open(file) as f :
        raw_lines = f.readlines()
        lines = []
        for i in range(save.length(raw_lines)):
            if i < save.length(raw_lines):
                lines += [save.strip_enter(raw_lines[i])]
        j = 0
        for line in lines:
            data = ""
            k = 0
            for i in range(save.length(line)):
                if line[i] == ';':
                    # jika bertemu ';' yang terdapat pada csv maka data akan ditambahkan ke arr
                    if k < jk:  # pastikan nilai k tidak melebihi jumlah kolom
                        var[j][k] = data
                        k += 1
                        data = ""
                    else:  # jika k sudah melebihi jumlah kolom, atur kembali ke 0
                        k = 0
                elif (i == save.length(line) - 1):
                    # menambahkan data yang paling belakang untuk ditambahkan ke arr
                    var[j][k] = data + line[i]
                else:
                    data += line[i]
            j += 1                
        return var


