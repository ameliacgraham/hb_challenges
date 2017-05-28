def snake_to_camel(variable_name):
    """Given a variable name in snake_case, return camelCase of name."""

    camel = ""
    words = variable_name.split('_')
    camel += words[0]
    for word in words[1:]:
        camel += word.capitalize()

    return camel

print snake_to_camel("variable_name")