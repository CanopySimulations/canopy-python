import canopy


def get_default_config_path(
        session: canopy.Session,
        config_type: str,
        document_name: str):

    config_type_metadata = session.study_types.get_config_type_metadata(config_type)
    return '{}/{}.json'.format(config_type_metadata.plural_key, document_name)

