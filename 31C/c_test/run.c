#include <stdio.h>
#include <time.h>

double get_cpu_speed()
{
  clock_t start = clock();
  for (int i = 0; i < 100000000; i++)
  {
  }
  clock_t end = clock();

  double elapsed_time = (double)(end - start) / CLOCKS_PER_SEC;

  return elapsed_time;
}

int main()
{
  int cpu_speed = 0;
  int cpu_cores = 0;
  int cpu_threads = 0;

  int ram_usage = 0;
  int ram_total = 0;
  int ram_speed = 0;

  int gpu_usage = 0;
  int gpu_memory = 0;
  int gpu_temperature = 0;

  int disk_usage = 0;
  int disk_total = 0;
  int disk_speed = 0;

  return 0;
}