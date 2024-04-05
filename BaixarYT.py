import os
import time
from moviepy.editor import VideoFileClip
from pytube import YouTube
from functions import *
from desenhos import *

clearTerminal()

takeRandomDraw()

#DELAY DE 2 SEGUNDOS
time.sleep(2)
clearTerminal()

link= input("Insira o link do vídeo que deseja baixar: ")

clearTerminal()

# Defina o diretório de destino para salvar o vídeo
print('Insira o diretório de destino para salvar o vídeo')
print('Caso queira salvar no diretório atual, pressione Enter.')
dest_dir = input()

clearTerminal()

# Verifica se o diretório de destino existe, se não, cria um novo

yt, dest_path = dowloadVideo(on_progress, link, dest_dir)

print('Deseja converter o arquivo para MP3? (s/n)')
convert = input()
if(convert.lower() == 's'):
    convert_mp4_to_mp3(dest_path, os.path.join(dest_dir, yt.title + '.mp3'))
    print(f'Arquivo convertido para MP3! {yt.title}.mp3')
else:
    print('Ok, download concluído!')
