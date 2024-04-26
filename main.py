import requests

def get_file_urls_via_api(repo_url):
    api_url = f"https://api.github.com/repos/{repo_url}/contents/"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        file_urls = [item['download_url'] for item in data if 'download_url' in item]
        return file_urls
    else:
        return []

def generate_m3u_content(file_urls):
    m3u_content = "#EXTM3U\n"
    for url in file_urls:
        m3u_content += f"{url}\n"
    return m3u_content

repo_url = "lucmsilva651/mod.eleu.me"
file_urls = get_file_urls_via_api(repo_url)
m3u_content = generate_m3u_content(file_urls)

with open("modules.m3u", "w") as m3u_file:
    m3u_file.write(m3u_content)
