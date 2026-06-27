
#Python Programming Project 4 - The General Knowledge Quiz

score = 0

print("=" * 50)
print("   WELCOME TO THE GENERAL KNOWLEDGE QUIZ")
print("=" * 50)
print("Answer each question. Your score will be tallied at the end.\n")

# ----------------------------------------------------------------------
# QUESTION BLOCK 1
# ----------------------------------------------------------------------

answer1 = input("Q1. What is the capital of France? ")
answer1 = answer1.strip().lower()          

if answer1 == "paris":
    print("Correct! ✅\n")
    score += 1
else:
    print("Incorrect. ❌ The correct answer was 'Paris'.\n")


# ----------------------------------------------------------------------
# QUESTION BLOCK 2
# ----------------------------------------------------------------------
answer2 = input("Q2. Which planet is known as the Red Planet? ")
answer2 = answer2.strip().lower()

if answer2 == "mars":
    print("Correct! ✅\n")
    score += 1
else:
    print("Incorrect. ❌ The correct answer was 'Mars'.\n")


# ----------------------------------------------------------------------
# QUESTION BLOCK 3
# ----------------------------------------------------------------------
answer3 = input("Q3. Who developed the theory of relativity? ")
answer3 = answer3.strip().lower()

if answer3 == "einstein" or answer3 == "albert einstein":
    print("Correct! ✅\n")
    score += 1
else:
    print("Incorrect. ❌ The correct answer was 'Albert Einstein'.\n")

print("=" * 50)
print(f"QUIZ COMPLETE! Your final score is: {score:>2} / 3")
print("=" * 50)
