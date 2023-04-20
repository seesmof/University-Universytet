void Sort(int[] array)
{
    for (j = 0; j < n - 1; j++)
    {
        iMin = j;
        for (i = j + 1; i < n; i++)
        {
            if (array[i] < array[iMin])
                iMin = i;
        }
            if (iMin != j)
        swap(array[j], array[iMin];
    }
}