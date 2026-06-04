import requests
from bs4 import BeautifulSoup

SEARCH_WORD = "Multivan"
PAGES_TO_SCAN = 15

BASE_URL = "https://www.gov.pl/web/ias-katowice/obwieszczenia-o-licytacjach"

headers = {
    "User-Agent": "Mozilla/5.0"
}

found = []

for page in range(1, PAGES_TO_SCAN + 1):

    # Pierwsza strona ma inny URL
    if page == 1:
        url = BASE_URL
    else:
        url = f"{BASE_URL}?page={page}&size=10"

    print(f"\nSprawdzam stronę {page}: {url}")

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        text = soup.get_text("\n")

        lines = [line.strip() for line in text.split("\n") if line.strip()]

        for line in lines:
            if SEARCH_WORD.lower() in line.lower():
                found.append({
                    "page": page,
                    "title": line,
                    "url": url
                })

    except Exception as e:
        print(f"Błąd podczas pobierania strony {page}: {e}")

print("\n================ WYNIKI ================\n")

if found:
    for item in found:
        print(f"Strona: {item['page']}")
        print(f"Tytuł: {item['title']}")
        print(f"URL: {item['url']}")
        print("-" * 60)
else:
    print(f"Nie znaleziono frazy: {SEARCH_WORD}")