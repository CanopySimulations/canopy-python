from __future__ import absolute_import

import swagger_client
import canopy


def get_study_document(session: canopy.Session, canopy_document: swagger_client.CanopyDocument) -> swagger_client.StudyDocument:
    # We access the protected member here to save us modifying the swagger generated code.
    return session.client._ApiClient__deserialize(canopy_document.data, 'StudyDocument')
