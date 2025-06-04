# Gerador de Dockerfile PHP com Python

Este projeto é um gerador de arquivos Dockerfile para ambientes de desenvolvimento PHP, permitindo a instalação de extensões conforme a versão do PHP escolhida.

## Funcionalidades

- Gera Dockerfile customizado para diferentes versões do PHP.
- Permite especificar extensões PHP a serem instaladas.
- Automatiza a criação de ambientes de desenvolvimento PHP via Docker.

## Como usar

1. Clone este repositório:
    ```
    git clone https://github.com/seu-usuario/seu-repo.git
    cd seu-repo
    ```

2. Execute o script Python para gerar o Dockerfile:
    ```
    python gerar_dockerfile.py --php-versao 8.1 --extensoes pdo_mysql,gd,zip
    ```

3. O arquivo `Dockerfile` será criado na pasta atual.

## Executando via Docker

Este repositório também possui um `Dockerfile` pronto para uso. Para construir a imagem com as permissões do seu usuário, utilize o comando abaixo:

```
docker build --build-arg USER_ID=$(id -u) --build-arg GROUP_ID=$(id -g) -t sua-imagem .
```

Caso prefira executar o gerador dentro de um container, utilize a imagem disponível:

```
docker run -it -v "$(pwd)/Dockerfiles:/usr/src/app/Dockerfiles" giovanii/gerador_dockerfile
```

## Exemplo de uso

Ao executar o comando abaixo, será exibido um menu interativo para escolher a versão do PHP:

```
docker run -it -v "$(pwd)/Dockerfiles:/usr/src/app/Dockerfiles" giovanii/gerador_dockerfile
```

Saída esperada:

```
Escolha a versão do PHP:

1) 8.2-cli
2) 8.1-cli
3) 8.0-cli
4) 7.4-cli
5) 7.3-cli
6) 7.2-cli
7) 7.1-cli
8) 7.0-cli
9) 5.6-cli

Digite o número da versão desejada:
```
