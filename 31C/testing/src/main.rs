fn main() {
    for i in 1..5 {
        println!("JESUS THANK YOU for the first loop - {} {}", i, i * i);
    }
    for i in 1..=10 {
        println!("JESUS THANK YOU for the second loop - {} {}", i, i * i);
    }
    for i in [1, 2, 3, 4, 5] {
        println!("JESUS THANK YOU for the third loop - {} {}", i, i * i);
    }

    loop {
        println!("JESUS THANK YOU for the fourth loop");
        break;
    }
}
