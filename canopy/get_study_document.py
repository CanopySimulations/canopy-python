def get_study_document(session, canopy_document):
    # We access the protected member here to save us modifying the swagger generated code.
    return session.client._ApiClient__deserialize(canopy_document.data, 'StudyDocument')