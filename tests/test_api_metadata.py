import os
import json
import pytest
import requests
import responses
from dotenv import load_dotenv
from utils.marc_validator import MARC21Validator

# Load environment variables dari file .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://openlibrary.org")
TIMEOUT = int(os.getenv("TIMEOUT", 5))

def load_mock_data():
    mock_path = os.path.join(os.path.dirname(__file__), "../data/mock_books.json")
    with open(mock_path, "r", encoding="utf-8") as f:
        return json.load(f)

class TestBookMetadataAPI:

    @pytest.mark.parametrize("book", load_mock_data())
    def test_mock_book_data_schema(self, book):
        """Validate structure and data types of local mock book metadata."""
        assert "isbn" in book and isinstance(book["isbn"], str)
        assert "title" in book and isinstance(book["title"], str)
        assert "author" in book and isinstance(book["author"], str)
        assert "ddc" in book, "Library system catalog must include DDC classification"

    def test_get_book_by_isbn_success(self):
        """Validate live Open Library API integration for a valid ISBN."""
        isbn = "9780132350884"
        url = f"{BASE_URL}/api/books"
        params = {
            "bibkeys": f"ISBN:{isbn}",
            "format": "json",
            "jscmd": "data"
        }
        try:
            response = requests.get(url, params=params, timeout=TIMEOUT)
            assert response.status_code == 200, f"Expected HTTP 200, got {response.status_code}"
            data = response.json()
            assert f"ISBN:{isbn}" in data, f"Key ISBN:{isbn} not found in API response"
        except requests.exceptions.RequestException as e:
            pytest.fail(f"API request failed due to network/timeout error: {e}")

    # ==========================================
    # HERMETIC API MOCKING TESTS (RESPONSES)
    # ==========================================

    @responses.activate
    def test_open_library_api_mocked_success(self):
        """Simulasi pengujian jika API merespons 200 OK secara terisolasi (Mocking)."""
        mock_isbn = "0451450523"
        mock_url = f"{BASE_URL}/api/books?bibkeys=ISBN:{mock_isbn}&format=json"
        
        # Mocking respons sukses dari server
        responses.add(
            responses.GET,
            mock_url,
            json={f"ISBN:{mock_isbn}": {"bib_key": f"ISBN:{mock_isbn}", "preview": "noview"}},
            status=200
        )

        response = requests.get(mock_url, timeout=TIMEOUT)
        assert response.status_code == 200
        assert f"ISBN:{mock_isbn}" in response.json()

    @responses.activate
    def test_open_library_api_mocked_server_down(self):
        """Simulasi pengujian jika API Server Open Library sedang mengalami Error 500."""
        mock_isbn = "0451450523"
        mock_url = f"{BASE_URL}/api/books?bibkeys=ISBN:{mock_isbn}&format=json"
        
        # Mocking respons error 500 dari server
        responses.add(
            responses.GET,
            mock_url,
            json={"error": "Internal Server Error"},
            status=500
        )

        response = requests.get(mock_url, timeout=TIMEOUT)
        assert response.status_code == 500