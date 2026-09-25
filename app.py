import gradio as gr, os

KNOWLEDGE = """
PIECE 30 WORD MADE FLESH: Thoughts given form, speech sets direction for consciousness. Death/life in power of tongue. Words are crystallized vibrations amplified. Stories you tell about yourself become lens. Change how you speak about self, miracles begin. Synchronicity. Man who thinks he can and cannot are both right.

PIECE 29 REPROGRAMMING: Blood pumping ferociously, infinite possibilities, go to backend rewrite script. New strings, variables, functions, brand new commands. Cascaded concatenations. Error returns, maliciously corrupted drives, need bug search, virus scan. Rebuild from scratch. Power to create immortal worlds.

PIECE 28 SPEAKER: Life changer, destinies on structure of every word. Contagious energy. Cadence of God, hand ready writer, pen skilled poet, voice great commander. Uses silence as weapon so whisper becomes loudest. Like water adapts, under pressure becomes deadly spear. Art of war is Speaking. Lips coated gold. Words are spells breaking spells.

PIECE 22 WORDS: Finally Words weapon massive destruction unlimited creation. Crafting Creation/Destruction Joy/Sorrow fiery arrows breakdown generational walls. Farmer sowing seeds fertile grounds. Pain dragon coiling? Pain is teacher pushes beyond comfort. Fire consumes within burns fears ash. Hunger for more fire.

VISION: Need Vision over talent, see yourself doing it first in details. To stop habit, see self NOT doing it. If cannot fathom, cannot become.

REALITY: Hits hard, chains heavy around arms, sack cement on chest, bone stuck throat. Movie you can't stop acting, script own writing. Only death separates.

PIECE 17 STOIC FAMILY: Epictetus - Men disturbed not by things but opinion. Be cheerful, tolerant, best interpretation, act as if success inevitable, smile 3x, react calmly, ignore unchangeable facts. Happiness = problems + attitude ready for action. Fear to fight. Protective structure vs modern world. They broke extended family. Now 1 function/year you avoid. Isolated chasing car/house/status for respect - least important. Shame sinks teeth, pride blocks humility. Family teaches happiness from within. Child cures depression: lights up when you return, curiosity makes problems disappear, rolling laughter, wonder, no grudge, Jet to palace to meal, crying laughing same person. Most fulfilling.

PIECE 16 WILL: How many volts to smoke you from deep sleep? You have everything - will of mind! Creative spontaneous from within. You are all it takes: Disgust Desire Decision. Path no lion threaded, chicken never knows. Voyage every man alone into destiny.

PIECE 14 GAME: Man must bring value. Life is game, many not playing controller in other hands. Like Naruto/Solo Leveling chakra cultivated daily. Imagine levels above heads. Level up, rack points, ascend pyramid or settle scraps. Pick up control pad press start. Master terrain. Select YOUR character, don't play another's. Hone own abilities.

PIECE 13 ROCK BOTTOM: Hit rock bottom? Where else but up? Forward unto prize, tunnel vision, aim deadly sharp shooter, looking unto Jesus author finisher. Not outside but inside fight. From victim to giver - not asking handouts but giving gifts. Sharpened self esteem. Words have new deeper meaning: faith love patience etc. Need conscious action, paint vivid picture of self you crave, opposite of self you disgust. 4D sculpture, 10000 hours to unlock genius Pandora box supernatural powers way of sword way of pen fingers taught battle arm taught war. Look up hills help comes. Pattern wrong switch up. Time essence.

PIECE 8 I AM: Desperate need for father instruction. At impasse: I am Spirit Son Father. I am God reflection. Journey without fixed destination realms outside time space. Search God for God. Ledge new threshold need faith to fly. Flesh and Time only burdens spirit not bound. Father Son one same Spirit within Man. Made Image Likeness.

PIECE 5 KNOWLEDGE: Knowledge sweeter than honey stimulating than physical sensation. Love bonds us, atoms joined, binds all creation. Language of love interfaces soul. Brings dead spirit to life. Sets free ageless bondage, arms tools, power transformation corrects teaches righteousness opens channels immense power.
"""

def search(q):
    words = q.lower().split()
    best = sorted(KNOWLEDGE.split("PIECE"), key=lambda c: sum(w in c.lower() for w in words), reverse=True)[:2]
    return "\n\n".join(best)

def chat(message, history):
    ctx = search(message)
    return f"🔥 DAVID AI — {len(KNOWLEDGE.split('PIECE'))} pieces trained\n\nYou: {message}\n\nFrom my actual writings:\n{ctx[:1800]}\n\nMy take: {ctx[:300]}... Turn fear to fight. Word to flesh. Pick your character and level up."

with gr.Blocks() as demo:
    gr.Markdown("# DAVID ALEXANDER AI 🔥\n*I set myself ablaze*\nTrained on 13+ pieces - Stoic, Hacker, Speaker, Spirit")
    gr.ChatInterface(fn=chat, examples=["I'm at rock bottom", "I feel isolated", "How to reprogram mind?", "What is reality?"])

demo.launch(server_name="0.0.0.0", server_port=int(os.environ.get("PORT", 7860)))
