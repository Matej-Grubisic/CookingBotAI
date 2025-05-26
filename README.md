# Cooking AI app

### Before running the app

1. Make sure to set up a virtual environment before.
2. Make sure all the requirements are installed with this command:

```
pip install -r requirements.txt
```
3. Make sure ollama is running:

```ollama pull llama3.2:1.5b```

```ollama pull nomic-embed-text```

### Run Backend

1. Be connected to the school network
2. Run the API:
```
python Endpoints.py
```
3. Open the API docs in your browser:
```
http://localhost:8000/docs
```
###
Running the UI:

```
flet run
```
or
```
python.exe main.py
```

## Run Backend in Docker

Just go to the directory and run:

```
docker compose up
```

And open:

```
http://localhost:8000/docs
```


## Promptfoo Testing
have promptfoo installed:
```
npm install promptfoo@latest
```

Then run the following command inside the project directory:
```
npx promptfoo@latest eval
```
or
```
promptfoo eval
```

After you have done that you should be able to see all the statistics

## Notes
1. Ensure the pdf's you wish to import are actually .pdf 

2. This app uses local LLMs and embeddings via Ollama, so make sure those services are working before use.
