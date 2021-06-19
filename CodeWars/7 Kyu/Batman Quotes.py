class BatmanQuotes(object):

    def get_quote(quotes, hero):
        return f"{('Batman', 'Joker', 'Robin')['BJR'.index(hero[0])]}: {quotes[int(min(hero))]}"