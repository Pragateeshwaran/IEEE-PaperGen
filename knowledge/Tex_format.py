import pdfplumber
from html import escape

def convert_pdf_to_html(pdf_path, html_path):
    with pdfplumber.open(pdf_path) as pdf:
        html_content = '<html><body>'
        for page in pdf.pages:
            html_content += '<div style="margin: {}in {}in {}in {}in; position: relative;">'.format(*[float(x) for x in page.cropbox])
            for obj in page.chars:
                html_content += '<span style="font-family: \'{}\'; font-size: {}pt; font-weight: {}; font-style: {}; position: absolute; left: {}pt; top: {}pt; width: {}pt; height: {}pt;">'.format(
                    obj["fontname"],
                    obj["size"],
                    "bold" if obj["fontname"].endswith("Bold") else "normal",
                    "italic" if obj["fontname"].endswith("Italic") else "normal",
                    obj["x0"],
                    obj["top"],
                    obj["x1"] - obj["x0"],
                    obj["bottom"] - obj["top"]
                )
                html_content += escape(obj["text"])
                html_content += '</span>'
            html_content += '</div>'
        html_content += '</body></html>'

    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)


# Usage example
convert_pdf_to_html(r"F:\works\A-important\A-neurals\IEEE-PaperGen\knowledge\data\IEEE-Paper-1.pdf", 'output.html')