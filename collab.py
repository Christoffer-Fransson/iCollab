def scoreboard(round = 0, rounds = 0):
   rounds = rounds + round
   return rounds
  
run = 0
while run < 10:     
    round = scoreboard(round = 1)
    print(round)
    run = run + 1


