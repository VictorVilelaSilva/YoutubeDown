import os
from moviepy.editor import VideoFileClip
from pytube import YouTube

def convert_mp4_to_mp3(mp4_file, mp3_file):
    video_clip = VideoFileClip(mp4_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3_file)
    audio_clip.close()
    video_clip.close()

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f'Baixando... {percentage_of_completion:.2f}% completo.', end='\r')

def dowloadVideo(on_progress, link, dest_dir):
    try: 
        if(not os.path.exists(dest_dir) and dest_dir != ''):
            os.makedirs(dest_dir)

        yt = YouTube(link, on_progress_callback=on_progress)

        # Seleciona o stream de maior qualidade
        ys = yt.streams.get_highest_resolution()

        # Define o caminho completo para o arquivo de destino
        dest_path = os.path.join(dest_dir, ys.default_filename)

        # Começa o download
        ys.download(output_path=dest_dir, filename=ys.default_filename)

        print(f'\nDownload concluído! {dest_path}')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        exit()

def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

    
