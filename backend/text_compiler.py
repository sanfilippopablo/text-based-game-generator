from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import markdown
import re

class StepLinkPreprocessor(Preprocessor):
    def run(self, lines):
        global choices
        new_lines = []
        for line in lines:
            regex = re.compile(r'<\$([\s\w]*)\$>\(([\s\w]*)\)')
            groups = regex.findall(line)
            if groups:
                choices = groups
                new_line = re.sub(regex, r'[\1](\2.html)', line)
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        return new_lines

class StepLinkExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('steplinkpreprocessor', StepLinkPreprocessor(), '_begin')

def get_text_and_choices(text):
    global choices
    compiled = markdown.markdown(text, extensions=[StepLinkExtension()])
    return compiled, choices