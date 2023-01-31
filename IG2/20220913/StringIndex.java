class StringIndex {
	public static void main(String[] args) {
		String string = "Computer Science";

		System.out.println("Original string: " + string);

		System.out.println("\nstring.charAt(0): \n" + tryit(string, 0));
		System.out.println("\nstring.charAt(1): \n" + tryit(string, 1));
		System.out.println("\nstring.charAt(15): \n" + tryit(string, 15));
		System.out.println("\nstring.charAt(16): \n" + tryit(string, 16));
		System.out.println("\nstring.charAt(-1): \n" + tryit(string, -1));
		System.out.println("\nstring.charAt(100): \n" + tryit(string, 100));
		System.out.println("\nstring.charAt(-100): \n" + tryit(string, -100));
	}

	public static String tryit(String text, int i) {
		String a;
		try {
			a = String.valueOf(text.charAt(i));
		} catch (Exception e) {
			a = String.valueOf(e);
		}
		return a;
	}
}