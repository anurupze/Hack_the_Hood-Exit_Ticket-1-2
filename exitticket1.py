print()
print()
print()


print("This is my exit ticket today!")

print("Part I: More on Spotify Playlist")
# First, add the songs in your section's list again in 
playlist = [
    "Numb",
    "Destiny",
    "Time",
    "WOW",
    "Changes"
  ]

# Print the playlist in the line below:
print(playlist)

# What's the first song on your list? What number should you add in the index (inside the square backets " [ ] " ) in the next line to access the first song in the list?
print(playlist[0])

# # You can create a variable called favorite_song from the playlist to store it & use for concatenation (when you combine variables with strings in an ouput)
favorite_song = playlist[1]
# # # now print this song into a sentence:
print("My favorite song from the playlist is " + favorite_song)

# # You re-write the message about using f-strings to create a message based on a value from a list. When indexing the value from the list, use curly brackets. Here's how to re-write the above message using f-strings:
message = f"My favorite song from the playlist is {playlist[1]}."
print(message)

# # # Who sings your favorite song? Create a new variable of the artist/singer/musician by adding the name as a string. For example, "Break my Soul" is by Beyonce I would write it this way:
# # # artist = "Beyonce" # this is the example. Try yours in the next line:
artist = "Neffex"
#artist = "Ahmed Amin"
# # # now print the artist of that song
print(artist + " sings that song.")
# # # Now use f-strings to print the same thing now making the variable called message2. Follow the format from the previous example on lines 23 & 24.
message2 = f"My favorite song from the playlist is {playlist[1]}"
print(message2)

# # # Now, the next line concatenates or joins the variables together with other string words to make a sentence:
print("My favorite song is "+ favorite_song + " by " + artist)

# # Now use f-strings to print the same thing now making the variable called message3. Follow the format from the previous example on lines 23 & 24.
message3 =f"My favorite song from the playlist is {playlist[1]}"
print(message3)

# # # Finding the length of a list via len()
# # # How many songs are in your playlist? Write the number (integer) to create the variable songcount below: 
songcount = len(playlist) 
print(songcount)

# # # Now use f-strings to print the same thing now making the variable called message4. Follow the format from the previous example on lines 23 & 24.
message4 = f"My favorite song from the playlist is {playlist[1]}"
print(message4)

# # # Modify your playlist 
# # # Change the first song to "Yay Area" in the next line
playlist[0] = "Yay Area"
# # # Print playlist to confirm that "Yay Area" replaced the first song
print(playlist)
print("This is how you make a change!")

# # ## ADDING ELEMENTS
# print("Now we're gonna add songs to our playlist.")
# print("append() adds a new element to the end of the list.")
# # # Add another song to the end of the list using append(). In the next line, right now it shows "Purple Hearts" by Kendrick Lamar but you can change that to any other song of your liking
playlist.append("I miss the days")
# # # print the playlist to show that you added a new song
print(playlist)

# # # You changed your mind & want to delete the last song you just added using pop()
playlist.pop()
# # # In the next line, print the playlist to show that you deleted the last song
print(playlist)

# # ## Now add another song (element) to the playlist (list) using insert(). The index indicates the position of where the new song will be added. Here's how to add a song to the front of the list. This is "Moscow Mule" by Bad Bunny, but you can play around and add a different song:
playlist.insert(0, "Your Heart")
print(playlist)

# # # You changed your mind and decided to take out the last song you just added! However, this time you want take out it out of this playlist AND to put it in another playlist. Here's how you can do that:
popped_song = [playlist.pop()]
print(playlist)
print(popped_song)

# # You're doing a great job!
# # You're almost done with this coding activity!
# # Keep going!
# # You're amazing!

# # # Now, going back to PLAYLIST, you can actually pop elements from any position in a list. However, remember that the item you pop will no longer be stored in the list you took it out from. Remove the 2nd song from the playlist using pop:
playlist.pop(1)
print(playlist)

# # You changed your mind once again & want to add "Yay Area" once again." Do you remember how to add
playlist.insert(1,"Yay Area")
print(playlist)
# # Now you want to remove "Yay Area" using remove(). You can also then put it in another playlist. Here's how you can do that:
yay_song = "Yay Area"
playlist.remove(yay_song)
print(playlist)
print(yay_song)
# # \n = creates a new line in the code
print(f"\n {yay_song} is a Bay Area anthem!")

# # You change your mind a final time & want to delete the last song in the playlist. You can also use del to do that:
del playlist[-1]
print(playlist)

# # Sort your playlist in alphabetical order using sorted()
print(sorted(playlist))
# # Write here the order of the songs in your playlist:
# # Destiny, Time, Your Heart