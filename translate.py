import requests
import csv
import os

from concurrent.futures import ThreadPoolExecutor, as_completed

def translate_text(text: str, source_lang: str, target_lang: str):
    url = 'https://655.mtis.workers.dev/translate'

    params = {
        'text': text,
        'source_lang': source_lang,
        'target_lang': target_lang
    }

    response = requests.get(url, params=params)

    data = response.json()
    if response.status_code == 200:
        print(f'Translation: {data["response"]["translated_text"]}')
        return data["response"]["translated_text"]
    else:
        print(f'Error: {response.status_code} - {data["error"]}')
        return None


def translate_csv(input_file: str, output_file: str, source_lang: str, target_lang: str):
    # Read existing translations from the output file if it exists
    existing_translations = {}
    if os.path.exists(output_file):
        with open(output_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                existing_translations[row['v2']] = row['v3']

    with open(input_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames
        rows = list(reader)

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in rows:
            if row['v2'] in existing_translations and existing_translations[row['v2']]:
                print(f"Skipping already translated row: {row['v2']}")
                row['v3'] = existing_translations[row['v2']]
            else:
                translated_text = translate_text(row['v2'], source_lang, target_lang)
                row['v3'] = translated_text

            writer.writerow(row)


translate_csv("data/spam.csv", "data/spam_translated.csv", "en", "es")
