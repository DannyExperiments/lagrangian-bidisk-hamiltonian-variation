# Directional support derivative

[Download the offline explorer ZIP](https://raw.githubusercontent.com/DannyExperiments/lagrangian-bidisk-hamiltonian-variation/refs/tags/v1.0.0/visualization/lagrangian-bidisk-hamiltonian-variation-explorer.zip), extract it, then open index.html in a browser. The controls choose the squared length proportion and relative angle, recall the exact rational fixture or an orthogonal direction, and rotate the camera.

The GIF and explorer plot the derivative of one support value as the graph of $-(\sqrt{s}+\sqrt{1-s})\cos^2\theta$. Here $s=\|a\|^2$ for a direction $(a,b)\in S^3$ and $\theta$ is the angle between normalized disk directions. The worked point has $s=9/25$ and $\cos\theta=3/5$, giving exact support rate $-63/125$. The full directional-width derivative is $-126/125$ at that point. The mean-width derivative $-4/3$ comes from an analytic spherical average of both opposite support values.

The displayed surface omits the zero-component directions, where the linear functional does not have a unique maximizer on the bidisk. Camera rotation shows the same support derivative in different perspectives. A Python environment with Pillow and Arial or DejaVu Sans can regenerate the GIF with the following command.

    python3 visualization/render.py
