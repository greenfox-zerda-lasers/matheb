var heading = document.getElementsByTagName("h1");
alert(heading[0].textContent);
// 2. Write the content of the first paragraph to the console.
var paragraph = document.getElementsByTagName("p");
console.log(paragraph[0].textContent);
// 3. Alert the content of the second paragraph.
alert(paragraph[1].textContent);
// 4. Replace the heading's content with 'New content'.
heading[0].textContent = "New Content"
// 5. Replace the last paragraph's content with the first paragraph's content.
paragraph[paragraph.length-1].textContent = paragraph[0].textContent
