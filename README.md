# Docker image using the Playwright python image as base

This branch explores using the [Playwright python image](https://github.com/microsoft/playwright-python) as a base for our container, since it includes both playwright and Chromium that we use for pdf conversion.

## Results
The application works as expected, but the image size is 4.22 GB. Other possible base images will be explored to reduce the size of our image.
