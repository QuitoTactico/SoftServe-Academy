from django import template

register = template.Library()


@register.filter
def get_flag(lang_flag, language_code):
    """Retrieve the flag image path based on the language code."""
    return lang_flag.get(
        language_code, "images/flags/xx.svg" # Provide a default flag if not found
    )  
