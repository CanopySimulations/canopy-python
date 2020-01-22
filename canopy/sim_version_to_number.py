
def sim_version_to_number(sim_version: str):
    if sim_version.startswith('1.'):
        return int(sim_version[2:])

    return 0
