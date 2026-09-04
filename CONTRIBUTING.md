# Contributing to IrminsulGuard

Thank you for taking the time to contribute to **IrminsulGuard**! As an automated QA testing suite, maintaining code quality, test structure, and clear documentation is essential.

## 🚀 How to Contribute

### 1. Reporting Issues
* Use GitHub Issues to report bugs or suggest new test scenarios.
* Provide clear reproduction steps, expected behavior, and actual test logs.

### 2. Development Workflow
1. Fork the repository and create your feature branch:
   `git checkout -b feature/your-feature-name`
2. Ensure Python virtual environment is active and dependencies are installed.
3. Add your new test cases or utility modules under `tests/` or `utils/`.

### 3. Testing Standards
* All test files must follow Pytest naming conventions (`test_*.py`).
* Ensure code passes all assertions locally before committing: `python -m pytest -v`
* Ensure `report.html` generates cleanly without unexpected test failures.

### 4. Commit Message Conventions
We follow standard Conventional Commit patterns:
* `feat:` Add new test scenario or utility validator.
* `fix:` Fix failing test cases or pipeline scripts.
* `docs:` Update documentation or test execution evidence.
* `refactor:` Code improvements without changing functionality.

---
*Happy Testing! Keep the knowledge of Irminsul pristine.* 🌳