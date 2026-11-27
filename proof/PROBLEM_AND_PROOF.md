# Ahn–Kerman Question 1.13

Does there exist a smooth path of global standard symplectomorphisms, starting at the identity, along which the mean width of the Lagrangian bidisk has nonzero derivative? Mean width averages the full directional width over spherical probability. The support definition applies to any compact image. [Original question, p. 4](https://arxiv.org/pdf/2311.02870v3#page=4)

Let $\chi$ be smooth, compactly supported and identically one near the bidisk. Use $H=\frac12\chi(\|x\|^2-\|y\|^2)(x\cdot y)$ and $X_H=(\nabla_y H,-\nabla_x H)$. The vector field is complete and its flow preserves the ambient symplectic form. Outside its support the flow fixes points.

For a unit direction $u=(a,b)$ with $a,b\ne0$, its unique maximizing point is $p=(a/\|a\|,b/\|b\|)=(x,y)$. At $p$, differentiation gives the velocity $(-(x\cdot y)y,-(x\cdot y)x)$. Its projection to $u$ is $-(\|a\|+\|b\|)(x\cdot y)^2$.

Maximizers for the moving support converge to $p$, by compactness and uniqueness at zero. Compare the value at $p$ to the maximum at time $t$, and bound the original value of a time-$t$ maximizer by its original maximum. These inequalities control the error after subtracting the projected linear term by $|t|$ times the change in projected velocity at the maximizing point, plus $O(t^2)$. This is $o(|t|)$ for either sign of $t$. The two excluded circles have spherical measure zero. A uniform difference-quotient bound follows from the bounded speed of the entire flow, allowing dominated convergence.

The squared component length $s=\|a\|^2$ is uniform on $[0,1]$. The independent circle directions give $\mathbb E(x\cdot y)^2=1/2$. Both component lengths have mean $2/3$. Antipodal invariance doubles the mean support derivative, giving $-2(2/3+2/3)(1/2)=-4/3$. The mean width strictly decreases for all sufficiently small positive times. [Detailed paper](../paper/manuscript.pdf)
