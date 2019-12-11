import wget

filepath = 'listLien.txt'
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       if "abandonware" in line :
          line = line.rstrip("\n\r")
          DDownload = wget.download(line)
          DDownload
       line = fp.readline()
       
