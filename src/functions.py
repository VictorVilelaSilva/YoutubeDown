import os
from pytubefix import YouTube
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn

progress = Progress(
    TextColumn("[progress.description]{task.description}"),
    BarColumn(style="red",complete_style="green"),
    TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    TimeRemainingColumn(),
)
task = None 
progress_table = None

def on_progress(stream, chunk, bytes_remaining):
    global task
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    
    if task is None:
        task = progress.add_task("[red]Baixando...", total=total_size)
        progress.start()  

    progress.update(task, completed=bytes_downloaded)

    if bytes_remaining == 0:
        progress.stop()
        task = None
        print("Download completo!")

def downloadVideo(on_progress, link, dest_dir, archive_type):
    try:
        if dest_dir != '' and not dest_dir:
            input('Deseja salvar no mesmo diretório? Pressione Enter para confirmar.')
        if not os.path.exists(dest_dir) and dest_dir != '':
            os.makedirs(dest_dir)

        yt = YouTube(link, on_progress_callback=on_progress)

        # Seleciona o stream de maior qualidade
        ys = yt.streams.get_highest_resolution()

        if archive_type == 'mp3':
            ys = yt.streams.filter(only_audio=True).first()

            # Começa o download
            arquivo = ys.download(output_path=dest_dir, filename=ys.default_filename)

            # Troca o nome do arquivo para mp3
            base, ext = os.path.splitext(arquivo) 
            novo_arquivo = base + '.mp3'
            os.rename(arquivo, novo_arquivo)

            dest_path = os.path.join(dest_dir, os.path.basename(novo_arquivo))
            
            print(f'\nDownload concluído! {dest_path}')

            return yt, dest_path

        # Define o caminho completo para o arquivo de destino
        dest_path = os.path.join(dest_dir, ys.default_filename)

        # Começa o download
        ys.download(output_path=dest_dir, filename=ys.default_filename)

        print(f'\nDownload concluído! {dest_path}')

        return yt, dest_path

    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        exit()

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    from .desenhos import drawLogo   # import local para evitar ciclo
    drawLogo()