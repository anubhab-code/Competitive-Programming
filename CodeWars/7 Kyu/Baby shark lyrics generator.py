def baby_shark_lyrics():
    a = [f"{w} shark" for w in "Baby Mommy Daddy Grandma Grandpa".split()] + ["Let's go hunt"]
    b = [f"{s},{' doo' * 6}\n" * 3 + f"{s}!\n" for s in a]
    return "".join(b) + "Run away,…"