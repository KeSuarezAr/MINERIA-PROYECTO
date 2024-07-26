async function run() {
    const res = await fetch("POST https://translate.api.cloud.yandex.net/translate/v2/translate", {
        method: "POST",
        body: JSON.stringify({
            "sourceLanguageCode": "string",
            "targetLanguageCode": "string",
            "format": "string",
            "texts": [
                "string"
            ],
            "folderId": "string",
            "model": "string",
            "glossaryConfig": {
                "glossaryData": {
                    "glossaryPairs": [
                        {
                            "sourceText": "string",
                            "translatedText": "string",
                            "exact": true
                        }
                    ]
                }
            },
            "speller": true
        }
        ),
        headers: { "Content-Type": "application/json" }
    });

    console.log(await res.json());
}

run()