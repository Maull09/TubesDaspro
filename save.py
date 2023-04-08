import data
def save(type, data): 
    if type=="bangun":
        n = data.count(data.candi) #data =[pembuat, pasir, batu, air]
        data.candi[n] = [n-1,data[0],data[1],data[2],data[3]]
    else:
        #data = [pasir, batu, air]
        data.bahan_bangunan[0] = ["pasir", "Digunakan untuk merekatkan batu",data[0]]
        data.bahan_bangunan[1] = ["batu","Digunakan sebagai fondasi dasar candi",data[1]]
        data.bahan_bangunan[2] = ["air", "Digunakan untuk memproses bahan lainnya",data[2]]
