use std::io;
use rand::Rng;

fn main() {
     // Generate a random number from 1 to 100
     let secret_number = rand::thread_rng().gen_range(1..101);

     println!("Welcome to the game 'Guess the number'!");

     loop {
         println!("Please enter your guess:");

         let mut guess = String::new();

         io::stdin().read_line(&mut guess).expect("Error reading line");

         // Convert the string to a number, ignoring errors
         let guess: u32 = match guess.trim().parse() {
             Ok(num) => num,
             Err(_) => continue,
         };

         println!("Your guess: {}", guess);

         // Check if the user guessed the number
         match guess.cmp(&secret_number) {
             std::cmp::Ordering::Less => println!("Too small!"),
             std::cmp::Ordering::Greater => println!("Too big!"),
             std::cmp::Ordering::Equal => {
                 println!("Congratulations! You guessed the number!");
                 break;
             }
         }
     }
}
