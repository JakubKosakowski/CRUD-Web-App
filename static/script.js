const btn = document.querySelector('.random')
const field = document.querySelector("#favorite_color")

var colors = ['red', 'blue', 'green', 'yellow']

console.log("Connect");

btn.addEventListener("click", function(){
    field.value = colors[Math.floor(Math.random()*colors.length)];
});