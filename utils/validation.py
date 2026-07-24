SUPPORTED_PROFILE = "ga5-incident-agent/v2"


def validate_profile(profile):

    if profile != SUPPORTED_PROFILE:
        return False

    return True
