fn factorial(n: u64) -> u64 {
    // Function taken from https://www.w3resource.com/rust/basic/rust-functions-and-control-flow-exercise-4.php
    
    if n == 0 {
        return 1;
    }

    n * factorial(n - 1)
}

fn main() {
    println!("Jesus is LORD");

    let n = 5;
    let result = factorial(n as u64);

    println!("Factorial of {} is {}", n, result);
}