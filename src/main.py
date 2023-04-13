from pytube import YouTube
import os

if __name__ == "__main__":
    
    os.system('color')
    
    file_to_read='src/links.txt'
    f = open(file_to_read, "r")

    for link in f:
        try:
            yt = YouTube(link)
            video = yt.streams.filter(only_audio=True).first()
        
            dn = os.path.abspath(file_to_read)    
            out_path = os.path.join(os.path.dirname(dn),'out')
            out_file = video.download(output_path=out_path)

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            
            print("\033[92m" + yt.title + " se descargo correctamente\033[0m")

        except Exception as e:
            
            print(f"\033[91mOcurrio un error en {link} \b{e}\033[0m")

    f.close()
