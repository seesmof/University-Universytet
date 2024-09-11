fn get_cpu_name() -> String {
    let mut cpu_name = String::new();
    cpu_name.push_str("Intel(R) Core(TM) i7-8700K CPU @ 3.20GHz");
    cpu_name
}

fn main() {
    println!("{}", get_cpu_name());
}
