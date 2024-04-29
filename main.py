def remove_blank(lista):
    # Iterando e substituindo espaços em branco por %
    for i in range(len(lista)):
        if ' ' in lista[i]:
            lista[i] = lista[i].replace(' ', '%20')
    return lista

def readFile(file_path):
    lista_arquivos = []
    with open(file_path) as file:
        lista_arquivos = file.readlines()
    return lista_arquivos

def generate_m3u_content(lista, url):
    # Gerando o cabeçalho
    m3u_content = "#EXTM3U\n"
    # Iterar sobre o tamanho da lista e dar append no m3ucontent
    for i in range(len(lista)):
        m3u_content += f"{url}{lista[i]}"
    return m3u_content

url = "https://raw.githubusercontent.com/lucmsilva651/mod.eleu.me/main/"
path = input('Caminho do txt: ')
lista = readFile(path)

remove_blank(lista)
m3content = generate_m3u_content(lista, url)

with open("modules.m3u", "w") as m3u_file:
    m3u_file.write(m3content)