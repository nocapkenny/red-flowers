# environment.py
from django_tex.environment import environment

def do_latex_escape(value):
    return (value
        .replace("\\", "\\textbackslash ")
        .replace('\n', '\\linebreak ')
        .replace("÷", "-")
        .replace('&', '\\&')
        .replace('$', '\\$')
        .replace('%', '\\%')
        .replace('#', '\\#')
        .replace('_', '\\_')
        .replace('{', '\\{')
        .replace('}', '\\}')
        .replace('₽', 'P')
        .replace('"','')
        .replace('°', '$^\circ$')
        .replace('¬', '$-$')
            .replace('" ', '"\, ')
        )
def format_datetime(value, format='medium'):
    return value.strftime('%d.%m.%Y')

def my_environment(**options):
    env = environment(**options)
    env.filters.update({
        'latex_escape': do_latex_escape,
        'format_datetime':format_datetime,
    })
    return env
