# YoutubeDown

Um projeto em Python para baixar vídeos do YouTube.

## Descrição

Este projeto permite aos usuários baixar vídeos do YouTube utilizando a biblioteca `BaixarYT`.

## Requisitos

- Python 3.x

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/VictorVilelaSilva/YoutubeDown.git
    ```
2. Navegue até o diretório do projeto:
    ```sh
    cd YoutubeDown
    ```
3. Crie um ambiente virtual:
    ```sh
    python -m venv venv
    ```
4. Ative o ambiente virtual:
- Windows:
    ```sh
    venv\Scripts\activate
    ```
- Linux:
    ```sh
    source venv/bin/activate
    ```

5. Instale as dependências necessárias:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

O YoutubeDown pode ser usado de duas maneiras:

### 1. Modo Interativo
Para usar o modo interativo original, execute:
```sh
python main.py
```
Este modo irá guiá-lo através de um menu interativo onde você pode inserir a URL, escolher o formato e definir o diretório de destino.

### 2. Modo Linha de Comando (Novo!)
Para baixar diretamente via linha de comando, use:

```sh
# Baixar como MP3 no diretório atual
python main.py -u "https://www.youtube.com/watch?v=VIDEO_ID"

# Baixar como MP4 em um diretório específico
python main.py -u "https://www.youtube.com/watch?v=VIDEO_ID" -f mp4 -o "C:/Downloads"

# Baixar como MP3 em um diretório específico
python main.py -u "https://www.youtube.com/watch?v=VIDEO_ID" -f mp3 -o "./downloads"
```

#### Parâmetros disponíveis:
- `-u, --url`: URL do vídeo do YouTube (obrigatório para modo linha de comando)
- `-f, --format`: Formato do arquivo (`mp3` ou `mp4`, padrão: `mp3`)
- `-o, --output`: Diretório de saída (padrão: diretório atual)

#### Exemplos:
```sh
# Baixar um vídeo como MP3
python main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Baixar um vídeo como MP4 na pasta Downloads
python main.py -u "https://www.youtube.com/watch?v=dQw4w9WgXcQ" -f mp4 -o "C:/Users/SeuUsuario/Downloads"

# Ver ajuda com todos os parâmetros
python main.py -h
```
