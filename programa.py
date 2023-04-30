import argparse
import shutil

parsx = argparse.ArgumentParser()
parsx.add_argument("-i", "--input", help="ARCHIVO-ENTRADA.txt", required=True)
parsx.add_argument("-o", "--output", help="ARCHIVO-SALIDA.txt", required=True)
argumentox = parsx.parse_args()

if shutil.which(argumentox.input):
    
     with open(argumentox.input, "R") as fin:
        content = fin.read()
        
        with open(argumentox.output, "W") as fout:
            
            fout.write(content)
else:
   
    print(f"El siguiente archivo no existe: {argumentox.input}")