STRIKE_SCORE = 10

def score_strike(arr):
	if len(arr) < 3:
		return (0, [])
	
	return (STRIKE_SCORE + arr[1] + arr[2], arr[1:])

def score_spare(arr):
	if len(arr) < 2:
		return (0,[])
	
	return (STRIKE_SCORE + arr[2], arr[2:])

def score_frame(arr):
	if len(arr) == 0:
		return (0, [])
	
	if arr[0] == STRIKE_SCORE:
		return score_strike(arr)
	
	if len(arr) >= 2 and arr[0] + arr[1] == STRIKE_SCORE:
		return score_spare(arr)
	
	if len(arr) < 2:
		return (0, [])
	
	return (arr[0] + arr[1], arr[2:])

def calculate_score(arr):
	if len(arr) == 0:
		return 0
	
	(score, leftover) = score_frame(arr)
	return score + calculate_score(leftover)
