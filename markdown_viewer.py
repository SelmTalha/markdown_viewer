import markdown
import webbrowser
import os
import re

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="author" content="{author}">
    <style>
        body {{
            background-color: #2d1e2f;
            color: #fff;
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            padding: 20px;
            flex-direction: column;
        }}
        .container {{
            background: rgba(128, 128, 128, 0.3);
            padding: 20px;
            border-radius: 7px;
            box-shadow: 0 2px 10px rgba(0, 0, 10, 2.5);
            max-width: 950px;
            width: 100%;
        }}
        h1, h2, h3 {{
            color: #ffcc00;
        }}
        .footer a{{
            text-decoration:none;
            color: #fff;
            border: 1px solid;
            padding: 10px;
            border-radius:7px;
            box-shadow: 0 2px 10px rgba(0, 0, 5, 1.5);
        }}
        .footer a:hover{{
            color: #ffcc00;
        }}
        pre {{
            background: #333;
            padding: 10px;
            border-radius: 7px;
        }}
        footer {{
            margin-top: 20px;
            text-align: center;
            color: #aaa;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <div>{content}</div>
    </div>
    <footer class="footer">
        <a href="https://selmtalha.github.io/" target="_blank">© 2024 Selim Talha Çağlar. MIT License</a>
    </footer>
</body>
</html>
"""

def extract_metadata(md_content):
    metadata = {"title": "Untitled", "description": "", "author": "", "date": ""}
    metadata_pattern = re.compile(r'^([a-zA-Z]+):\s*(.*)$', re.MULTILINE)
    
    lines = md_content.split("\n")
    if lines[0].strip() == "---":
        end_idx = lines[1:].index("---") + 1
        yaml_block = "\n".join(lines[1:end_idx])
        
        for match in metadata_pattern.finditer(yaml_block):
            key, value = match.groups()
            key = key.lower()
            
            # Yalnızca title, description ve author'ı al
            if key in metadata:
                metadata[key] = value.strip()
    
    return metadata

def render_markdown(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    metadata = extract_metadata(md_content)
    
    # Markdown'dan HTML'ye çevirme (başlık ve açıklama dışında kalan kısmı)
    # Başlık ve metadata arasındaki kısmı çıkarıyoruz
    content_start = md_content.find('---', md_content.find('---') + 1) + 3
    md_content = md_content[content_start:].strip()
    html_content = markdown.markdown(md_content)
    
    # HTML dosyasını oluşturma (title, description ve author metadataları kullanarak)
    html_output = HTML_TEMPLATE.format(
        title=metadata["title"],
        description=metadata["description"],
        author=metadata["author"],
        content=html_content
    )
    html_path = "temp_output.html"
    
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_output)
    
    # Tarayıcıda açma
    webbrowser.open("file://" + os.path.abspath(html_path))

if __name__ == "__main__":
    file_path = input("Dosyanızı sürükleyin ve Enter'a basın: ").strip().strip('"')
    
    if os.path.isfile(file_path) and file_path.endswith(".md"):
        render_markdown(file_path)
    else:
        print("Geçerli bir Markdown dosyası sürükleyip bırakın.")
