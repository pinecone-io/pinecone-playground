# Pinecone Playground

Pinecone Playground is a companion app for the [Pinecone docs](https://www.pinecone.io/docs). It is an interactive web app that lets you run Pinecone without writing any code.

Get started with Pinecone at [pinecone.io/start](https://www.pinecone.io/start/)
and receive your API key.

## Get started

Make sure that your Python version is `>=3.6`.

Clone the repository.

```
git clone https://github.com/pinecone-io/pinecone-playground.git
cd pinecone-playground
```

Install dependencies.

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start server.

```
# Activate the virtual environment if it is not active.
source venv/bin/activate

python server.py
```

![Pinecone Playground](pinecone-playground.png)
