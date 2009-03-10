"""
Lexers for use with Pygments, a source code highlighter.
"""

from pygments.lexer import RegexLexer, include
from pygments.token import Comment, Keyword, Name, Number, Operator, \
                           Punctuation, String, Text


class ThriftLexer(RegexLexer):
    """
    Lexer for Apache Thrift source IDL
    """
    name = 'Thrift'
    aliases = ['thrift']
    filenames = ['*.thrift']
    mimetypes = ['text/x-thrift']

    tokens = {
        'root': [
            include('whitespace'),
            (r'#.*$', Comment),
            (r'//.*?\n', Comment),
            (r'/\*[\w\W]*?\*/', Comment.Multiline),
            (r'[=]', Operator),
            (r'[(){},:.<>]', Punctuation),
            (r'"(\\\\|\\"|[^"\n])*["\n]', String),
            (r'\'(\\\\|\\\'|[^\'\n])*[\'\n]', String),
            include('keywords'),
            include('numbers'),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', Name),
        ],
        'whitespace': [
            (r'\n', Text),
            (r'\s+', Text),
        ],
        'keywords': [
            (r'(async|extends|namespace|optional|required|throws)\b', Keyword),
            (r'(const|enum|exception|service|struct|typedef)\b', Keyword),
            (r'(void|bool|byte|i16|i32|i64|double|string|binary)\b', Keyword.Type),
            (r'(map|list|set)\b', Keyword.Type),
            (r'(abstract|and|args|as|assert|break)\b', Keyword.Reserved),
            (r'(case|class|continue|declare|def|default)\b', Keyword.Reserved),
            (r'(del|delete|do|elif|else|elseif|except)\b', Keyword.Reserved),
            (r'(exec|false|finally|float|for|foreach)\b', Keyword.Reserved),
            (r'(function|global|goto|if|implements)\b', Keyword.Reserved),
            (r'(import|in|inline|instanceof|interface)\b', Keyword.Reserved),
            (r'(is|lambda|native|new|not|or|pass|public)\b', Keyword.Reserved),
            (r'(print|private|protected|raise|return)\b', Keyword.Reserved),
            (r'(sizeof|static|switch|synchronized|this)\b', Keyword.Reserved),
            (r'(throw|transient|true|try|unsigned|var)\b', Keyword.Reserved),
            (r'(virtual|volatile|while|with|union|yield)\b', Keyword.Reserved),
        ],
        'numbers': [
            (r'\d+\.?\d*|\d*\.\d+', Number.Float),
            (r'0[xX][a-fA-F0-9]+', Number.Hex),
            (r'\d+', Number.Integer),
        ]
    }
