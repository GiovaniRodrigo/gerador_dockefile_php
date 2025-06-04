import json
import os

def montar_comando_volumes():
    prefix = "VOLUME /var/www/html"
    comando = prefix
    print(comando)
    return comando

def montar_comando_copy():
    prefix = "COPY ./src/ /var/www/html/"
    comando = prefix
    print(comando)
    return comando

def montar_comando_from(versao):
    prefix = "FROM php:"
    if versao.startswith('8.0'):
        comando = prefix + versao + "-fpm"
    elif versao.startswith('8.1'):
        comando = prefix + versao + "-fpm"
    elif versao.startswith('8.2'):
        comando = prefix + versao + "-fpm"
    elif versao.startswith('8.3'):
        comando = prefix + versao + "-fpm"
    else:
        comando = prefix + versao
    
    print(comando)
    return comando

def montar_comando_instalar_extensoes(lista_extensao):
    prefix = "RUN docker-php-ext-install "
    extensoes = lista_extensao.split('\n')
    extensoes = [extensao for extensao in extensoes if extensao]  # Remove linhas vazias
    comando = prefix + ' '.join(extensoes)
    print(comando)
    return comando


def listaExtensaoDockerfile(versao_php):
    extensaoDockerfile = ""
    
    extensoes = versao_php_list[versao_php]
    for extensao in extensoes:
        if extensoes[extensao] == 2:
            print("A extensão ", extensao, " está obsoleta, deseja adicionar?")
            inserir = input("Digite 's' para sim ou 'n' para não: ")
            
            if inserir not in ['s', 'n']:
                os.system('clear' if os.name == 'posix' else 'cls')
                print("Opção inválida. Por favor, digite 's' ou 'n'.")
                listaExtensaoDockerfile(versao_php)
            
            if inserir.lower() == 's':
                extensaoDockerfile += extensao + '\n'
            
        else:
            extensaoDockerfile += extensao + '\n'
            pass
    
    print("\nExtensões do Dockerfile:")
    print(extensaoDockerfile)
    return extensaoDockerfile

def selecionar_versao():
    global versao_php_list, versao_php, dependencias_list
    
    with open('dockerfileContent.json', 'r', encoding='utf-8') as arquivo:
        conteudo = json.load(arquivo)
        os.system('clear' if os.name == 'posix' else 'cls')
        print("=== Criando Dockerfile ===")
        print("Versão do PHP selecionada:", versao_php)
    
    return versao_php

def importar_dependencias_json():
    global dependencias_list
    with open('dependencias.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    dependencias_list = dados

def importar_versao_json():
    global versao_php_list
    with open('versao_extensao.json', 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
    versao_php_list = dados

def menu ():
    versoes = list(versao_php_list.keys())
    print("Versões disponíveis:")
    for versao in versoes :
        print("- ", versao)
        
        pass
    print()
    print("Qual versão do php deseja criar o Dockerfile?")
    
    global versao_php 
    versao_php = input("Digite a versão do PHP: ")
    if versao_php not in versoes:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("Versão inválida. Por favor, tente novamente.")
        menu()
        pass
    os.system('clear' if os.name == 'posix' else 'cls')

def main() :
    print("=== Main Function: Construct Module ===")
    importar_versao_json()
    importar_dependencias_json()
    
    os.system('clear' if os.name == 'posix' else 'cls')
    menu()
    
    versao = selecionar_versao()
    
    lista_extensao = listaExtensaoDockerfile(versao)
    
    os.system('clear' if os.name == 'posix' else 'cls')
    
    comando_from = montar_comando_from(versao)
    
    comando_instalar_extensoes = montar_comando_instalar_extensoes(lista_extensao)
    
    comando_copy = montar_comando_copy()
    
    comando_volumes = montar_comando_volumes()
    
    os.makedirs('Dockerfiles', exist_ok=True)
    dockerfile_path = f'Dockerfiles/Dockerfile.{versao}'
    with open(dockerfile_path, 'w', encoding='utf-8') as arquivo:
        arquivo.write(comando_from + '\n')
        arquivo.write(comando_copy + '\n')
        arquivo.write(comando_instalar_extensoes + '\n')
        arquivo.write(comando_volumes + '\n')
        
    print("\nDockerfile criado com sucesso!")
    print("Para construir a imagem, execute: docker build -t nome_da_imagem .")
    
main()
