import java.util.Scanner;

public class activityTen {
	public static void main(String[] args) {
		game();
		while (true) {
			System.out.println("Do you want to play again? (y/n)");
			Scanner myScanner = new Scanner(System.in);
			String answer = myScanner.nextLine();
			if (answer.equals("y")) {
				game();
			} else {
				myScanner.close();
				break;
			}
		}
	}

	static void game() {
		int randomNum = (int) (Math.random() * 100 + 1);
		System.out.println(randomNum);
		System.out.println("Guess a number between 1 and 100");
		Scanner myObj = new Scanner(System.in);
		int guess = myObj.nextInt();
		int guessCount = 1;
		while (guess != randomNum) {
			if (guess < randomNum) {
				System.out.println("Too low");
			} else if (guess > randomNum) {
				System.out.println("Too high");
			}
			guess = myObj.nextInt();
			guessCount++;
		}
		System.out.println("You guessed it!");
		System.out.println("It took you " + guessCount + " tries");
	}
}
