
# API Test Framework (Pytest-based)

This framework allows you to perform data-driven API testing using Pytest, with support for:
- Batch data input
- Automatic proxy setup
- Token generation via secure flow
- Logging and HTML reporting

---

## 🔧 1. Setting Up Proxy (if behind corporate firewall)

If your company network requires a proxy, update the proxy values in:

```
CommonFunctions/proxy_setup.py
```

```python
os.environ["HTTP_PROXY"] = "http://your.proxy.server:port"
os.environ["HTTPS_PROXY"] = "http://your.proxy.server:port"
```

You can also set proxy in the terminal (for one session):

**Windows:**
```cmd
set HTTP_PROXY=http://your.proxy.server:port
set HTTPS_PROXY=http://your.proxy.server:port
```

**macOS/Linux:**
```bash
export HTTP_PROXY=http://your.proxy.server:port
export HTTPS_PROXY=http://your.proxy.server:port
```

---

## 📦 2. Installing Dependencies (even if SSL issues)

Make sure you have Python 3.8+ installed.

Then install dependencies:
```bash
pip install --proxy=http://your.proxy.server:port -r requirements.txt
```

If SSL issues occur:
```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --proxy=http://your.proxy.server:port -r requirements.txt
```

---

## 🚀 3. Running the Tests

To run **all tests**:
```bash
pytest
```

To run tests in a specific file:
```bash
pytest tests/test_workitem_api.py
```

---

## 🧪 4. Running With HTML Report Output

Pytest is pre-configured to generate HTML reports automatically via `pytest.ini`.

After running tests, open:

```
output/report.html
```

This file shows:
- Each test
- Status (pass/fail)
- Detailed tracebacks (if any)
- Timestamped execution log

---

## 📁 5. Output Files

| File | Description |
|------|-------------|
| `output/logs/test_execution.log` | Logs of API calls and errors |
| `output/report.html`             | HTML report of test run |
| `output/response_output.csv`     | Raw API responses logged per test |

---

## ✅ 6. Customize It

Plug in your actual logic in:
- `CommonFunctions/auth_helper.py` — for token generation
- `pages/workitem_api.py` — for your actual API call logic

You're ready to go!
