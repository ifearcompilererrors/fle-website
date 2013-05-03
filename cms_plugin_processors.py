# see http://readthedocs.org/docs/django-cms/develop/extending_cms/custom_plugins.html#plugin-processors

def wrap_in_div(instance, placeholder, rendered_content, original_context):
    '''
    This plugin processor wraps each plugin's output in a div 
    '''
    # Plugins embedded in Text should remain unchanged in order not to break output
    if (instance._render_meta.text_enabled and instance.parent): # or placeholder.slot != 'portfolio':
        return rendered_content
    else:
        from django.template import Context, Template
        t = Template('<div class="plugin_item">{{ content|safe }}<div style="clear:both;"></div></div>\n');
        c = Context({'content': rendered_content })
        return t.render(c)

