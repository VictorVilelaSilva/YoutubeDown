import os
import time
from moviepy.editor import VideoFileClip
from pytube import YouTube
from functions.functions import *
from functions.desenhos import *


def initYoutubeDownloader():
    clearTerminal()

    #desenha o tech lead
    takeRandomDraw()

    #DELAY DE 2 SEGUNDOS
    time.sleep(3)
    clearTerminal()

    link= input("Insira o link do vídeo que deseja baixar: ")

    clearTerminal()

    # Defina o diretório de destino para salvar o vídeo
    print('Insira o diretório de destino para salvar o vídeo')
    print('Caso queira salvar no diretório atual, pressione Enter.')
    dest_dir = input()

    archive_type = input('Deseja baixar o Video ou apenas o Audio? 1-mp4 2-mp3: ')

    clearTerminal()

    print('Aguarde um monento...')

    # Verifica se o diretório de destino existe, se não, cria um novo

    yt, dest_path = dowloadVideo(on_progress, link, dest_dir,archive_type)

    time.sleep(3)

    clearTerminal()



