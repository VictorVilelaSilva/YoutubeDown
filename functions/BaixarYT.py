from importlib import reload
import os
import time
from moviepy.editor import VideoFileClip
from pytubefix import YouTube
from functions.functions import *
from functions.desenhos import *


def initYoutubeDownloader():
    reload = True
    clearTerminal()
    dest_dir = None

    #desenha o tech lead
    takeRandomDraw()

    #DELAY DE 2 SEGUNDOS
    time.sleep(3)
    clearTerminal()
    while reload:
        link= input("Insira o link do vídeo que deseja baixar: ")

        clearTerminal()

        if(not dest_dir):
            # Defina o diretório de destino para salvar o vídeo
            print('Insira o diretório de destino para salvar o vídeo')
            print('Caso queira salvar no diretório atual, pressione Enter.')
            dest_dir = input()
        else:
            print(f'Diretório de destino atual: {dest_dir}')
            print('Caso queira alterar, insira o novo diretório ou pressione Enter para confirmar.')
            new_dest_dir = input()
            if(new_dest_dir):
                dest_dir = new_dest_dir

        archive_type = input('Deseja baixar o Video ou apenas o Audio? 1-mp4 2-mp3: ')

        clearTerminal()

        print('Aguarde um monento...')

        yt, dest_path = dowloadVideo(on_progress, link, dest_dir,archive_type)

        time.sleep(2)

        clearTerminal()
        if input('Deseja baixar outro vídeo? (s/n):').lower() == 'n':
            reload = False
        clearTerminal()
    valeuDraw()
    time.sleep(3)
        



