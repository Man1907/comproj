import mysql.connector as m

con = m.connect(host = '127.0.0.1',username = 'root', password = 'admin', database = 'mobile_shop')
print ("connection established")
cur = con.cursor()

#cur.execute("create database if not exists mobile_shop")
#con.commit()
#cur.execute("use mobile_shop")

cur.execute("create table if not exists phone_db(prodno int(5) primary key, brand varchar(20), model varchar(50) not null,processor varchar(70), OS varchar (20), ram_GB int (3), battery_mAh int (5), price float(9,2))")
print ("table created")
con.commit()

cur.execute('insert into phone_db values(1,"samsung","Galaxy M35 5g","Samsung Exynos 1380","Android v14",6,6000,19998.00)')
cur.execute('insert into phone_db values(2,"samsung","Galaxy A35 5G","Samsung Exynos 1380","Android v14",8,5000,22898.00)')
cur.execute('insert into phone_db values(3,"Samsung","Galaxy S24 Ultra","Qualcomm Snapdragon 8 gen 3","Android v14",12,5000,108800.00)')
cur.execute('insert into phone_db values(4,"Apple","IPhone 15 pro max","Apple A17 Pro","iOS v17",8,4441,146999.00)')
cur.execute('insert into phone_db values(5,"Apple","iPhone 15","Apple A16 Bionic","iOS v17",6,3349,70499.00)')
cur.execute('insert into phone_db values(6,"Apple","iPhone 12","Apple A14 Bionic","iOS v14",4,2815,37999.00)')
cur.execute('insert into phone_db values(7,"Apple","iPhone 14 Plus","Apple A15 Bionic",	"iOS v16",6,4325,64999.00)')
cur.execute('insert into phone_db values(8,"Google","Pixel 9","Google Tensor G4","Android v14",12,4700,79999.00)')
cur.execute('insert into phone_db values(9,"Google","Pixel 8A","Google Tensor G3","Android v14",8,4492,52999.00)')
cur.execute('insert into phone_db values(10,"Google","Pixel 8 Pro","Google Tensor G3","Android v14",12,5050,101999.00)')
cur.execute('insert into phone_db values(11,"Google","Pixel 7A","Google Tensor G2","Android v13",8,4385,36999.00)')
cur.execute('insert into phone_db values(12,"OnePlus","Open Apex Edition","Qualcomm Snapdragon 8 Gen 2","Android v14",16,4805,149999.00)')
cur.execute('insert into phone_db values(13,"OnePlus","8 Pro 256GB","Qualcomm Snapdragon 865","Android v10 (Q)",12,4510,53999.00)')
cur.execute('insert into phone_db values(14,"OnePlus","Nord 3 5G 256GB","MediaTek Dimensity 9000 MT6893","Android v13",16,5000,37999.00)')
cur.execute('insert into phone_db values(15,"Motorola","Razr 50 Ultra","MediaTek Dimensity 7200 Pro MT6886","Android v14",12,4000,94998.00)')
cur.execute('insert into phone_db values(16,"Nothing","Phone 2a","MediaTek Dimensity 7200 Pro MT6886","Android v14",8,5000,24795.00)')
cur.execute('insert into phone_db values(17,"Oppo","Find N3 Flip","MediaTek Dimensity 9200 MT6985","Android v13",12,4300,62999.00)')
cur.execute('insert into phone_db values(18,"Motorola","Edge 50 Ultra","Qualcomm Snapdragon 8s Gen 3","Android v14",12,4500,53499.00)')
cur.execute('insert into phone_db values(19,"Asus","ROG Phone 8 Pro","Qualcomm Snapdragon 8 Gen 3","Android v14",16,5500,94999.00)')
cur.execute('insert into phone_db values(20,"Asus","Zenfone 3 Deluxe 256GB","Qualcomm Snapdragon 821 MSM8996 Pro","Android v6.0",6,3000,14999.00)')

con.commit()

