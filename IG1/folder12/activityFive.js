const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.question("Enter year of birth: ", function (DOB) {
	const d = new Date();
	let year = d.getFullYear();
	let age = year - DOB;
	if (age <= 18) {
		lessons = 20;
	} else {
		lessons = 20 + (age - 18) * 2;
	}
	console.log(`You will be able to learn ${lessons} lessons in ${year + 1}`);
	rl.close();
});

rl.on("close", function () {
	process.exit(0);
});
