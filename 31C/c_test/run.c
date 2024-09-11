#include <stdio.h>
#include <stdint.h>
#include <time.h>

static inline uint64_t read_tsc() {
    uint32_t lo, hi;
    __asm__ __volatile__ (
        "rdtsc" 
        : "=a"(lo), "=d"(hi)
    );
    return ((uint64_t)hi << 32) | lo;
}

int main() {
    const int iterations = 100000000; // Number of iterations for the loop
    uint64_t start, end;
    clock_t start_time, end_time;

    // Start measuring TSC
    start = read_tsc();
    
    // Start measuring time
    start_time = clock();

    // Perform a simple operation in a loop
    for (int i = 0; i < iterations; i++) {
        // Simple operation
        volatile int temp = i * 2; // Prevent optimization
    }

    // End measuring time
    end_time = clock();
    end = read_tsc();

    // Calculate elapsed time in seconds
    double elapsed_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;

    // Calculate CPU speed in MHz
    uint64_t cycles_taken = end - start;
    double cpu_speed_mhz = (cycles_taken / elapsed_time) / 1e6; // Convert to MHz

    printf("Estimated CPU Speed: %.2f MHz\n", cpu_speed_mhz);
    return 0;
}