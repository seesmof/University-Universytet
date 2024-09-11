#include <stdio.h>
int main()
{
  while (1)
  {
    // Update information each second
    sleep(1);

    // Output CPU information
    int cpu_cores = 4;
    printf("CPU: %d cores\n", cpu_cores);

    // Output RAM information
    int ram_size = 21333;
    printf("RAM: %d MB\n", ram_size);

    // Output GPU information
    char gpu_name[] = "GTX 1050 Ti";
    printf("GPU: %s\n", gpu_name);

    // Clear screen
    system("cls");
  }
}