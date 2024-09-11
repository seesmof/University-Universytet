use std::arch::asm;

fn read_tsc() -> u64 {
    let lo: u32;
    let hi: u32;
    unsafe {
        asm!(
            "rdtsc",          // Read Time Stamp Counter
            out("eax") lo,    // Low 32 bits in EAX
            out("edx") hi,    // High 32 bits in EDX
        );
    }
    ((hi as u64) << 32) | (lo as u64) // Combine high and low parts
}

fn main() {
    const ITERATIONS: u64 = 100_000_000; // Number of iterations for the loop
    let start_cycles = read_tsc();

    // Perform a simple operation in a loop
    for i in 0..ITERATIONS {
        let _temp = i * 2; // Simple operation
    }

    let end_cycles = read_tsc();

    // Calculate CPU speed in MHz
    let cycles_taken = end_cycles - start_cycles;
    let elapsed_time = ITERATIONS as f64; // Assuming 1 cycle per operation for simplicity
    let cpu_speed_mhz = (cycles_taken as f64 / elapsed_time) / 1_000_000.0;

    println!("Estimated CPU Speed: {:.2} MHz", cpu_speed_mhz);
}
