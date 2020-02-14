import canopy


def get_study_document(session: canopy.Session, canopy_document: canopy.openapi.CanopyDocument) -> canopy.openapi.StudyDocument:
    # We access the protected member here to save us modifying the swagger generated code.
    return session.sync_client._ApiClient__deserialize(canopy_document.data, 'StudyDocument')
