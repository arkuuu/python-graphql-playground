# python-graphql-playground

```bash
# load venv (mac/linux)
source venv/bin/activate
```

```bash
# start server
uvicorn main:app

# start dev server with reload
uvicorn --reload main:app
```

```bash
# reinstall packages
pip freeze | xargs pip uninstall -y
pip install -r requirements.txt
```
