# Encryption
I made an algorithm that encrypt/decrypt text with only some of the characters avaiable, given a key and the text.

# Is it safe?
Actually, I don't even know if this is applicable on a real-world project: there are not key-exchange systems, it is only one file with some functions. I am far from an expert on Computer Science: I am just having fun building some algorithms/tools. This is  *for fun only*.

# What it is?
I made an algorithm to encrypt a message with limited amount of characters *(but you can add if you want, it is as easy as adding at "alf" list)*.

# Input and output:
Input: a str (with characters avaiable in "alf" list only) and a key for both of the functions (Encryption and Decryption).
Output: text encrypted/decrypted.

# How it works:
The key is transformed into a list made its digits separared in pairs. If the number of digits is odd, an "0" will be added on the last element of the list
<br/>Ex1: the key 1234 is transformed in [12, 34]
<br/>Ex2: the key 1235 is transformed in [12, 34, 50]
<br/><br/>
A variable "current" keeps track of the current index of the key. For each time that we move a character on the str, the current will be updated.
<br/>
Then, every character of the str receives a value (according to its position on the alf list), which is added to the value of the key[current].
<br/><br/>
Ex: txt = "abcabc", key = 12345678. Lets suppose that the alf for this example is [a, b, c, d, e], meaning  that a = 0, b = 1, c = 2, d = 3 and e = 4<br/>
For each letter on the text, two digits of the key will be  added to the value of the letter:<br/>
key --> [12, 34, 56, 78]<br/>
a --> 0 + 12 = 12. Since there is  no othe number with the value of 12, we will subtract the (highest value + 1) from this value until it is correspondent to another digit.
<br/> 12 - 5 = 7 - 5 = 2 --> value of "c"
<br/>Then, "c" would be the first letter of the encrypted txt.<br/>
b --> 1 + 34 = 35. Since there is  no number with the value of 35, we will subtract the (highest value + 1) from this value until it is correspondent to another digit.
<br/> 35 - 5 = 30 - 5 = 25 - 5 = 20 - 5 = 15 - 10 = 5 - 5 = 0 --> value of "a"
<br/>Then, "a" would be the second letter of the encrypted txt. 
<br/>This would happen until there are no more digits to be encrypted. If current == len(key), current goes back to the beginning, receiving the value of 0.
<br/><br/>
Decryption:
<br/>It is the opposite from the encryption: we get the value of the encrypted digit, add the key[current], and subtract from len(alf) until the value is represented by a digit. This digit will be the decrypted digit.
