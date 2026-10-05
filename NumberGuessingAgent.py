def guessing_agent(low,high,secret):
    attempts=0
    while low<=high:
        guess=(low+high)//2
        attempts+=1
        print(f"Attempt {attempts}: Agent guesses {guess}")
        if guess==secret:
            print(f"Guessed correctly in {attempts} attempts! Number was {secret}.")
            return attempts
        elif guess<secret:
            print("Feedback: higher")
            low=guess+1
        else:
            print("Feedback: lower")
            high=guess-1
    print("No valid number found in range.")
    return None

guessing_agent(1,100,42)