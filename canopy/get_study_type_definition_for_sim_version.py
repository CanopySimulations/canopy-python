from typing import Optional

import canopy


def get_study_type_definition_for_sim_version(
        item: canopy.openapi.StudyTypeDefinition,
        sim_version: Optional[str] = None) -> canopy.openapi.StudyTypeDefinition:

    if item.previous_definitions is not None and sim_version is not None:
        numeric_sim_version = canopy.sim_version_to_number(sim_version)

        for previous_study_type in item.previous_definitions:
            previous_numeric_sim_version = canopy.sim_version_to_number(previous_study_type.sim_version)
            if previous_numeric_sim_version >= numeric_sim_version:
                return previous_study_type.definition

    return item
