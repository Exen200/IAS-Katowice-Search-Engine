# IAS-Katowice-Search-Engine

A lightweight and targeted Python command-line utility designed to scan administrative auction notices from the Chamber of Tax Administration (IAS) in Katowice. The script automatically iterates through multiple pagination levels of the official website to search for specific vehicle keywords (e.g., *Multivan*).

## 🌟 Features
* **Keyword-Driven Scanning:** Searches the entire text content of the website for a user-defined keyword (`SEARCH_WORD`).
* **Multi-Page Pagination:** Automatically loops through up to 15 pages of announcement listings, correctly handling the unique URL structure of the first page versus subsequent pages.
* **Direct Terminal Output:** Formats and prints matching results cleanly in the console, displaying the exact text found, the page number, and the source URL.
* **Error Handling:** Safe execution wrapped in try-except blocks to prevent crashes if a specific page fails to load due to connection timeouts or server errors.

---

## 🛠️ Requirements & Installation

The script runs on **Python 3.x** and relies on two popular external packages for making web requests and parsing HTML.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR-USERNAME/IAS-Katowice-Search-Engine.git](https://github.com/Exen200/IAS-Katowice-Search-Engine.git)
   cd IAS-Katowice-Search-Engine