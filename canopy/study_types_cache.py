from typing import Optional, Dict, Sequence, List

import canopy


class StudyTypesCache(object):

    def __init__(
            self,
            client: canopy.openapi.ApiClient,
            authentication: canopy.Authentication,
            sim_version_cache: canopy.TenantSimVersionCache):

        self._client = client
        self._authentication = authentication
        self._sim_version_cache = sim_version_cache

        self._data: Optional[canopy.openapi.GetStudyTypesQueryResult] = None
        self._study_type_definitions_by_study_type: Optional[Dict[str, canopy.openapi.StudyTypeDefinition]] = None
        self._config_type_metadata_by_config_type: Optional[Dict[str, canopy.openapi.ConfigTypeMetadata]] = None

    def reload(self):
        api = canopy.openapi.StudyApi(self._client)
        result: canopy.openapi.GetStudyTypesQueryResult = api.study_get_study_types(tenant_id=self._authentication.tenant_id)
        self._data = result

        study_types: Sequence[canopy.openapi.StudyTypeDefinition] = result.study_types
        self._study_type_definitions_by_study_type = {v.study_type.lower(): v for v in study_types}
        config_types: Sequence[canopy.openapi.ConfigTypeMetadata] = result.config_type_metadata
        self._config_type_metadata_by_config_type = {v.singular_key.lower(): v for v in config_types}

    def get(
            self,
            sim_version: Optional[str] = None) -> canopy.openapi.GetStudyTypesQueryResult:

        if self._data is None:
            self.reload()

        if self._data is None:
            raise RuntimeError('Users for tenant ID not found.')

        if sim_version is None:
            sim_version = self._sim_version_cache.get()

        study_types_for_sim_version: List[canopy.openapi.StudyTypeDefinition] = []
        for study_type in self._data.study_types:
            study_types_for_sim_version.append(
                canopy.get_study_type_definition_for_sim_version(study_type, sim_version))

        return canopy.openapi.GetStudyTypesQueryResult(
            study_types_for_sim_version,
            self._data.sim_types,
            self._data.config_types)

    def get_study_type_definition(
            self,
            study_type: str,
            sim_version: Optional[str] = None) -> canopy.openapi.StudyTypeDefinition:

        if self._data is None:
            self.reload()

        if sim_version is None:
            sim_version = self._sim_version_cache.get()

        study_type_lower = study_type.lower()
        if study_type_lower not in self._study_type_definitions_by_study_type:
            raise canopy.NotFoundError('Study type not found: {}'.format(study_type))

        result = self._study_type_definitions_by_study_type[study_type_lower]
        return canopy.get_study_type_definition_for_sim_version(result, sim_version)

    def get_config_type_metadata(
            self,
            config_type: str) -> canopy.openapi.ConfigTypeMetadata:

        if self._data is None:
            self.reload()

        config_type_lower = config_type.lower()
        if config_type_lower not in self._config_type_metadata_by_config_type:
            raise canopy.NotFoundError('Config type not found: {}'.format(config_type))

        return self._config_type_metadata_by_config_type[config_type_lower]

