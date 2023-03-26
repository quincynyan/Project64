import java.util.Scanner;

class activitySix {
	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter first number: ");
		int num1 = myObj.nextInt();
		System.out.println("Enter second number: ");
		int num2 = myObj.nextInt();
		myObj.close();
		System.out.println(sum(num1, num2));
	}

	static String sum(int num1, int num2) {
		int sum = 0;
		for (int i = num1; i <= num2; i++) {
			sum = sum + i;
		}
		return "The sum of the numbers between " + num1 + " and " + num2 + " is " + sum;
	}
}
