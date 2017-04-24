#Zahrah Citra Hafizha
#5114100012
#KIJ A
#Tugas Encrypt Decrypt

from operator import xor

def function (asciitext, asciisecret): #fungsi encrypt
    hasil = [None] * len(asciitext) #buat array kosongan
    hasilchar = [None] * len(asciitext)

    leftmost = [None] * 4 #bagian kiri
    rightmost = [None] * 4 #bagian kanan
    for i in range(0,4):
        leftmost[i] = asciisecret[i]
        rightmost[i] = asciisecret[i+4] #tambah 4 bit dr yang kiri

    #lakukan proses xor antara p dan k0
    index = 0
    blok = len(asciitext) / 4 #dibagi per blok
    for i in range(0, blok):
        for j in range(0, 4):
            hasil[index] = xor(asciitext[index], leftmost[j]) #xor
            index += 1

    index = 0
    #print "before (hasil xor sebelum ditambah)", hasil
    for i in range(0, blok):
        for j in range(0, 4):
            hasil[index] = hasil[index]+ rightmost[j] #tambahin hasil proses sebelumnya dengan k1
            hasil[index] = hasil[index] % 256 #yang di mod 2pangkat64
            index += 1
    #print "after", hasil

    #change to character
    for i in range(0,len(asciitext)):
        hasilchar[i] = chr(hasil[i])#jadi karakter
    #print "hasil : ", hasil
    print "hasil encrypt : ", hasilchar

    #print "mulai proses DECRYPT"

    tempasc = [None] * len(asciitext)
    for i in range (0, len(asciitext)):
        tempasc[i] = ord(hasilchar[i]) #ke ascii

    tempmin = [None] * len(asciitext)
    index = 0
    for i in range(0, blok):
        for j in range(0, 4):
            tempmin[index] = tempasc[index] - rightmost[j] #dibalikin waktu sebelum
            index += 1
    #print "before add-ing", tempmin

    tempxor = [None] * len(asciitext)
    index = 0
    for i in range(0, blok):
        for j in range (0,4):
            tempxor[index] = xor(tempmin[index], leftmost[j])
            index += 1

    hasildec = [None] * len(asciitext)
    for i in range(0, len(asciitext)):
        hasildec[i] = chr(tempxor[i])

    print "hasil decrypt : ", hasildec

    return hasildec

secret = raw_input("Masukkan secret key: ") #secret key
longsecret = len(secret)
ascsec = [None] * longsecret #bikin array kosong
for i in range(0, longsecret):
    ascsec[i] = ord(secret[i]) #mengkonversikan secret key ke ascii

text = raw_input("Masukkan input: ")#masukin input yg mau di encrypt decrypt
longtext = len(text)#itungjumlah huruf
longdata = longtext

#hitung panjang karakter yg di proses, harus 32 bit
if longtext % 4 > 0: #kalo di mod nya masih ada sisa
    sisa = 4 - (longtext % 4)
    longdata = longtext + sisa
datatext = [None] * longdata
for i in range(0, longdata):
    if i < longtext:
        datatext[i] = text[i]
    else:
        datatext[i] = " " #ditambahin tapi pake kosongan

textascii = [None] * longdata #kosongan
for i in range(0, longdata):
    textascii[i] = ord(datatext[i]) #konversi dr string ke ascii

#print "asciitext ", textascii

hasil = function(textascii, ascsec)
print hasil
