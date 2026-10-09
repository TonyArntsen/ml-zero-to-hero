# Linear Regression: Ordinary Least Squares (OLS) Calculations

Linear regression models the relationship between an independent variable $X$ and a dependent variable $Y$ using a straight line. The equation of the line is defined as:

$$\hat{y} = mx + b$$

Where:
* $\hat{y}$ is the predicted output value.
* $x$ is the input feature value.
* $m$ is the slope (weight) of the line.
* $b$ is the intercept (bias) of the line.

---

## 1. Calculating the Means

First, we calculate the arithmetic mean (average) of both the $X$ and $Y$ data arrays, where $N$ is the total number of data points:

$$\bar{x} = \frac{1}{N} \sum_{i=1}^{N} x_i$$

$$\bar{y} = \frac{1}{N} \sum_{i=1}^{N} y_i$$

---

## 2. Calculating the Slope ($m$)

The slope represents the rate of change of $Y$ relative to $X$. It is computed using the covariance of $X$ and $Y$ divided by the variance of $X$:

$$m = \frac{\sum_{i=1}^{N} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{N} (x_i - \bar{x})^2}$$

---

## 3. Calculating the Intercept ($b$)

Once the slope ($m$) is known, the intercept is calculated using the means of $X$ and $Y$ to ensure the regression line passes through the point $(\bar{x}, \bar{y})$:

$$b = \bar{y} - m\bar{x}$$