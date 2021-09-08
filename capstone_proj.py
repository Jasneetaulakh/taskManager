

#I HAVE WRITTEN MY NOTES IN CAPS TO MAKE IT EASY TO DIFFERENTIATE MY NOTES FROM THE EXAMPLE NOTES



import pygame # Imports a game library that lets you use specific functions in your program.
import random # Import to generate random numbers. 

# Initialize the pygame modules to get everything started.

pygame.init() 

# The screen that will be created needs a width and a height.

screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height)) # This creates the screen and gives it the width and height specified as a 2 item sequence.

# This creates the player and gives it the image found in this folder (similarly with the enemy image).

#HERE I'VE ADDED TWO MORE ENEMIES AND A PRIZE IMAGE

player = pygame.image.load("image.png")
enemy = pygame.image.load("enemy.png")
enemy2 = pygame.image.load("enemy.png")
enemy3 = pygame.image.load("monster.jpg")
prize = pygame.image.load("prize.jpg")

# Get the width and height of the images in order to do boundary detection (i.e. make sure the image stays within screen boundaries or know when the image is off the screen).

#GET HEIGHT AND WIDTH OF THE IMAGES 

image_height = player.get_height()
image_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

print("This is the height of the player image: " +str(image_height))
print("This is the width of the player image: " +str(image_width))

# Store the positions of the player and enemy as variables so that you can change them later. 

playerXPosition = 100
playerYPosition = 50

# Make the enemy start off screen and at a random y position.

#enemyXPosition =  screen_width
#enemyYPosition =  random.randint(0, screen_height - enemy_height)

#ENEMY2 STARTS IN POSITION X BUT RANDOM Y POSITION
#ENEMY3 DOESNT HAVE A RANDOM POSITION, ALWAYS STARTS IN THE SAME PLACE, BUT COMES FROM OFF SCREEN TO ON SCREEN
#PRIZE POSITON IS ALWAYS IN THE SAME PLACE, MIDDLE-ISH OF THE SCREEN

enemyXPosition= screen_width
enemyYPosition= random.randint(0,screen_height-enemy_height)

enemy2XPosition = 150
enemy2YPosition = random.randint(0, screen_height-enemy2_height)

enemy3XPosition = 300
enemy3YPosition = screen_height

prizeXPosition = 500
prizeYPosition = 300



# This checks if the up or down key is pressed.
# Right now they are not so make them equal to the boolean value (True or False) of False. 
# Boolean values are True or False values that can be used to test conditions and test states that are binary, i.e. either one way or the other. 

keyUp= False
keyDown = False
keyLeft = False
keyRight = False

# This is the game loop.
# In games you will need to run the game logic over and over again.
# You need to refresh/update the screen window and apply changes to 
# represent real time game play. 

while 1: # This is a looping structure that will loop the indented code until you tell it to stop(in the event where you exit the program by quitting). In Python the int 1 has the boolean value of 'true'.
    #In fact numbers greater than 0 also do. 0 on the other hand has a boolean value of false. You can test this out with the bool(...) function to see what boolean value types have.
    #You will learn more about while loop structers later. 

    screen.fill(0) # Clears the screen.
    screen.blit(player, (playerXPosition, playerYPosition))# This draws the player image to the screen at the postion specfied. I.e. (100, 50).
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    pygame.display.flip()# This updates the screen. 
    
    # This loops through events in the game.
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is the one we want.

            #CHECKES IF LEFT/RIGHT PRESSED IS THE RIGHT ONE WE WANT
            
            if event.key == pygame.K_UP: # pygame.K_UP represents a keyboard key constant. 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
            
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:

        
            # Test if the key released is the one we want.
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    # After events are checked for in the for loop above and values are set,
    # check key pressed values and move player accordingly.
    
    # The coordinate system of the game window(screen) is that the top left corner is (0, 0).
    # This means that if you want the player to move down you will have to increase the y position.

    #IF YOU WANT TO MOVE THE PLAYER RIGHT, YOU HAVE TO INCREASE THE X POSITION AND DECREASE FOR LEFT
    
    if keyUp == True:
        if playerYPosition > 0 : # This makes sure that the user does not move the player above the window.
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - image_height:# This makes sure that the user does not move the player below the window.
            playerYPosition += 1
    if keyLeft == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition -=1
    if keyRight == True:
        if playerXPosition < screen_width - image_width:
            playerXPosition +=1
    
    # Check for collision of the enemy with the player.
    # To do this we need bounding boxes around the images of the player and enemy.
    # We the need to test if these boxes intersect. If they do then there is a collision.
    
    # Bounding box for the player:
    
    playerBox = pygame.Rect(player.get_rect())
    
    # The following updates the playerBox position to the player's position,
    # in effect making the box stay around the player image. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition
    
    # Bounding box for the enemy:
    
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    #BOUNDING BOX FOR ENEMIES AND PRIZE 
    
    enemy2Box = pygame.Rect(enemy2.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.right = enemy2YPosition

    enemy3Box = pygame.Rect(enemy.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    prizeBox = pygame.Rect(player.get_rect())
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition


    
    # Test collision of the boxes:
    
    if playerBox.colliderect(enemyBox) or playerBox.colliderect(enemy2Box) or playerBox.colliderect(enemy3Box):

        print("You lose!")
        pygame.quit()
        exit()

        #IF PLAYER COLLIDES WITH PRIZE, PRINT YOU WIN AND EXIT THE GAME
        
    if playerBox.colliderect(prizeBox):

        print("You win!")
        pygame.quit()
        exit()
        
      
        
    # If the enemy is off the screen the user wins the game:
    
    if enemyXPosition < 0 - enemy_width:
        print("endofline")
        enemyXPosition= screen_width
        enemyYPosition= random.randint(0,screen_height-enemy_height)


    #ENEMY2 APPROACEHS FROM THE LEFT AND MOVES RIGHT
    #ENEMY3 MOVES UP 
    
    # Make enemy approach the player.
    
    enemyXPosition -= 0.15
    enemy2XPosition += 0.15
    enemy3YPosition -= 0.25
    
    # ================The game loop logic ends here. =============
  
