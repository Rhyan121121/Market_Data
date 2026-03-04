from os import system
from time import sleep
from core import ods_handler, shoping_list_handler, export_handler
import os


def get_user_file_selection(directory="data", extension=".ods"):

    available = [f.replace(extension, '') for f in os.listdir(directory) if f.endswith(extension)]

    if not available:
        print(f"\nNenhum arquivo {extension} encontrado na pasta '{directory}'.")
        return None

    print(f"\nListas {extension} encontradas:")
    for i, name in enumerate(available, start=1):
        print(f"  {i} - {name}")

    choice = input("\nEscolha o número ou digite o nome da lista: ").strip()

    if choice.isdigit():
        index = int(choice) - 1
        if 0 <= index < len(available):
            return available[index]


    return choice if choice else None

def menu():
    print("""
====== Market Data Manager ======
1 - Criar/Editar Lista (TXT -> ODS)
2 - Exportar para Imagem (PNG)
3 - Remover Item da Planilha
4 - Sair""")


def main():
    print("Iniciando o servidor do LibreOffice...")
    ods_handler.start_ods_server()

    while True:
        system('clear')
        menu()
        option = input("\nOpção: ")

        if option == "4":
            print("\nEncerrando sistema...")
            ods_handler.stop_ods_server()
            sleep(1)
            break

        match option:
            case "1":
                list_name = input("\nNome da lista (ex: compras_maio): ").strip()
                if not list_name: list_name = "lista_padrao"


                txt_path = f"data/{list_name}.txt"
                ods_path = f"data/{list_name}.ods"

                while True:
                    raw_data = input(f"\n[{list_name}] Item, Quantidade (ou 'S' para salvar ou 'ENTER'): ")
                    if raw_data.strip().upper() == "S" or raw_data.strip() == "":
                        break

                    if ',' not in raw_data:
                        print("Erro: Use o formato 'Produto, Quantidade'.")
                        continue


                    shoping_list_handler.write_in_archive(txt_path, raw_data + "\n", mode='a')


                print(f"Gerando planilha em {ods_path}...")
                raw_lines = shoping_list_handler.read_archive(txt_path)

                shopping_list = []
                for line in raw_lines:
                    if "," in line:
                        item, amount = line.split(",", 1)
                        shopping_list.append((item.strip(), amount.strip()))

                if shopping_list:
                    ods_handler.create_spreadsheet(shopping_list, ods_path)
                    print("Sucesso!")

                sleep(2)

            case "2":
                    target_name = get_user_file_selection()

                    if target_name:
                        source_file = f"data/{target_name}.ods"
                        if os.path.exists(source_file):
                            export_handler.export_document(source_file, output_format="png")
                        else:
                            print(f"Erro: A lista '{target_name}' não existe!")

                    sleep(2)

            case "3":
                target_name = get_user_file_selection()

                if target_name:
                    ods_path = f"data/{target_name}.ods"
                    txt_path = f"data/{target_name}.txt"

                    if os.path.exists(ods_path):
                        item = input(f"Qual item deseja remover de '{target_name}'? ").strip()


                        ods_handler.remove_item_and_shift_up(ods_path, item)

                        shoping_list_handler.remove_item_from_txt(txt_path, item)

                        print("\nRemoção concluída com sucesso!")
                    else:
                        print(f"Erro: O arquivo '{target_name}.ods' não existe.")

                sleep(2)

            case _:
                print("Numero invalido!\nReiniciando o sistema...")
                sleep(2)
                continue



if __name__ == "__main__":
    main()