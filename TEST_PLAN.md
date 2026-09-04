# Test Plan - IrminsulGuard Automation Suite

## 1. Overview
IrminsulGuard is an automated QA framework designed to validate library catalog metadata integrity (MARC21/DDC standards) and ensure API reliability for digital library systems.

## 2. Test Scope
* **Unit Testing:** Metadata formatting validation (ISBN-10, ISBN-13, and DDC decimal format).
* **API Testing:** Open Library REST API schema validation, response HTTP status codes, and error handling for invalid queries.
* **Mock Data Integrity:** Local JSON dataset schema verification.

## 3. Test Scenarios
| ID | Test Suite | Description | Expected Result |
|---|---|---|---|
| TC-01 | TestBookMetadataAPI | Local mock book data schema validation | All required fields exist with correct data types |
| TC-02 | TestBookMetadataAPI | GET book by valid ISBN via Open Library API | Returns HTTP 200 and correct book title |
| TC-03 | TestBookMetadataAPI | Query API with non-existent/invalid ISBN | Returns HTTP 200 with empty JSON object |
| TC-04 | TestMARC21Validator | Validate correct ISBN-10 & ISBN-13 string patterns | Returns True |
| TC-05 | TestMARC21Validator | Validate corrupted/invalid ISBN strings | Returns False |
| TC-06 | TestMARC21Validator | Validate standard DDC classification notation | Returns True |

## 4. Execution Command
```bash
python -m pytest