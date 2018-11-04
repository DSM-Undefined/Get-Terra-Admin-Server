def param(name, description):
    return {
        'name': name,
        'description': description,
        'in': 'json',
        'type': 'str',
        'required': True
    }


def n_param(name, description):
    return {
        'name': name,
        'description': description,
        'in': 'json',
        'type': 'str',
        'required': False
    }
