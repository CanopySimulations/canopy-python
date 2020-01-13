from __future__ import absolute_import

import canopy


def get_study_document(session: canopy.Session, canopy_document: canopy.swagger.CanopyDocument) -> canopy.swagger.StudyDocument:
    # We access the protected member here to save us modifying the swagger generated code.
    return session.client._ApiClient__deserialize(canopy_document.data, 'StudyDocument')
