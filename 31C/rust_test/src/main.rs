use systemstat::{Platform, System};

fn main() {
    let sys = System::new();

    // Get CPU load
    match sys.cpu_load_aggregate() {
        Ok(cpu) => {
            // Wait for a moment to get a valid reading
            std::thread::sleep(std::time::Duration::from_millis(100));
            let load = cpu.done().unwrap();
            println!("CPU Load: {:.2}%", load.user * 100.0);
        }
        Err(e) => println!("Error getting CPU load: {}", e),
    }

    // Get CPU speed (in MHz)
    match sys.cpu_speed() {
        Ok(speed) => println!("CPU Speed: {} MHz", speed),
        Err(e) => println!("Error getting CPU speed: {}", e),
    }
}
