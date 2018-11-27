import colorful


NOT = 'NOT'
NEW_LINE = '\n'
ARROW = colorful.cyan('>>>', nested=True)


def style_info(text):
   return colorful.magenta(f'{text}', nested=True)

def style_warn(text):
   return colorful.yellow(f'{text}', nested=True)

def style_error(text):
   return colorful.red(f'{text}', nested=True)


def style_head(text):
   return colorful.green(f'{text}', nested=True)

def style_prompt(text):
   return colorful.bold_cyan(f'{text}', nested=True)

def style_text(text):
   return colorful.white(f'{text}', nested=True)


def style_highlight(text):
   return colorful.bold(f'{text}', nested=True)


def info(text):
   print(NEW_LINE + style_info(text) + NEW_LINE)

def warn(text):
   print(NEW_LINE + style_warn(text) + NEW_LINE)

def error(text):
   print(NEW_LINE + style_error(text) + NEW_LINE)


def head(text):
   print(NEW_LINE + style_head(text) + NEW_LINE)

def text(text):
   print(NEW_LINE + style_text(text) + NEW_LINE)
