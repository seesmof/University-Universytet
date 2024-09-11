fn main() {
    let y = 13;
    let x = {
        let a = 10;
        println!("{}", a);
        a + y
    };
    println!("{}", x);
}
