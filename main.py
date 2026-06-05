from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# A reusable, simple HTML layout template
def get_html_layout(title: str, content: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 40px;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }}
            .card {{
                background: white;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                text-align: center;
                min-width: 300px;
            }}
            h1 {{ color: #333; }}
            p {{ color: #666; font-size: 1.1em; }}
            .highlight {{ color: #0070f3; font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="card">
            {content}
        </div>
    </body>
    </html>
    """

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    
    return html_content

@app.get("/greeting", response_class=HTMLResponse)
def read_root(name: str | None = None):
    content = f"""
        <h1>
            WELCOME TO PETRELLI'S TEST PAGE, AM SO GLAD TO HAVE YOU HERE! am sorry, there's nothing much to see here yet
        </h1>
        <p>{name}</p>
    """
    return get_html_layout("Home", content)


@app.get("/items/{item_id}", response_class=HTMLResponse)
def read_item(item_id: int, q: str | None = None):
    content = f"""
        <h1>Item Details</h1>
        <p>Item ID: <span class="highlight">{item_id}</span></p>
        <p>Query: <span class="highlight">{q if q else 'None'}</span></p>
    """
    return get_html_layout(f"Item {item_id}", content)