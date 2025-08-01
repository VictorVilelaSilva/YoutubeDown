import sys
import os
import argparse
from src.BaixarYT import initYoutubeDownloader
from src.functions import downloadVideo, on_progress, clearTerminal

def download_from_url(url, output_dir=None, format_type='mp3'):
    """Baixa um vídeo diretamente da URL fornecida"""
    try:
        clearTerminal()
        print(f"Baixando de: {url}")
        print(f"Formato: {format_type}")
        print(f"Diretório: {output_dir if output_dir else 'diretório atual'}")
        print("-" * 50)
        
        yt, dest_path = downloadVideo(on_progress, url, output_dir or '', format_type)
        
        print(f"\n✅ Download concluído com sucesso!")
        print(f"📁 Arquivo salvo em: {dest_path}")
        
    except Exception as e:
        print(f"❌ Erro ao baixar: {e}")
        sys.exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='YouTube Downloader - Baixe vídeos do YouTube como MP4 ou MP3',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Exemplos de uso:
  python main.py                                    # Modo interativo
  python main.py -u "https://youtube.com/watch?v=..." # Baixar MP3 no diretório atual
  python main.py -u "https://youtube.com/watch?v=..." -f mp4 -o "C:/Downloads" # Baixar MP4 em pasta específica
        '''
    )
    
    parser.add_argument('-u', '--url', 
                       help='URL do vídeo do YouTube para baixar')
    parser.add_argument('-f', '--format', 
                       choices=['mp3', 'mp4'], 
                       default='mp3',
                       help='Formato do arquivo (padrão: mp3)')
    parser.add_argument('-o', '--output', 
                       help='Diretório de saída (padrão: diretório atual)')
    
    args = parser.parse_args()
    
    # Se uma URL foi fornecida, usa o modo de linha de comando
    if args.url:
        download_from_url(args.url, args.output, args.format)
    else:
        # Caso contrário, usa o modo interativo original
        initYoutubeDownloader()