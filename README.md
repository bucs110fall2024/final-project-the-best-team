Team Name: The Best Team
Team Members: Max Zapesochny
Project Name: Joe Mann the Bowman
Project Description: In this game you play as Joe Mann, an unlucky archer who just wants to get home. Unfortunately an evil wizard has imprisoned Joe in an invisible box and and created enemies who wish only to kill him. Joe Mann the Bowman can shoot his bow to stop enemies from coming at him, but beware because Joe has limited arrows and must constantly refill by collecting quivers from around the game map. 
Program Features:
    Start screen
    Gameover screen
    Player movement
    Player faces towards cursor
    Player can shoot arrows in direction of cursor
    Player can run out of arrows and has to pick up more off ground
    Arrows can hit enemies killing them
    Enemies run towards the Player
    If enemies touch player, player loses health
    Player can pick up bags of arrows that spawn in to regain arrows
    Arrows face the direction that they are going
    Enemies always face the player
Class Descriptions:
    Controller: controls all player input as well as calculating everything in the game.
    Player: controls the health, cordinates, and angle of the player, as well as the amount of arrows the player has
    Enemy: controls the enemies which come towards the player and all their stats like cordinates, angle, and how they move towards the player and what direction they face
    Arrow: controls the arrows that the player fires cordinates and angle. controls the way the arrow moves using it's angle and the set arrow_speed, give it a set trajectory
    Quiver: controls the cordinates of the bags of arrows that the player can pick up. The initization simply puts the quiver in a random spot on the game map.
ATP:
Test Case 1: Player Movement

    Test Description: Verify that the player moves in all directions as expected.
    Test Steps:
    Start the game.
    Press any button
    Hold the w key.
    Verify that the player moves up.
    Hold the a key.
    Verify that the player moves left.
    Hold the s key.
    Verify that the player moves down.
    Hold the d key.
    Verify that the player moves right.
    Expected Outcome: The player should move left and right in response to the wasd keys

Test Case 2: Player Turning detection
    Test Description: Ensure that the player is always facing towards the mouse
    Test Steps:
    Start the game.
    Press any button
    Move mouse in clockwise direction around the player
    Verify that player character's eyes are always facing the cursor
    Expected Outcome: Player character's eyes should always face the cursor

Test Case 3: Arrow Flight Direction
    Test Description: Ensure that arrows are flying in the right direction as well as if there tips are facing the direction they are going
    Test Steps:
    Start the game.
    Press any button
    Fire a player's arrow into the distance
    Verify that the arrow goes from the player towards the cursor
    Verify that the tip of arrow is parralel to the direction of the arrows trajectory
    Verify that this happens when player is facing NE, NW, SE, and SW directions
    Expected Outcome: Arrows should go towards the direction of the cursor towards the player and the arrows model should be facing the correct direction, which is with the head of the arrow being at the front

Test Case 4: Enemy Movement
    Test Description: Ensure that enemies are moving towards player
    Test Steps:
    Start the game.
    Press any button
    Wait for enemies to spawn in.
    Verify that the enemies are moving towards the player location
    Move player to new location
    Verify that enemies are still moving towards player
    Verify that enemies will eventually reach the players location
    Expected Outcome: Enemies should always move towards the player

Test Case 5: Arrow collision detection
    Test Description: Ensure that when an arrow hits an enemie that the enemy is killed
    Test Steps:
    Start the game.
    Press any button
    Wait for enemies to spawn in.
    Shoot arrow at enemy.
    Wait for arrow to hit target
    Ensure when arrow hits enemy that both the enemy and arrow are deleted
    Expected Outcome: When arrows hit enemies both object should be removed from the game.

Test Case 6: Enemy collision detection
    Test Description: Ensure that collisions between the player and enemies damage the player.
    Test Steps:
    Start the game.
    Press any button
    Wait for enemy to reach player
    Ensure enemy touches player
    Ensure enemy is deleted and top left bar shows one less heart of health
    Expected Outcome: Enemy should be killed after touching player and player should lose 1 heart
    
Test Case 7: Game Over Condition
    Test Description: Confirm that the game ends when the player loses all lives.
    Test Steps:
    Start the game.
    Press any button
    Play until the player loses all lives.
    Verify that the game displays a "Game Over" message.
    Expected Outcome: The game should display a "Game Over" message when the player loses all lives.
Test Case 8: Quiver Pickup detection

    Test Description: Test that when player character goes to quiver icon his arrows increase and quiver disappears
    Test Steps:
    Start the game.
    Press any button
    Wait for Quivers to spawn
    walk player over quiver
    Ensure quiver disappears
    Ensure players amount of arrows increases by at least two
    Expected Outcome: Player gains a random amount of arrows and that specific quiver item disappears from game.
Test Case 9: Start Menu Navigation

Test Description: Verify that the program handles unexpected inputs gracefully.
Test Steps:
Start the game.
Press any button
Ensure player reaches main screen with health, arrow amount, and player character in center
Expected Outcome: User reaches main screen.


