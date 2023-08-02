## Description

Create a Django project with a page to upload an image `/`. On that page a user can pick an image from disk (no authentication required) and upload it to the server.
  - There's a quota of 10 uploads per day per IP.

After a successful upload, redirect to the image details page.
  - It includes
    - The uploaded image.
    - The date of the upload.
    - A button to delete the image. **Only** the person who did the upload can do this action.
  - The url `/image/<unique-identifier>/`.
    - is unique and sharable.
    - should **not include** the primary key.

Notes:
- The project must run inside a container. See below.
- Your solution will be judged based on readability, correctness and concision.
- This task should not take more than 1 hour.
- If you have extra time, add unit tests, type annotations, upload multiple files at once.

## Submission (Important!)
- Create a zip file django_exercise.zip
- After it's unzipped, it should contain the project source code.
- To run the server, we should be able to create a Docker image and run it. Here's what we will use:

```shell
unzip django_exercise.zip
cd django_exercise
docker build -t exercise .
docker run --rm -p 8000:8000 -v $(pwd):/app exercise
```
