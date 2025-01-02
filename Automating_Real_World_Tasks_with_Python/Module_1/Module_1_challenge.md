## Module 1 challenge: Scale and convert images using PIL


**Questions:**

**1. You're working on a project and need to use some image files that are compressed in a file named images.zip. Which of the following options will allow you to access the images for use?**

> Change the file extension of images.zip to .jpg.  (Incorrect)
>
> Ignore images.zip and download the images individually from the source again. (Incorrect)
>
> **Unzip the images.zip file using the unzip command.** (Correct)
>
> Try to open images.zip directly in your photo editing software. (Incorrect)

---


**2. You downloaded a Python library that lets you manipulate images and add text overlays. What's the most likely name for this library?**

> Fresco (Image Processing Framework) (Incorrect)
>
> Canvas (Graphics Library) (Incorrect)
>
> Stencil (Image Editing Toolkit) (Incorrect)
>
> **Pillow (Python Imaging Library)** (Correct)


---

**3. Imagine you created a Python script to download and organize your favorite music files. After saving the script, how can you ensure you can run it by typing its name in the terminal?**

> Open a Python interpreter and import your script as a module. (Incorrect)
>
> Rename the script to include the word "download" in the filename. (Incorrect)
>
> **Change the file permissions with chmod +x <script_name>.py.** (Correct)
>
> Run the script by double-clicking it in your file explorer. (Incorrect)


---


**4. Imagine you created a script to resize all images in a folder to a standard size and store them in the /opt/icons directory. After running the script, which command would show you the names of the resized images?**

> Review the lab Qwiklabs assessment: Scale and convert images using PIL (Incorrect)
>
> D. The script will automatically display a success message with filenames upon completion. (Incorrect)
>
> **Use the ls /opt/icons command to list the contents of the directory.** (Correct)
>
> B. Open the script and search for the logic related to naming the resized images. (Incorrect)


---


**5. You're writing a script to resize images to a specific size. After opening an image, how can you access its original dimensions before resizing?**

> **Utilize the img.size attribute to get the image's width and height as a tuple.** (Correct)
>
> Load a preview of the image using a graphical library and estimate the size visually. (Incorrect)
>
> Check the filename, as some filenames might embed image size information. (Incorrect)
>
> The script cannot access the original dimensions after opening the image for resizing. (Incorrect)


---


**6. You're building a Python application that automatically resizes images to fit a specific layout. After opening an image for resizing, which code snippet would reveal its original dimensions before any modifications?**

> The script will overwrite the original dimensions upon opening the image, so this information is no longer accessible. (Incorrect)
>
> Load a preview of the image and use a graphical library to estimate the size visually before resizing. (Incorrect)
>
> Search for the filename extension (e.g., ".jpg") as some formats might embed size data there. (Incorrect)
>
> **Use print(img.size) to get the original width and height as a tuple.** (Correct)


---


**7. Imagine you're building a mobile app that displays weather information. How can you efficiently access weather data without manually collecting it from weather stations around the world?**

> Hire a meteorologist to provide real-time weather updates for your app. (Incorrect)
>
> Purchase weather data directly from individual weather stations and write code to parse their data format. (Incorrect)
>
> Employ web scraping techniques to extract data from weather websites. (Less efficient)
>
> **Use a library or code framework that provides an API for a weather service.** (Correct)


---


**8. You're managing a company website that experiences traffic spikes throughout the day. A distributed computing system could be a good solution because:**

> All user requests must be processed by a single central server in a distributed system, creating a bottleneck. (Incorrect)
>
> Distributed systems are complex to manage and not ideal for simple web applications. (Not always true)
>
> **It enables you to scale the system resources (web servers) up or down depending on real-time traffic demands.** (Correct)
>
> Security is a major concern with distributed systems as they involve multiple interconnected machines. (Security can be addressed with proper configuration)

---


**9. Your company's e-commerce website experiences a surge in traffic during peak holiday seasons. To ensure smooth operation and prevent downtime, which approach would be most beneficial?**

> Hire additional customer service representatives to handle the increased customer inquiries during peak seasons. (Incorrect)
>
> Reduce website functionality during peak times to minimize resource usage and prevent crashes. (Incorrect)
>
> **Implement a distributed system architecture to distribute processing load across multiple servers, improving scalability and handling high traffic volume.** (Correct)
>
> Upgrade the existing server with the most powerful hardware possible to centralize all processing and data. (Less scalable)

---


**10. After a period of development, you realize your Docker environment has accumulated a significant amount of data, including unused Docker images. How can you safely remove these unused images to reclaim disk space?**

> Back up all your Docker images and then delete everything using docker system prune -f. (Overly aggressive)
>
> Unused images don't consume significant space, so there's no need to worry about removing them. (Incorrect)
>
> **Execute the docker image prune command to target only unused images for removal.** (Correct)
>
> Stop all running containers and then use docker rmi to remove all images. (Too broad, may remove images in use)
