from image import Image
import numpy as np

def brighten(image, factor):
    # when we brighten, we just want to make each channel higher by some amount 
    # factor is a value > 0, how much you want to brighten the image by (< 1 = darken, > 1 = brighten)
    
    #get all the data from the image we already input
    x_pixels, y_pixels, num_channels = image.array.shape
    
    # create our new image of same size so we don't overwrite the old picture
    new_image = Image(x_pixels=x_pixels, y_pixels= y_pixels, num_channels=num_channels)

    # the most intuitive but slow way to accomplish this...Is by reading the file bitwise and chanelwise
    # for x in range(x_pixels):
    #    for y in range(y_pixels):
    #        for c in range(num_channels):
    #            new_image.array[x, y, c] = image.array[x, y, c] * factor """

    # vectorized, so faster but more complicated version
    new_image.array = image.array * factor

    # returns the new image 
    return new_image


def adjust_contrast(image, factor, mid=0.5):
    # adjust the contrast by increasing the difference from the user-defined midpoint by factor amount
    
    # get all the data from the image we already input
    x_pixels, y_pixels, num_channels = image.array.shape
    
    # create our new image of same size so we don't overwrite the old picture
    new_image = Image(x_pixels=x_pixels, y_pixels= y_pixels, num_channels=num_channels)

    # the most intuitive but slow way to accomplish this...Is by reading the file bitwise and chanelwise
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_image.array[x, y, c] = (image.array[x, y, c]- mid) * factor + mid
    
    return new_image


def blur(image, kernel_size):
    # kernel size is the number of pixels to take into account when applying the blur
    # (ie kernel_size = 3 would be neighbors to the left/right, top/bottom, and diagonals)
    # kernel size should always be an *odd* number
    
    # get all the data from the image we already input
    x_pixels, y_pixels, num_channels = image.array.shape
    
    # create our new image of same size so we don't overwrite the old picture
    new_image = Image(x_pixels=x_pixels, y_pixels= y_pixels, num_channels=num_channels)

    neighbor_range = kernel_size // 2 

    # the most intuitive but slow way to accomplish this...Is by reading the file bitwise and chanelwise
    # The problem here is, that for the borders of the image, we take less and less pixels to average as we 
    # come to the point were image_border - coordinate < neighbor_range. This is not too important however, as 
    # The neighbor_range is very small in comparison to the entire picture bounds
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                # we take this pixel and all pixels in the neighbor range and add them all 
                for x_i in range(max(0, x-neighbor_range), min(x_pixels-1, x+neighbor_range)):
                    for y_i in range(max(0, y-neighbor_range), min(y_pixels-1, y+neighbor_range)):
                        total += image.array[x_i, y_i, c]
                # at the end we need to devide the total by all the pixels we averaged d
                new_image.array[x, y, c] = total / (kernel_size ** 2)
    return new_image


def apply_kernel(image, kernel):
    # the kernel should be a 2D array that represents the kernel we'll use!
    # for the sake of simiplicity of this implementation, let's assume that the kernel is SQUARE

    # get all the data from the image we already input
    x_pixels, y_pixels, num_channels = image.array.shape
    
    # create our new image of same size so we don't overwrite the old picture
    new_image = Image(x_pixels=x_pixels, y_pixels= y_pixels, num_channels=num_channels)

    neighbor_range = kernel.shape[0] // 2 

    # the most intuitive but slow way to accomplish this...Is by reading the file bitwise and chanelwise
    # The problem here is, that for the borders of the image, we take less and less pixels to average as we 
    # come to the point were image_border - coordinate < neighbor_range. This is not too important however, as 
    # The neighbor_range is very small in comparison to the entire picture bounds
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                total = 0
                # we take this pixel and all pixels in the neighbor range and add them all 
                for x_i in range(max(0, x-neighbor_range), min(new_image.x_pixels-1, x+neighbor_range) + 1):
                    for y_i in range(max(0, y-neighbor_range), min(new_image.y_pixels-1, y+neighbor_range) + 1):
                        # we need to find which value of the kernel this corresponds to
                        x_k = x_i + neighbor_range - x
                        y_k = y_i + neighbor_range - y 
                        # we then multiply the corresponding kernel value with the respective image kernel to get the desired effect
                        kernel_val = kernel[x_k, y_k]
                        total += image.array[x_i, y_i, c] * kernel_val
                new_image.array[x, y, c] = total
            
    return new_image


def combine_images(image1, image2):
    # let's combine two images using the squared sum of squares: value = sqrt(value_1**2, value_2**2)
    # size of image1 and image2 MUST be the same
    
    # get all the data from the image we already input
    x_pixels, y_pixels, num_channels = image1.array.shape
    
    # create our new image of same size so we don't overwrite the old picture
    new_image = Image(x_pixels=x_pixels, y_pixels= y_pixels, num_channels=num_channels)

    #just add every squared value from both images, add them and then take the square root to get combined image :D
    for x in range(x_pixels):
        for y in range(y_pixels):
            for c in range(num_channels):
                new_image.array[x, y, c] = ((image1.array[x, y, c]**2 + image2.array[x, y, c]**2)**0.5)
    
    return new_image

if __name__ == '__main__':
    lake = Image(filename='lake.png')
    city = Image(filename='city.png')
    

    #lightening the lake
    darkened_im = brighten(lake, 0.3)
    darkened_im.write_image("lake_darker.png")

    # adjust contrast
    increase_contrast=adjust_contrast(lake, 2, 0.5)
    increase_contrast.write_image("increased_contrast.png")

    # blur
    blur_city=blur(city, 45)
    blur_city.write_image("blur_45k.png")

    # lets try out the sobel edge detection kernel...
    sobel_x_kernel = np.array([
        [1, 2, 1], 
        [0, 0, 0], 
        [-1, -2, -1]
        ])

    sobel_y_kernel = np.array([
        [1, 0, -1],
        [2, 0, -2], 
        [1, 0, -1]
        ])

    sobe_x = apply_kernel(lake, sobel_x_kernel)
    sobe_x.write_image("sobel_x.png")

    sobe_y = apply_kernel(lake, sobel_y_kernel)
    sobe_y.write_image("sobel_y.png")

    # combine both :)
    sobe_xy = combine_images(sobe_x, sobe_y)
    sobe_xy.write_image("sobel_xy.png")


