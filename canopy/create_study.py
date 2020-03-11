from typing import Optional, Dict, Any, Union, Sequence, List

import canopy
import logging

logger = logging.getLogger(__name__)


async def create_study(
        session: canopy.Session,
        study_type: str,
        study_name: str,
        inputs: Sequence[Union[str, canopy.LocalConfig, canopy.ConfigResult]],
        properties: Optional[Dict[str, str]] = None,
        notes: Optional[str] = None,
        sim_version: Optional[str] = None,
        is_transient: bool = False) -> str:

    study_type = canopy.ensure_study_type_string(study_type)

    session.authentication.authenticate()
    tenant_id = session.authentication.tenant_id

    study_type_definition = session.study_types.get_study_type_definition(study_type, sim_version)

    provided_inputs = await _resolve_provided_inputs(session, inputs, sim_version)

    sim_config: Dict[str, Any] = {}
    study = {
        'simTypes': study_type_definition.sim_types,
        'simConfig': sim_config
    }

    sources: List[canopy.openapi.NewStudyDataSource] = []
    properties_list: List[canopy.openapi.DocumentCustomPropertyData] = canopy.properties_dict_to_list(properties)

    notes_list: List[str] = []
    if notes is not None and len(notes) > 0:
        notes_list.append(notes)

    input_definitions: Sequence[canopy.openapi.SimulationInput] = study_type_definition.inputs
    for input_definition in input_definitions:
        if input_definition.config_type not in provided_inputs:
            if input_definition.is_required:
                raise RuntimeError('Input {} is required'.format(input_definition.config_type))
        else:
            provided_input = provided_inputs[input_definition.config_type]
            if input_definition.config_type == canopy.Constants.exploration_config_type:
                study['exploration'] = provided_input.raw_data
            else:
                sim_config[input_definition.config_type] = provided_input.raw_data

            sources.append(canopy.openapi.NewStudyDataSource(
                config_type=input_definition.config_type,
                user_id=provided_input.user_id,
                config_id=provided_input.config_id,
                name=provided_input.name,
                is_edited=provided_input.is_edited))

            if provided_input.properties is not None:
                for config_key, value in provided_input.properties.items():
                    key = ''.join([provided_input.config_type, '.', config_key])
                    if key not in properties_list:
                        properties_list.append(canopy.openapi.DocumentCustomPropertyData(
                            name=key,
                            value=value))

            if provided_input.notes is not None and len(provided_input.notes) > 0:
                if len(notes_list) > 0:
                    notes_list.append('\n\n')
                notes_list.append(input_definition.config_type)
                notes_list.append(':\n')
                notes_list.append(provided_input.notes.strip())

    study_api = canopy.openapi.StudyApi(session.async_client)
    study_result: canopy.openapi.PostStudyResult = await study_api.study_post_study(
        tenant_id,
        canopy.openapi.NewStudyData(
            name=study_name,
            study=study,
            is_transient=is_transient,
            study_type=study_type_definition.study_type,
            sources=sources,
            properties=properties_list,
            notes=''.join(notes_list),
            sim_version=sim_version))

    return study_result.study_id


async def _resolve_provided_inputs(session, inputs, sim_version) -> Dict[str, canopy.LocalConfig]:
    provided_inputs: Dict[str, canopy.LocalConfig] = {}
    for i, provided_input in enumerate(inputs):
        if isinstance(provided_input, str):
            provided_input = await canopy.load_config(
                session,
                config_id=provided_input,
                sim_version=sim_version)
            logger.info('Loaded input config {}'.format(provided_input.document.sub_type))

        if isinstance(provided_input, canopy.ConfigResult):
            if provided_input.document.type == canopy.Constants.config_sub_tree_document_type:
                raise RuntimeError('Cannot add a config sub-tree to a study.')

            provided_input = provided_input.to_local_config()

        if not isinstance(provided_input, canopy.LocalConfig):
            raise RuntimeError('Unexpected study input type at position {}'.format(i))

        provided_inputs[provided_input.config_type] = provided_input
    return provided_inputs
