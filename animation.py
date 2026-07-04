import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.transforms import Affine2D


def draw_toast(ax, toast):

    ax.clear()
    ax.set_xlim(-0.1, 0.4)
    ax.set_ylim(-0.05, max(1.0, toast.y + 0.1))

    ax.set_aspect("equal")

    # Floor
    ax.axhline(0, color="black", linewidth=2)

    bread = patches.Rectangle(
        (
            toast.x - toast.length/2,
            toast.y - toast.bread_thickness/2
        ),
        toast.length,
        toast.bread_thickness,
        facecolor="wheat",
        edgecolor="black"
    )

    pb = patches.Rectangle(
        (
            toast.x - toast.length/2,
            toast.y + toast.bread_thickness/2
        ),
        toast.length,
        toast.pb_thickness,
        facecolor="saddlebrown",
        edgecolor="black"
    )

    transform = (
        Affine2D()
        .rotate_around(
            toast.x,
            toast.y,
            toast.theta
        )
        + ax.transData
    )

    bread.set_transform(transform)
    pb.set_transform(transform)

    ax.add_patch(bread)
    ax.add_patch(pb)

    plt.pause(0.001)