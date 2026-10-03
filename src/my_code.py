import json
import subprocess

DOCS = [
    {
        "field": "visual_art",
        "channel": "web",
        "url": "https://riverbend-design-review.example/2026/02/illustration-studios",
        "title": "Illustration studios and generated concept art",
        "publisher": "Riverbend Design Review",
        "publication_date": "2026-02-11",
        "collection_period": "2025-01 to 2025-09",
        "text": "Across forty-two studios, commissioning of external concept art fell by twelve "
        "per cent against the previous comparable period. The decline is concentrated "
        "in early-stage mood and layout work rather than in finished illustration, and "
        "studios reported that revision rounds rose over the same window.",
    },
    {
        "field": "music",
        "channel": "web",
        "url": "https://riverbend-music-quarterly.example/2026/01/session-players",
        "title": "Session players and generated stems",
        "publisher": "Riverbend Music Quarterly",
        "publication_date": "2026-01-09",
        "collection_period": "2025-03 to 2025-10",
        "text": "Booking logs from nineteen recording studios show total session hours down by "
        "nine per cent against the previous comparable period. The decline is "
        "concentrated in library and advertising work rather than in album sessions. "
        "The analysis excludes home and project studios.",
    },
    {
        "field": "music",
        "channel": "internal",
        "url": "https://intranet.example/post-production/2026/01/audio-post-note",
        "title": "Audio post production note",
        "publisher": "Post Production, internal",
        "publication_date": "2026-01-30",
        "collection_period": "Q4 2025",
        "text": "Session hours booked across the quarter fell by twenty-two per cent against "
        "the same quarter a year earlier. The review counts every project the "
        "department ran, including work recorded in home and project studios.",
    },
]

# Generate an excerpt for each document by taking the first sentence of the text.
for _doc in DOCS:
    _doc["excerpt"] = _doc["text"].split(". ")[0] + "."

formatted_docs = json.dumps(DOCS, indent=2, ensure_ascii=False)
print(formatted_docs)


# Create a dictionary mapping URLs to their corresponding documents.
# Alternative way to create the dictionary mapping URLs to documents.
# BY_URL = {}
# for doc in DOCS:
#     url = doc["url"]
#     BY_URL[url] = doc
BY_URL = {doc["url"]: doc for doc in DOCS}

formatted_by_url = json.dumps(BY_URL, indent=2, ensure_ascii=False)


# Copy the JSON representation of the documents indexed by URL to the clipboard.
subprocess.run(
    "clip",
    input=formatted_by_url,
    text=True,
    check=True,
)
