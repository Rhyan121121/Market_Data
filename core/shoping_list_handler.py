import os

def read_archive(name_archive):

    try:
        with open(name_archive, 'r', encoding='utf-8') as arquivo:
            return arquivo.readlines()

    except FileNotFoundError:
        print(f"Arquivo '{name_archive}' não encontrado.")
    except IOError:
        print("Erro : no acesso de abertura do arquivo")
    except PermissionError:
        print("Erro : permissão de acesso ao arquivo")
    except Exception as e:
        print(f"Erro : inesperado ao ler o arquivo '{name_archive }': {e}")
    return []

def write_in_archive(name_archive, content, mode='w'):
    try:
        with open(name_archive, mode, encoding='utf-8') as archive:
            archive.write(content)

    except IOError:
        print("Erro : no acesso de abertura do arquivo")
    except PermissionError:
        print(f"Erro : permissão de acesso ao arquivo {name_archive}")
    except Exception as e:
        print(f"Erro : inesperado ao ler o arquivo '{name_archive}': {e}")

def verify_if_archive_exists(arquivov):
    if not os.path.exists(arquivov):
        open(arquivov, 'a').close()


def remove_item_from_txt(name_archive, item_to_remove):
    lines = read_archive(name_archive)

    if not lines:
        print("Nenhum dado para remover.")
        return

    updated_lines = []
    target = item_to_remove.strip().lower()

    for line in lines:
        if "," in line:
            product = line.split(",")[0].strip().lower()
            if product != target:
                updated_lines.append(line)
        elif line.strip() != "":
            updated_lines.append(line)

    write_in_archive(name_archive, "".join(updated_lines), mode='w')
    print(f"Item '{item_to_remove}' removido do arquivo com sucesso!")


def list_available_lists(directory="data", extension=".ods"):


    if not os.path.exists(directory):
        return []

    files = [f.replace(extension, '') for f in os.listdir(directory) if f.endswith(extension)]
    return files

