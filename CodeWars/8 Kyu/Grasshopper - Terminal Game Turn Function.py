def do_turn():
    steps = [roll_dice, move, combat, 
             get_coins, buy_health, print_status]
    
    for step in steps:
        step()