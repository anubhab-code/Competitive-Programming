def cog_RPM(cogs):
    return cogs[0] / cogs[-1] * (-1) ** len(cogs+[1])