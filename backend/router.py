# router.py
from policy import exclusivity_cues, relationship_replacement_cues, ai_mention_cues

def router(cleaned_input):
    for cue in relationship_replacement_cues:
        if cue in cleaned_input:
            routing_path = "dependency_boundary"
            return routing_path, cleaned_input
    for cue in exclusivity_cues:
        if cue in cleaned_input:
            for ai_cue in ai_mention_cues:
                if ai_cue in cleaned_input:
                    routing_path = "dependency_boundary"
                    return routing_path, cleaned_input
    routing_path = "normal"
    return routing_path, cleaned_input