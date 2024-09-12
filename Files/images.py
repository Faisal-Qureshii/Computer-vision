import cv2
import os

def load_and_show_image(image_path):
    # Print the current working directory
    print("Current Working Directory:", os.getcwd())
    
    # Load the image using OpenCV
    image = cv2.imread(image_path)
    
    # Check if the image is loaded properly
    if image is None:
        print(f"Error: Couldn't load image at {image_path}")
        return

    # Display the image in a window
    cv2.imshow('Loaded Image', image)
    
    # Wait indefinitely for a key press
    cv2.waitKey(0)
    
    # Destroy the window when a key is pressed
    cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    image_path = './Images/1.jpeg'  # Update this if necessary
    load_and_show_image(image_path)
