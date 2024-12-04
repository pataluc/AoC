import requests
from dotenv import load_dotenv
import os
import argparse
from datetime import datetime

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

def download_file(url):
    # Lire le cookie de session et le proxy depuis les variables d'environnement
    session_cookie = os.getenv('SESSION_COOKIE')
    proxy = os.getenv('PROXY')

    # Préparer les en-têtes avec le cookie de session
    headers = {
        'Cookie': session_cookie
    }

    # Configurer le proxy si fourni
    proxies = None
    if proxy:
        proxies = {
            'http': proxy,
            'https': proxy
        }

    # Faire la requête pour télécharger le fichier
    response = requests.get(url, headers=headers, proxies=proxies)

    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Écrire le contenu dans un fichier
        filename = 'input.txt'  # Extraire le nom du fichier de l'URL
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(response.content)
        print(f'Fichier téléchargé : {filename}')
    else:
        print(f'Erreur lors du téléchargement : {response.status_code}')

def main(year, day):
    # Construire l'URL à partir de l'année et du jour
    url = f'https://adventofcode.com/{year}/day/{day}/input'
    download_file(url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Télécharger un fichier en utilisant un cookie de session.')
    parser.add_argument('-y', '--year', type=int, help='Année à utiliser pour l\'URL.', default=datetime.now().year)
    parser.add_argument('-d', '--day', type=int, help='Jour à utiliser pour l\'URL.', default=datetime.now().day)

    args = parser.parse_args()

    year = args.year if args.year else datetime.now().year
    day = args.day if args.day else datetime.now().day
    main(year, day)