import imageio.v2 as imageio
import os


path = os.getcwd()

path = os.path.join(path, str(input("input folder in cwd  with image: ")))

files = os.listdir(path)




files = sorted(files, key=lambda el: int(el.split(".")[0]))
print(files)


images = []
for file in files:
    if file.endswith('.png'):
        file_path = os.path.join(path, file)
        images.append(imageio.imread(file_path))
gif_path = "1.gif"


imageio.mimsave(gif_path, images, duration=10)
