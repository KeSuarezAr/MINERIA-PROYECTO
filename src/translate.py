from pandas import DataFrame
import requests
import os


def translate_text(text, source_lang, target_lang):
    # Define the Cloudflare Worker endpoint URL
    worker_url = 'https://655.mtis.workers.dev/translate'

    # Parameters for translation (customize as needed)
    params = {
        'text': text,  # Text to translate
        'source_lang': source_lang,  # Source language code
        'target_lang': target_lang  # Target language code
    }

    # Send GET request to the Cloudflare Worker endpoint
    response = requests.get(worker_url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        print(response.text)
        return response.text
    else:
        print(f'Error: {response.status_code} - {response.text}')


def iterate(df: DataFrame):
    df_copy = df.copy()
    for i in range(len(df_copy["label"])):
        df_copy.loc[i, "text"] = translate_text(df_copy.loc[i, "text"], "en", "es")
    data_path = os.path.join(os.path.dirname(__file__), 'data')
    os.makedirs(data_path, exist_ok=True)
    df_copy.to_csv(os.path.join(data_path, 'df_copy.csv'), index=False)
