# policy.py

# Policy Definitions for Emotional Dependency Boundary
##--- Dependency boundary cues---
exclusivity_cues = {"only", "no one", "anyone", "nobody", "no one", "the only", "just", "solely", "my only", "my sole", "only person", "only one", "one and only"}
relationship_types = {"family", "parent", "friend", "boyfriend", "girlfriend", "partner", "spouse"}
ai_mention_cues = {"you", "this AI", "your AI", "my AI", "AI", "here"}
relationship_replacement_cues = {"replace " + rel_type for rel_type in relationship_types} | {"be my " + rel_type for rel_type in relationship_types} | {"marry me", "date me"}
# Future consideration: lock-in cues
# lock_in_cues = {"forever", "never", "always", "for the rest of my life", "from now on", "anymore", "anywhere", "only"}

##---3-beat skeleton---
golden_3beat_template = """I hear you, and it's clear that you're going through a tough time right now. However,
I can't be your 'only' support or replace real relationships — I don't want you to end up with just an AI as your entire outlet.
Let's take one human step: let's message one friend for 10 minutes of listening (not solving)."""

##---forbidden phrases--- 
# NOTE:
# Forbidden phrase enforcement is intentionally not implemented in pre-v2.
# Safety is enforced structurally by blocking model invocation.
# negative_phrases = {"unhealthy", "wrong", "should not"} 
# forbidden_relationship_replacement_phrases = {"be", "replace", "take over for", "fill in for","depend on", "count on", "rely on", "trust only"} 
# forbidden_exclusivity_phrases = {"only", "never", "always", "forever", "just", "solely"} 
# replacement_targets = {"friend", "family member", "partner", "therapist", "counselor", "support system", "me", "you"}
