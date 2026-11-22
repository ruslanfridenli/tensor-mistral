# markov muse — n-gram text generator (python)
import random
CORPUS_EN = """the quick brown fox jumps over the lazy dog and runs through the forest while the wind moves through the trees and the river flows steadily toward the sea. every morning the sun rises above the hills and paints the sky in shades of gold and violet. scientists study the stars and discover new worlds beyond our solar system every day. music has the power to move people across cultures and centuries. the best ideas often arrive when we least expect them. practice makes progress and progress makes perfect. a journey of a thousand miles begins with a single step. technology transforms how we learn work and connect with each other around the world."""
CORPUS_DE = """die schnelle braune fuchs springt über den faulen hund und rennt durch den wald während der wind durch die bäume weht und der fluss stetig zum meer fließt. jeden morgen geht die sonne über den hügeln auf und malt den himmel in tönen aus gold und violett. wissenschaftler erforschen die sterne und entdecken jeden tag neue welten jenseits unseres sonnesystems. musik hat die kraft menschen über kulturen und jahrhunderte hinweg zu bewegen. die besten ideen kommen oft dann wenn wir sie am wenigsten erwarten. übung macht den meister und fortschritt macht perfekt. eine reise von tausend meilen beginnt mit einem einzigen schritt. technologie verändert wie wir lernen arbeiten und uns mit anderen auf der ganzen welt verbinden."""
def build(corpus, n=3):
    words = corpus.split()
    grams = {}
    for i in range(len(words)-n):
        key = tuple(words[i:i+n-1])
        grams.setdefault(key, []).append(words[i+n-1])
    return grams, words
def generate(grams, words, length, temp, n=3):
    random.seed()
    start = tuple(random.sample(words, n-1)) if len(words)>=n-1 else tuple(words[:n-1])
    out = list(start)
    for _ in range(length):
        key = tuple(out[-(n-1):])
        nxts = grams.get(key)
        if not nxts:
            key = tuple(random.sample(words, n-1))
            nxts = grams.get(key, words)
        if temp <= 0:
            w = nxts[0]
        else:
            import math
            # temperature: lower = more predictable
            counts = {}
            for x in nxts: counts[x] = counts.get(x,0)+1
            pool = list(counts.keys())
            weights = [counts[x]**(1/max(temp,0.05)) for x in pool]
            w = random.choices(pool, weights=weights, k=1)[0]
        out.append(w)
    return ' '.join(out)
GRAMS = {'en': build(CORPUS_EN), 'de': build(CORPUS_DE)}
def gen_text(lang, length, temp):
    g, w = GRAMS[lang]
    return generate(g, w, int(length), float(temp))
