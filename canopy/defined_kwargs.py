def defined_kwargs(**kwargs):
    return {k: v for k, v in kwargs.items() if v is not None}
