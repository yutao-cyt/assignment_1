from turtle import *

def draw_colorful_pattern():
    # Setup painting properties (similar to your code style)
    speed(0)              # Maximum speed for smooth drawing
    bgcolor("midnightblue") # Choose a striking background color
    pensize(2)            # Define the initial pen size
    
    # List of vibrant colors for dynamic color changes
    colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]
    
    # Move to starting position
    penup()
    goto(0, 0)
    pendown()
    
    # Incorporate structured for loops with dynamic color & length
    for i in range(200):
        # Dynamically change the pen color in each iteration
        color(colors[i % len(colors)])
        
        # Begin filling shapes to create a rich visual pattern
        begin_fill()
        
        # Dynamically change length and draw a geometric element (star-like motif)
        forward(i * 1.2)
        left(144)  # Standard angle to form a star shape path
        
        end_fill()

    # Hide turtle and finish
    hideturtle()
    done()

# Run the function
if __name__ == "__main__":
    draw_colorful_pattern()
