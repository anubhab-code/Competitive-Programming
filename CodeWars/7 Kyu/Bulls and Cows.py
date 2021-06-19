class BullsAndCows:
    def __init__(self, n):
        if not isinstance(n, int) or n < 0 or len(str(n)) != 4 or len(set(str(n))) != 4:
            raise ValueError
        self.secret = n
        self.turns = 8
        self.win = False
    
    def compare_with(self, n):
        if self.win :
            return "You already won!"
        if self.turns <= 0:
            return "Sorry, you're out of turns!"
        if not isinstance(n, int) or n < 0 or len(str(n)) != 4 or len(set(str(n))) != 4:
            raise ValueError
        
        if n == self.secret:
            self.turns -= 1
            self.win = True
            return "You win!"
        bulls, cows = 0, 0
        sec = str(self.secret)
        for i,d in enumerate(str(n)):
            if d == sec[i]:
                bulls += 1
            elif d in sec:
                cows += 1
        self.turns -= 1
        if bulls == 1:
            result = f"{bulls} bull "
        else:
            result = f"{bulls} bulls "
        if cows == 1:
            result += f"and {cows} cow"
        else: 
            result += f"and {cows} cows"
        return result