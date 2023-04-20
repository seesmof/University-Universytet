float MyFunction(int number)
{
    float result = 1
    for (int a = 0; a < number; a++)
    {
        result = result * (a < 10 ? 2 : 1.5);
    }
    return result;
}