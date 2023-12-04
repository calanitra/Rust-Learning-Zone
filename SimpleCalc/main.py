use std::io;

fn main() {
     // Read the input line from the user
     let mut input = String::new();

     println!("Enter the first number:");
     io::stdin().read_line(&mut input).expect("Error reading line");

     // Convert the string to a number using the trim() method to remove extra spaces and newlines
     let num1: f64 = input.trim().parse().expect("Error converting string to number");

     // Clear the input variable before the next input
     input.clear();

     println!("Enter the second number:");
     io::stdin().read_line(&mut input).expect("Error reading line");

     let num2: f64 = input.trim().parse().expect("Error converting string to number");

     // Perform the addition operation
     let sum = num1 + num2;

     // Print the result
     println!("Sum: {}", sum);
}
