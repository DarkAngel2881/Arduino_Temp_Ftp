import ftplib

def send_temps(file, city):
    #credentials
    HOST = "ftp.iotfermilecce.altervista.org"
    USER = "iotfermilecce"
    PASS = "Y43n3C6DTr2x"
    filename = file

    #initialize ftp
    ftp = ftplib.FTP(HOST, USER, PASS, encoding = "ISO-8859-1")

    #move to city directory
    ftp.cwd(city)

    #send binary file
    with open(filename, "rb") as file:
        ftp.storbinary("STOR " + filename, file)

    #write txt
    with open(filename, "wb") as file:
        ftp.retrbinary("RETR " + filename, file.write)

    ftp.dir()
    ftp.quit()
