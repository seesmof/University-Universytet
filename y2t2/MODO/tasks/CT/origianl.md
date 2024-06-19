### scipy.integrate.trapezoid

```py
scipy.integrate.trapezoid(y, x=None, dx=1.0, axis=-1)
```

#### Description

Integrate along the given axis using the composite trapezoidal rule.

If x is provided, the integration happens in sequence along its elements - they are not sorted.

Integrate y (x) along each 1d slice on the given axis, compute $\int y(x) dx$. When x is specified, this integrates along the parametric curve, computing $\int_t y(t) dt = \int_t y(t) \frac{dx}{dt} |_{x=x(t)} dt$.

#### Arguments

| Name | Type | Description |
|-|-|-|
|x|array_like|Input array to integrate.|
|x|array_like, optional|The sample points corresponding to the y values. If x is None, the sample points are assumed to be evenly spaced dx apart. The default is None.|
|dx|scalar, optional|The spacing between sample points when x is None. The default is 1.0.|
|axis|int, optional|The axis along which to integrate.|

#### Returns

| Type | Type | Description |
|-|-|-|
|trapezoid|float or ndarray|Definite integral of y = n-dimensional array as approximated along a single axis by the trapezoidal rule. If y is a 1-dimensional array, then the result is a float. If n is greater than 1, then the result is an n-1 dimensional array.|

#### Examples

Importing necessary libraries for all the examples:

```py
import numpy as np
from scipy import integrate

from rich.console import Console
from rich.traceback import install

install()
console = Console()
```

Use the trapezoidal rule on evenly spaced points:

```py
console.print(integrate.trapezoid([1, 2, 3]))
```

```shell
4.0
```

The spacing between sample points can be selected by either the `x` or `dx` arguments:

```py
console.print(integrate.trapezoid([1, 2, 3], x=[4, 6, 8]))
console.print(integrate.trapezoid([1, 2, 3], dx=2))
```

```shell
8.0
8.0
```

Using a decreasing `x` corresponds to integrating in reverse:

```py
console.print(integrate.trapezoid([1, 2, 3], x=[8, 6, 4]))
```

```shell
-8.0
```

More generally `x` is used to integrate along a parametric curve. We can estimate the integral $\int_0^1 x^2 = \frac{1}{3}$ using:

```py
x = np.linspace(0, 1, num=50)
y = x**2
console.print(integrate.trapezoid(y, x))
```

```shell
0.33340274885464394
```

Or estimate the area of a circle, noting we repeat the sample which closes the curve:

```py
theta = np.linspace(0, 2 * np.pi, num=1000, endpoint=True)
console.print(integrate.trapezoid(np.cos(theta), x=np.sin(theta)))
```

```shell
3.141571941375841
```

`trapezoid` can be applied along a specified axis to do multiple computations in one call:

```py
a = np.arange(6).reshape(2, 3)
console.print(a)
console.print(integrate.trapezoid(a, axis=0))
console.print(integrate.trapezoid(a, axis=1))
```

```shell
[[0 1 2]
 [3 4 5]]

[1.5 2.5 3.5]

[2. 8.]
```

### scipy.integrate.cumulative_trapezoid

```py
scipy.integrate.cumulative_trapezoid(y, x=None, dx=1.0, axis=-1, initial=None)
```

#### Description

Cumulatively integrate y(x) using the composite trapezoidal rule.

#### Arguments

| Name | Type | Description |
|-|-|-|
|y|array_like|Values to integrate.|
|x|array_like, optional|The coordinate to integrate along. If None (default), use spacing dx between consecutive elements in y.|
|dx|float, optional|Spacing between elements of y. Only used if x is None.|
|axis|int, optional|Specifies the axis to cumulate. Default is -1 (last axis).|
|initial|scalar, optional|If given, insert this value at the beginning of the returned result. 0 or None are the only values accepted. Default is None, which means res has one element less than y along the axis of integration.|

> [!error]
> ***Deprecated since version 1.12.0:*** The option for non-zero inputs for initial will be deprecated in SciPy 1.15.0. After this time, a ValueError will be raised if initial is not None or 0.

#### Returns

| Type | Type | Description |
|-|-|-|
|res|ndarray|The result of cumulative integration of y along axis. If initial is None, the shape is such that the axis of integration has one less value than y. If initial is given, the shape is equal to that of y.|

#### Examples

Importing necessary libraries for all the examples:

```py
from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
```

```py
x = np.linspace(-2, 2, num=20)
y = x
y_int = integrate.cumulative_trapezoid(y, x, initial=0)
plt.plot(x, y_int, "ro", x, y[0] + 0.5 * x**2, "b-")
plt.show()
```

