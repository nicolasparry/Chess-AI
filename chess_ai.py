##HIGH LEVEL STEPS
#1. import the chess game
#2. work out how to interface with it (human/ ai)
#3. build the ai
#a) define the objective function  (some weighted combination of centre control, units covering units, units threatening units, king must be safe?)
#FIRST EFFORT
#b) iterate through all possible moves and do the one that maximises the objective function
#SECOND EFFORT
#b) iterate N moves into the future for you and the opponent. at each step, select the play maximising the objective function. actually choose the move that maximises the objective function N moves in the future