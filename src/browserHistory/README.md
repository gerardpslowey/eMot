## Usage

### History

To get history from all installed browsers:
```python
from browser_history import get_history

outputs = get_history()

# his is a list of (datetime.datetime, url) tuples
his = outputs.histories
```

If you want history from a specific browser:
```python
from browser_history.browsers import Firefox

f = Firefox()
outputs = f.fetch_history()

# his is a list of (datetime.datetime, url) tuples
his = outputs.histories
```