![](https://i.imgur.com/pPxRlQk.png)

### scipy.integrate.simpson

```py
scipy.integrate.simpson(y, *, x=None, dx=1.0, axis=-1)
```

#### Description

Integrate y(x) using samples along the given axis and the composite Simpson’s rule. If x is None, spacing of dx is assumed.

If there are an even number of samples, N, then there are an odd number of intervals (N-1), but Simpson’s rule requires an even number of intervals. The parameter ‘even’ controls how this is handled.

#### Arguments

| Name | Type | Description |
|-|-|-|
|y|array_like|Array to be integrated.|
|x|array_like, optional|If given, the points at which y is sampled.|
|dx|float, optional|Spacing of integration points along axis of x. Only used when x is None. Default is 1.|
|axis|int, optional|Axis along which to integrate. Default is the last axis.|

#### Returns

|Type|Description|
|-|-|
|float|The estimated integral computed with the composite Simpson’s rule.|

#### Examples

Importing necessary libraries for all the examples:

```py
from rich.console import Console
from rich.traceback import install

install()
console = Console()


from scipy import integrate
import numpy as np

x = np.arange(0, 10)
y = np.arange(0, 10)
```

```py
console.print(integrate.simpson(y, x=x))
```

```shell
40.5
```

Now changing the value of `y`:

```py
y = np.power(x, 3)
console.print(integrate.simpson(y, x=x))
console.print(integrate.quad(lambda x: x**3, 0, 9)[0])
```

```shell
1640.5
1640.25
```

### scipy.integrate.cumulative_simpson

```py
scipy.integrate.cumulative_simpson(y, *, x=None, dx=1.0, axis=-1, initial=None)
```

#### Description

Cumulatively integrate y(x) using the composite Simpson’s 1/3 rule. The integral of the samples at every point is calculated by assuming a quadratic relationship between each point and the two adjacent points.

#### Arguments

| Name | Type | Description |
|-|-|-|
|y|array_like|Values to integrate. Requires at least one point along axis. If two or fewer points are provided along axis, Simpson’s integration is not possible and the result is calculated with cumulative_trapezoid.|
|x|array_like, optional|The coordinate to integrate along. Must have the same shape as y or must be 1D with the same length as y along axis. x must also be strictly increasing along axis. If x is None (default), integration is performed using spacing dx between consecutive elements in y.|
|dx|scalar or array_like, optional|Spacing between elements of y. Only used if x is None. Can either be a float, or an array with the same shape as y, but of length one along axis. Default is 1.0.|
|axis|int, optional|Specifies the axis to integrate along. Default is -1 (last axis).|
|initial|scalar or array_like, optional|If given, insert this value at the beginning of the returned result, and add it to the rest of the result. Default is None, which means no value at x[0] is returned and res has one element less than y along the axis of integration. Can either be a float, or an array with the same shape as y, but of length one along axis.|

#### Returns

|Name|Type|Description|
|-|-|-|
|res|ndarray|The result of cumulative integration of y along axis. If initial is None, the shape is such that the axis of integration has one less value than y. If initial is given, the shape is equal to that of y.|

#### Examples

Importing necessary libraries for all the examples:

```py
from rich.console import Console
from rich.traceback import install

install()
console = Console()


from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
```

```py
x = np.linspace(-2, 2, num=20)
y = x**2
y_int = integrate.cumulative_simpson(y, x=x, initial=0)
fig, ax = plt.subplots()
ax.plot(x, y_int, 'ro', x, x**3/3 - (x[0])**3/3, 'b-')
ax.grid()
plt.show()
```

![](https://i.imgur.com/COc4IEu.png)

The output of `cumulative_simpson` is similar to that of iteratively calling `simpson` with successively higher upper limits of integration, but not identical.

```py

def cumulative_simpson_reference(y, x):
    return np.asarray([integrate.simpson(y[:i], x=x[:i]) for i in range(2, len(y) + 1)])


rng = np.random.default_rng()
x, y = rng.random(size=(2, 10))
x.sort()
res = integrate.cumulative_simpson(y, x=x)
ref = cumulative_simpson_reference(y, x)
equal = np.abs(res - ref) < 1e-15
console.print(equal)
```

```shell
[False  True False  True False  True False  True  True]
```

This is expected: because `cumulative_simpson` has access to more information than `simpson`, it can typically produce more accurate estimates of the underlying integral over subintervals.

### scipy.integrate.romb

```py
scipy.integrate.romb(y, dx=1.0, axis=-1, show=False)
```

#### Description

Romberg integration using samples of a function.

#### Arguments

| Name | Type | Description |
|-|-|-|
|y|array_like|A vector of `2**k + 1` equally-spaced samples of a function.|
|dx|float, optional|The sample spacing. Default is 1.|
|axis|int, optional|The axis along which to integrate. Default is -1 (last axis).|
|show|bool, optional|When y is a single 1-D array, then if this argument is True print the table showing Richardson extrapolation from the samples. Default is False.|

#### Returns

|Name|Type|Description|
|-|-|-|
|romb|ndarray|The integrated result for axis.|

#### Examples

Importing necessary libraries for all the examples:

```py
from rich.console import Console
from rich.traceback import install

install()
console = Console()


from scipy import integrate
import numpy as np
```

```py
x = np.arange(10, 14.25, 0.25)
y = np.arange(3, 12)
console.print(integrate.romb(y))
```

```shell
56.0
```

```py
y = np.sin(np.power(x, 2.5))
console.print(integrate.romb(y))
```

```shell
-0.7425613366722288
```

```py
console.print(integrate.romb(y, show=True))
```

```shell
Richardson Extrapolation Table for Romberg Integration
======================================================
-0.81576
 4.63862  6.45674
-1.10581 -3.02062 -3.65245
-2.57379 -3.06311 -3.06595 -3.05664
-1.34093 -0.92997 -0.78776 -0.75160 -0.74256
======================================================
-0.7425613366722288
```