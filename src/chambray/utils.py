from django.utils.html import format_html

def get_svg_content(the_file=None):
    ret = '<span>Have a beer :-)</span>'
    f = the_file.file.open(mode='r')
    ret = f.read()
    f.close()
    return format_html(ret)
