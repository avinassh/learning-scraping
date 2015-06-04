import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

# uses mistune and produces a custom renderer for 
# mistune with pygments for code highlighting

class MyRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        formatter = HtmlFormatter()
        lexer = PythonLexer()
        return highlight(code, lexer, formatter)

def markdown_to_html(markdown_text):
    renderer = MyRenderer()
    md = mistune.Markdown(renderer=renderer)
    return md.render(markdown_text)