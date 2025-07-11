# Automation Framework (Python + Behave + CI)

![CI](https://github.com/Anshuloo7/automation-framework/actions/workflows/behave-ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.12-blue)
![License](https://img.shields.io/badge/license-MIT-green)
This is a modular, end-to-end automation testing framework built with Python, Behave (BDD), and GitHub Actions.

---

## ✅ Features

* 🔁 Retry logic for flaky APIs using `tenacity`
* 📊 HTML reports (via `behave-html-formatter`)
* 🧱 SQLite-based DB validations
* 🎲 Dynamic data with `Faker`
* 🧪 Tag-based suite control: `@smoke`, `@regression`, `@db`, `@faker`, `@e2e`
* ☁️ GitHub Actions integration with test report uploads

---

## 📂 Folder Structure

```
automation-framework/
├── .github/
│   └── workflows/
│       └── behave-ci.yml
├── .venv/                          # Local virtualenv (gitignored)
├── automation_framework/
│   ├── features/
│   │   ├── sample.feature
│   │   └── steps/
│   │       ├── api_steps.py
│   │       ├── db_steps.py
│   │       ├── e2e_steps.py
│   │       ├── faker_steps.py
│   │       └── environment.py
│   ├── utils/
│   │   ├── config.py
│   │   ├── context_setup.py
│   │   ├── data_factory.py
│   │   ├── db_utils.py
│   │   ├── logger.py
│   │   ├── retry_utils.py
│   │   └── __init__.py
│   └── tests/                      # (Reserved for future unit tests)
├── logs/                           # Runtime logs (gitignored)
├── reports/                        # HTML reports (gitignored)
├── create_db.py
├── requirements.txt
├── behave.ini
├── sample.db
├── pretty.output
├── test_suites.md
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🚀 How to Run Locally

```bash
# One-time setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Create SQLite DB
python create_db.py

# Run tests
behave

# Generate HTML report
behave -f behave_html_formatter:HTMLFormatter -o reports/report.html
```

---

## 🌿 Test Tags

| Tag           | Description                         |
| ------------- | ----------------------------------- |
| `@smoke`      | Lightweight sanity tests            |
| `@regression` | Full functional suite               |
| `@db`         | DB-layer tests using SQLite         |
| `@faker`      | Tests using randomized test data    |
| `@e2e`        | Simulated multi-layer test chaining |

---

## ⚙️ CI/CD

* GitHub Actions workflow (`behave-ci.yml`) runs on every push/PR
* Generates HTML test reports
* Uploads logs and reports as downloadable artifacts

---

## ✨ Potential Future Enhancements

* ✅ Publish HTML reports via GitHub Pages
* ✅ Add Allure or advanced HTML dashboards
* ✅ Integrate Playwright/Selenium for full-stack UI
* ✅ Move to PostgreSQL for realistic backend validation
* ✅ Add Docker support for isolated environment testing
