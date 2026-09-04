import re

class MARC21Validator:
    @staticmethod
    def validate_isbn(isbn: str) -> bool:
        """Validate standard ISBN-10 or ISBN-13 format."""
        clean_isbn = isbn.replace("-", "").replace(" ", "")
        if len(clean_isbn) == 10:
            return bool(re.match(r"^\d{9}[\dX]$", clean_isbn))
        elif len(clean_isbn) == 13:
            return bool(re.match(r"^\d{13}$", clean_isbn))
        return False

    @staticmethod
    def validate_ddc(ddc_code: str) -> bool:
        """Validate Dewey Decimal Classification (DDC) format."""
        pattern = r"^\d{3}(\.\d+)?(\s\d+)?$"
        return bool(re.match(pattern, ddc_code))