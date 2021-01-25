# Python_HW2_Q1

Write a python program that plays a game “guess the number” as follows: The program
chooses the number to be guessed by selecting an integer at random in the range 1 to
1000. The program then types:
 I have a number between 1 to 1000.
 Can you guess my number?
 Please type your first guess.
The player then types the first guess. The program responds with one of the following.
 Excellent!! You guessed the number!!!
Would you like to play again (y or n)?
 Too high. Try again.
 Too low. Try again.
If the player’s guess is incorrect, you should loop (keep telling the player Too low or Too
high) until the player finally gets the number right. Additionally, the program should count
the number of guesses the player makes. If the player makes more than 10 guesses, then
print “You should be able to do better!!!”, if he/she makes 10 guesses then print “Ahah!
You know the secret!”, otherwise print “Either you know the secret or you got lucky!”.
