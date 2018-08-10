# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1533870534.2282994
_enable_loop = True
_template_filename = '/home/alstof/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/tag.tmpl'
_template_uri = 'tag.tmpl'
_source_encoding = 'utf-8'
_exports = ['content', 'extra_head']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        subcategories = _import_ns.get('subcategories', context.get('subcategories', UNDEFINED))
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        subcategories = _import_ns.get('subcategories', context.get('subcategories', UNDEFINED))
        def content():
            return render_content(context)
        description = _import_ns.get('description', context.get('description', UNDEFINED))
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<article class="tagpage">\n    <header>\n        <h1>')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</h1>\n')
        if description:
            __M_writer('            <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        if subcategories:
            __M_writer('        ')
            __M_writer(str(messages('Subcategories:')))
            __M_writer('\n        <ul>\n')
            for name, link in subcategories:
                __M_writer('            <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(filters.html_escape(str(name)))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('        <div class="metadata">\n            ')
        __M_writer(str(feeds_translations.feed_link(tag)))
        __M_writer('\n        </div>\n        ')
        __M_writer(str(feeds_translations.translation_link()))
        __M_writer('\n    </header>\n')
        if posts:
            __M_writer('        <ul class="postlist">\n')
            for post in posts:
                __M_writer('            <li><time class="listdate" datetime="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('" title="')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
                __M_writer('</time> <a href="')
                __M_writer(str(post.permalink()))
                __M_writer('" class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('<a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('</article>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        tag = _import_ns.get('tag', context.get('tag', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(tag)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"137": 5, "138": 6, "139": 6, "140": 7, "141": 7, "147": 141, "23": 3, "29": 0, "49": 2, "50": 3, "55": 8, "60": 39, "66": 11, "82": 11, "83": 14, "84": 14, "85": 15, "86": 16, "87": 16, "88": 16, "89": 18, "90": 19, "91": 19, "92": 19, "93": 21, "94": 22, "95": 22, "96": 22, "97": 22, "98": 22, "99": 24, "100": 26, "101": 27, "102": 27, "103": 29, "104": 29, "105": 31, "106": 32, "107": 33, "108": 34, "109": 34, "110": 34, "111": 34, "112": 34, "113": 34, "114": 34, "115": 34, "116": 34, "117": 34, "118": 34, "119": 36, "120": 38, "126": 5}, "uri": "tag.tmpl", "filename": "/home/alstof/nikola/lib/python3.5/site-packages/nikola/data/themes/base/templates/tag.tmpl", "source_encoding": "utf-8"}
__M_END_METADATA
"""