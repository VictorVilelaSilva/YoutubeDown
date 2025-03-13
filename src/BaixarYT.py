import time
import inquirer
from .desenhos import valeuDraw
from .functions import clearTerminal,downloadVideo,on_progress



def initYoutubeDownloader():
    reload = True
    clearTerminal()
    dest_dir = None

    # DELAY DE 2 SEGUNDOS
    time.sleep(3)
    while reload:
        link = input("Insira o link do vídeo que deseja baixar: ")

        clearTerminal()

        if not dest_dir:
            # Defina o diretório de destino para salvar o vídeo
            print("Insira o diretório de destino para salvar o vídeo")
            print("Caso queira salvar no diretório atual, pressione Enter.")
            dest_dir = input()
        else:
            print(f"Diretório de destino atual: {dest_dir}")
            print(
                "Caso queira alterar, insira o novo diretório ou pressione Enter para confirmar."
            )
            new_dest_dir = input()
            if new_dest_dir:
                dest_dir = new_dest_dir

        archive_type = inquirer.prompt(
            [
                inquirer.List(
                    "archive_type",
                    message="Escolha o tipo de arquivo",
                    choices=["mp4", "mp3"],
                )
            ]
        )["archive_type"]

        clearTerminal()

        yt, dest_path = downloadVideo(on_progress, link, dest_dir, archive_type)

        time.sleep(2)

        clearTerminal()
        aux = inquirer.prompt(
            [
                inquirer.List(
                    "play",
                    message="Deseja baixar outro vídeo ?",
                    choices=["Sim", "Não"],
                )
            ]
        )
        if aux["play"] == "Não":
            reload = False
        clearTerminal()
    valeuDraw()
    clearTerminal()
    time.sleep(3)