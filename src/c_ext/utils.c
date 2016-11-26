#include <stdlib.h>
#include <stdint.h>

uint32_t *make_u32a(uint32_t size)
{
        uint32_t *arr = calloc(size, sizeof(*arr));
        return arr;
}

uint32_t *make_u32r(uint32_t size)
{
        uint32_t i, *arr = make_u32a(size);

        if (arr != NULL) {
            for (i = 0; i < size; i++) {
                arr[i] = i;
            }
        }

        return arr;
}

uint32_t sum_u32a(uint32_t *arr, uint32_t len)
{
        uint32_t i, acc = 0;

        for (i = 0; i < len; i++) {
                acc += arr[i];
        }
        return acc;
}
