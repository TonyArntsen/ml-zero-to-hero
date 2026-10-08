# Vectors | Essence of Linear Algebra (Chapter 1)

*Based on [3Blue1Brown's Essence of Linear Algebra](https://www.youtube.com/watch?v=fNk_zzaMoSs)*

---

## 1. What is a Vector?

In linear algebra, a vector is fundamentally an arrow anchored at the origin $(0, 0)$ on a coordinate system.

* A vector like $\begin{bmatrix} 2 \\ 4 \end{bmatrix}$ represents moving **2 units along the x-axis** and **4 units along the y-axis**.
* An arrow is drawn starting from the origin $(0, 0)$ and ending at the coordinate point $(2, 4)$.

---

## 2. Vector Addition

Adding two vectors means combining their directional movements.

$$\begin{bmatrix} 2 \\ 4 \end{bmatrix} + \begin{bmatrix} 1 \\ 2 \end{bmatrix} = \begin{bmatrix} 2 + 1 \\ 4 + 2 \end{bmatrix} = \begin{bmatrix} 3 \\ 6 \end{bmatrix}$$

* **Geometric View:** Take the second arrow and place its tail at the tip of the first arrow (tip-to-tail method). The sum is the vector leading from the origin straight to the final point: 3 steps on the x-axis and 6 steps on the y-axis.

---

## 3. Vector Multiplication (Scaling)

In linear algebra, multiplying a vector by a number is called **scaling**. The number itself is referred to as a **scalar** because it changes the *scale* (length) of the vector.

### Geometric View
* **Multiplying by $2$:** Stretches the vector to twice its original length.
* **Multiplying by $\frac{1}{3}$:** Compresses (squishes) the vector down to one-third of its original length.
* **Multiplying by a negative number (e.g., $-1.8$):** Flips the vector around to point in the opposite direction and scales its length by $1.8$.

### Numerical View
To multiply a vector by a scalar, multiply each individual coordinate component by that scalar:

$$3 \cdot \begin{bmatrix} 2 \\ 4 \end{bmatrix} = \begin{bmatrix} 3 \cdot 2 \\ 3 \cdot 4 \end{bmatrix} = \begin{bmatrix} 6 \\ 12 \end{bmatrix}$$

---

## 4. The Three Perspectives on Vectors

| Perspective | Description | Focus |
| :--- | :--- | :--- |
| **Physics** | Arrows pointing in space | Defined purely by **length** and **direction**. As long as these two properties don't change, the vector can slide anywhere in space. |
| **Computer Science** | Ordered lists of numbers | Vectors are treated as fixed-length arrays (e.g., modeling a house as `[square_footage, price]`). |
| **Mathematician's** | Abstract objects | A vector can be *anything* where adding two objects or scaling an object by a number makes sense. |

---

## 5. Summary & Core Takeaway

Linear algebra roots vectors at the **origin** $(0, 0)$ and connects spatial intuition with numerical calculations:

* **Geometric Intuition:** Allows you to visualize transformations, movements, and spatial concepts.
* **Numerical Calculation:** Translates those spatial ideas into concrete coordinate data that computers can easily process.