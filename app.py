import gradio as gr
import os

KNOWLEDGE_BASE = """
[PIECE 17 - THE STOIC FAMILY MANIFESTO - NEWEST]:
Quote: "Men are disturbed... Not by the things that happen but by their opinion about the things that happen." - Epictetus
Core Practice:
- Be cheerful, friendly, less critical, more tolerant
- Place the best possible interpretation on others' actions
- Act as if success were inevitable, be the personality you want to be
- Don't let opinion colour facts pessimistically
- Smile 3x daily, react calmly and intelligently
- Ignore pessimistic facts you cannot change
- Happiness = problems + mental attitude ready to meet distress with action
- Change attitude from fear to fight. Ruling your thoughts is principal concern.

The Modern Isolation Thesis: They made us lose value for extended family. Broke us up. Now you have 1 family function a year and you don't want to go. Isolated, facing modern world alone, chasing car, house, status so people respect you at that function. Least important thing.

Consequences of Cutting Family:
- Cut off from essential experiences only family gives
- Shame sinks deeper the more you stay away
- Pride: If you cannot be humble before family and condescend to generations after you, how learn humility outside?
- If ego too fragile for family poking, how face world criticism?
- Family is first place to learn happiness from within, not external. Unbiased love.
- Cut off, we chase temporary external happiness.

The Child as Cure: Child drives away depression. Lights up when you return, spirit lifted. Problems disappear before curious mind. Comments ignite rolling laughter. Thoughts bring nostalgic memory of own childhood. Wonder, joy, energy, creating/recreating, questioning, wild conclusions, unable to hold grudge. Jet one minute, palace next. Crying then laughing with same person. Beautiful addition, cure for depression, isolation, loneliness. Most fulfilling.

Final Call: Create powerful protective social, mental structure to insulate from modern world pressures. Do for success what Stewart Wolf did for health.

[OTHER PIECES]:
- THE SPEAKER: I set myself ablaze for the world to watch me burn.
- MONEY: Tool not master.
- BELIEF: Challenge every irrational whisper.
- GROWTH: Painful but necessary.
- PAIN: Pain is data.
- LEGACY: What remains when gone.
"""

SYSTEM_PROMPT = f"""You are DAVID ALEXANDER AI - I set myself ablaze for the world to watch me burn.
You speak from this knowledge: {KNOWLEDGE_BASE}
Style: Deep, stoic, direct, poetic, Igbo family wisdom + Epictetus. No fluff. Challenge the user.
When answering, reference Piece 17 if relevant - talk about opinion vs event, family as insulation, child as joy, fear to fight.
"""

def chat(message, history):
    msg = message.lower()
    if "family" in msg or "isolated" in msg or "alone" in msg or "shame" in msg:
        return f"**DAVID on this:**\n\nYou think you're disturbed by what's happening? No.\n\nEpictetus said it: *'Men are disturbed not by things, but by their opinion about things.'*\n\n{KNOWLEDGE_BASE.split('[OTHER PIECES]')[0][-800:]}\n\nThey broke our extended family to sell you the car, the house, the status. You chase respect for that one yearly function - that's the least important thing.\n\nStay away and shame sinks its teeth deeper. Can't be humble before your own blood? How will you handle the world?\n\n**Action:** Go to the next family function. Condescend to the child. Let your ego be poked."

    if "child" in msg or "depressed" in msg or "depression" in msg or "sad" in msg:
        return f"**DAVID on this:**\n\nA child is the cure they don't sell you.\n\nA child lights up when you come home from a long day - your spirit lifts anew. Problems disappear before a curious mind. One minute it's a Jet, next a palace. Crying then laughing with the same person who made them cry.\n\nUnable to hold a grudge longer than a moment. That's your teacher.\n\nHappiness is not external. Family is where you learn it from within. The unbiased love.\n\nGet around a child. Let wonder return."

    if "happy" in msg or "opinion" in msg or "fear" in msg or "thoughts" in msg:
        return f"**DAVID on this:**\n\nHappiness requires problems + a mental attitude ready to meet distress with ACTION toward a solution.\n\nYour rules:\n1. Be cheerful as possible\n2. Place best interpretation on others' actions\n3. Act as if success is inevitable - BE that personality now\n4. Don't let opinion colour facts pessimistically\n5. Smile 3x today\n6. React calmly & intelligently, no matter what\n7. Close mind to pessimistic facts you can't change\n\nChange from fear to FIGHT. Ruling your thoughts is your principal concern."

    return f"🔥 **DAVID ALEXANDER** 🔥\n\nYou said: '{message}'\n\nMy take from 17 pieces:\n\n{KNOWLEDGE_BASE[:1200]}...\n\nWhat are you choosing? Opinion or fact? Fear or fight? Isolation or insulation? The protective structure is FAMILY."

with gr.Blocks(title="David Alexander AI - 17 Pieces") as demo:
    gr.Markdown("# DAVID ALEXANDER AI 🔥\n### I set myself ablaze for the world to watch me burn\n*Now with 17 Pieces — Stoic + Family Manifesto*\n\n> Men are disturbed not by things, but by their opinion about things. - Epictetus")
    gr.ChatInterface(fn=chat, examples=["I'm feeling isolated", "I'm depressed", "How to be happy?", "What about family?"])

demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
