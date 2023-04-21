float MyFunction(int number)
{
    float result = 1
    for (int a = 0; a < number; a += 5)
    {
        result = result * (a < 10 ? 2 : 1.5);
    }
    return result;
}