## 09_feedback

### How to explit
In feedback page, they also show the text we put on the screen again. I thought we could do XSS exploit again.

Same as 08, I put `<script>alert` for both 'name' and 'message' and I got a flag. 

To do this, I needed to change max_length.

FLAG : 0fbb54bbf7d099713ca4be297e1bc7da0173d8b3c21c1811b916a3a86652724e