
/**
 * AverageMark
 */

import java.util.Scanner;

public class AverageMark {

    public static void main(String[] args) {
        int total = 0;
        int numberEntered = 0;
        char anotherEntry = 'Y';
        Scanner input = new Scanner(System.in);
        while (anotherEntry == 'Y') {
            System.out.print("Enter a mark: ");
            int mark = input.nextInt();
            total = total + mark;
            numberEntered = numberEntered + 1;
            System.out.print("Do you want to enter another mark? (Y/N): ");
            anotherEntry = input.next().toUpperCase().charAt(0);
        }
        input.close();
        float average = total / numberEntered;
        System.out.println("The average mark is " + average);
    }
}