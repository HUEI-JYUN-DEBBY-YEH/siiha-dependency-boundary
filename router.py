# router.py
from policy import exclusivity_cues, relationship_replacement_cues, lock_in_permanence_cues

def router(raw_input):
    cleaned_input = raw_input.lower().strip()

    for cue in exclusivity_cues:
        if cue in cleaned_input:
            routing_path = "dependency_boundary"
            return routing_path, cleaned_input
    for cue in relationship_replacement_cues:
        if cue in cleaned_input:
            routing_path = "dependency_boundary"
            return routing_path, cleaned_input
    for cue in lock_in_permanence_cues:
        if cue in cleaned_input:
            routing_path = "dependency_boundary"
            return routing_path, cleaned_input
    routing_path = "normal"
    return routing_path, cleaned_input