#!/usr/bin/python3


def do_create(self, arg):
    """Create a new instance of a class"""
    if not arg:
        print("** class name missing **")
        return

    args = arg.split()
    class_name = args[0]
    valid_params = {}

    if class_name not in classes:
        print("** class doesn't exist **")
        return

    for param in args[1:]:
        if '=' not in param:
            continue

        key, value = param.split('=')
        if not value:
            continue

        value = value.replace('_', ' ')

        # Check the value type and convert if necessary
        if value.startswith('"') and value.endswith('"'):
            # String value
            value = value[1:-1].replace('\\"', '"')
        elif '.' in value:
            try:
                # Float value
                value = float(value)
            except ValueError:
                continue
        else:
            try:
                # Integer value
                value = int(value)
            except ValueError:
                continue

        valid_params[key] = value

    # Create the new instance with the valid parameters
    instance = classes[class_name](**valid_params)
    instance.save()
    print(instance.id)
