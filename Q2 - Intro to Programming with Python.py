#Trivia Challenge - Battle of Wits

class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options
        self.correct_option = correct_option

    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")
        print()

    def is_correct(self, player_answer):
        return player_answer == self.correct_option

def run_trivia_game(questions):
    player1_score = 0
    player2_score = 0

    for i, question in enumerate(questions, start=1):
        print(f"\nQuestion {i}:")
        question.display_question()

        # Get the player 1's answer
        while True:
            try:
                player1_answer = int(input("Player 1, enter your answer (1-4): "))
                if 1 <= player1_answer <= 4:
                    break
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if question.is_correct(player1_answer):
            player1_score += 1

        # Get player 2's answer
        while True:
            try:
                player2_answer = int(input("Player 2, enter your answer (1-4): "))
                if 1 <= player2_answer <= 4:
                    
                else:
                    print("Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if question.is_correct(player2_answer):
            player2_score += 1

    print("\nGame Over! Results:")
    print(f"Player 1's Score: {player1_score}")
    print(f"Player 2's Score: {player2_score}")

    if player1_score > player2_score:
        print("Player 1 is the winner!")
    elif player2_score > player1_score:
        print("Player 2 is the winner!")
    else:
        print("It's a tie!")

if __name__ == "__main__":
    # Creating Question objects
    questions = [
        Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 3),
        Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], 1),
        # Add more questions here...
    ]

    # Run the trivia game with the list of questions
    run_trivia_game(questions)
