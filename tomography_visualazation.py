from skimage import io
import matplotlib.pyplot as plt
import matplotlib.animation as animation
fig = plt.figure()
struct_arr = io.imread('attention-mri.tif')
struct_arr2 = struct_arr.T
ims = []
for img in struct_arr2:
    im = plt.imshow(img, animated=True)
    ims.append([im])
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,
                                repeat_delay=500)
plt.show()