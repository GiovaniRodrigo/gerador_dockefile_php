import os

# construct.py

def write_dockerfile(content, php_version, dockerfile_dir="Dockerfiles"):
    os.makedirs(dockerfile_dir, exist_ok=True)
    dockerfile_path = os.path.join(dockerfile_dir, f"Dockerfile.{php_version}")
    with open(dockerfile_path, "w") as f:
        f.write(content)

def choose_php_version():
    versions = [
        "8.2-cli", "8.1-cli", "8.0-cli", "7.4-cli", "7.3-cli", "7.2-cli", "7.1-cli", "7.0-cli", "5.6-cli"
    ]
    print("Escolha a versão do PHP:")
    for idx, version in enumerate(versions, 1):
        print(f"{idx}. {version}")
    while True:
        try:
            choice = int(input("Digite o número da versão desejada: "))
            if 1 <= choice <= len(versions):
                return versions[choice - 1]
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

# Mapeamento das extensões por versão
EXTENSIONS = {
    "5.6-cli":  ["json", "mbstring", "curl", "openssl", "opcache", "intl", "pdo_mysql", "gd", "imagick", "zip", "fileinfo"],
    "7.0-cli":  ["json", "mbstring", "curl", "openssl", "opcache", "intl", "pdo_mysql", "gd", "imagick", "zip", "fileinfo"],
    "7.1-cli":  ["json", "mbstring", "curl", "openssl", "sodium", "opcache", "intl", "pdo_mysql", "gd", "imagick", "zip", "fileinfo"],
    "7.2-cli":  ["json", "mbstring", "curl", "openssl", "sodium", "opcache", "intl", "pdo_mysql", "gd", "imagick", "zip", "fileinfo"],
    "7.3-cli":  ["json", "mbstring", "curl", "openssl", "sodium", "opcache", "intl", "pdo_mysql", "gd", "imagick", "zip", "fileinfo"],
    "7.4-cli":  ["json", "mbstring", "curl", "openssl", "sodium", "opcache", "intl", "pdo_mysql", "gd", "imagick", "zip", "fileinfo"],
    "8.0-cli":  ["json", "mbstring", "curl", "openssl", "sodium", "opcache", "intl", "pdo_mysql", "gd", "imagick", "zip", "fileinfo"],
    "8.1-cli":  ["json", "mbstring", "curl", "openssl", "sodium", "opcache", "intl", "pdo_mysql", "gd", "imagick", "zip", "fileinfo"],
    "8.2-cli":  ["json", "mbstring", "curl", "openssl", "sodium", "opcache", "intl", "pdo_mysql", "gd", "imagick", "zip", "fileinfo"],
}

def get_install_commands(php_version):
    extensions = EXTENSIONS.get(php_version, [])
    # imagick precisa de instalação especial, as outras podem ser instaladas via docker-php-ext-install
    special_exts = []
    normal_exts = []
    for ext in extensions:
        if ext == "imagick":
            special_exts.append(ext)
        else:
            normal_exts.append(ext)
    cmds = []
    if normal_exts:
        cmds.append(f"RUN docker-php-ext-install {' '.join(normal_exts)}")
    if "imagick" in special_exts:
        cmds.append(
            "RUN apt-get update && apt-get install -y libmagickwand-dev --no-install-recommends && pecl install imagick && docker-php-ext-enable imagick"
        )
    return "\n".join(cmds)

if __name__ == "__main__":
    php_version = choose_php_version()
    install_cmds = get_install_commands(php_version)
    dockerfile_content = f"""\
FROM php:{php_version}
WORKDIR /app
COPY . /app
{install_cmds}
CMD ["php", "-S", "0.0.0.0:8000"]
"""
    write_dockerfile(dockerfile_content, php_version)
    print(f"Dockerfile criado com PHP {php_version}.")