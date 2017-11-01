# This was an achievement! I solved a problem using Regex!

import re

n = int(input())

for i in range(n):
	# Original string
    so = input()
    # Final string
    sf = ''

    # Count / Price variable that is incremented
    count = 0
    # Starts sf as having the first letter of so
    # and increments count
    sf += so[0]
    count += 1
    so = so[1:]

    # Runs while there are still characters in so left
    # to add to sf
    while len(so) > 0:
    	# Iterates through the current value of sf, looking for
        # any matches using regex
        for i in range(len(sf)):
        	# If a match is found, it is removed from so
            # and added to sf
            while len(re.findall(sf[i:], so)) > 0:
                foundPhrase = re.findall(sf[i:], so)[0]
                sf += foundPhrase
                so = so.replace(foundPhrase, '')
        # Stops the loop if the nested loop above
        # removed all characters from so
        if len(so) == 0:
            break
        # If not, then the first letter of so is added to sf
        # and count is incremented
        sf += so[0]
        count += 1
        so = so[1:]

    print(count)


# Alternative solution (Much simpler; this makes me feel dumb)

import string

n = int(input())

for i in range(n):
    s = input()
    count = 0
    for char in string.ascii_lowercase:
        if char in s:
            count+=1

    print(count)
